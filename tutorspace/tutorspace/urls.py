"""
URL configuration for tutorspace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from courses import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [

    path('', views.index, name="index"),

    # Admin

    path('admin/', 
         admin.site.urls),

    # User
    
    path('login/',
        auth_views.LoginView.as_view(),
        name='login'),
    
    path('logout/',
        auth_views.LogoutView.as_view(next_page='index'),
        name='logout'),
    
    path(
    'accounts/profile/',
    TemplateView.as_view(template_name='accounts/profile.html'),
    name='user_profile'),

    # Courses

    path('courses/', 
         views.CourseListView.as_view(), 
         name='course_list'
         ),
    
    path('courses/<slug:slug>/', 
         views.CourseDetailView.as_view(), 
         name='course_detail'
         ),

    # Modules

    path('courses/<slug:course_slug>/modules/<int:pk>/', 
         views.ModuleDetailView.as_view(), 
         name='module_detail'
        ),
    
    # Contents
    
    path('courses/<slug:course_slug>/modules/<int:module_pk>/content/<int:pk>/',
        views.ContentDetailView.as_view(),
        name='content_detail'
        ),

    
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
