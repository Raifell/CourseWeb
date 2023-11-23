from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'average')


admin.site.register(Course, CourseAdmin)
