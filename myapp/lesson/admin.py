from django.contrib import admin
from .models import *


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'module', 'duration')


admin.site.register(Lesson, LessonAdmin)
