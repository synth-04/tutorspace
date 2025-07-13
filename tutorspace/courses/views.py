from django.db.models import Q
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Course, Module, Content
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import StudentSignUpForm


def index(request):
    return render(request, 'index.html' )

class CourseListView(ListView, LoginRequiredMixin):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        user_groups = self.request.user.groups.all()
        return Course.objects.filter(
            Q(allowed_groups__in=user_groups)
        ).distinct()

class CourseDetailView(DetailView, LoginRequiredMixin):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'

    def get_queryset(self):
        user_groups = self.request.user.groups.all()
        return Course.objects.filter(
            allowed_groups__in=user_groups
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_groups = self.request.user.groups.all()
        context['modules'] = (
            self.object.modules
                .filter(unlocked_groups__in=user_groups)
                .distinct()
        )
        return context

class ModuleDetailView(DetailView, LoginRequiredMixin):
    model = Module
    template_name ='module_detail.html'
    context_object_name = 'module'

    def get_queryset(self):
        user_groups = self.request.user.groups.all()
        return Module.objects.filter(
            Q(course__allowed_groups__in=user_groups,
            unlocked_groups__in=user_groups)
        ).distinct()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_groups = self.request.user.groups.all()
        context['contents'] = self.object.contents.filter(
            unlocked_groups__in=user_groups
        ).distinct()
        return context
        
class ContentDetailView(DetailView, LoginRequiredMixin):
    model = Content
    template_name ='content_detail.html'
    context_object_name = 'content'

    def get_queryset(self):
        return Content.objects.filter(module__pk=self.kwargs['module_pk'], module__course__slug=self.kwargs['course_slug'])

class StudentSignUpView(CreateView):
    form_class    = StudentSignUpForm
    template_name = "registration/signup.html"
    success_url   = reverse_lazy("login")