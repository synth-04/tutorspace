from django.contrib import admin
from .models import Course, Module, Content, Resource

# Register your models here.

class ModuleInline(admin.StackedInline):
    model = Module

class ContentInline(admin.StackedInline):
    model = Content

class ResourceInline(admin.StackedInline):
    model = Resource

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline]
    filter_horizontal = ('allowed_groups',)

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [ContentInline]
    filter_horizontal = ('unlocked_groups',)

@admin.register(Content)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ResourceInline]

#admin.site.register(Course)
#admin.site.register(Module)
admin.site.register(Resource)

