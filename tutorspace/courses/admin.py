from django.contrib import admin
from .models import Course, Module, Content, Resource

# Register your models here.

class ModuleInline(admin.StackedInline):
    model = Module
    filter_horizontal = ('unlocked_groups',)

class ContentInline(admin.StackedInline):
    model = Content
    filter_horizontal = ('unlocked_groups',)

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
    filter_horizontal = ('unlocked_groups',)

admin.site.register(Resource)

