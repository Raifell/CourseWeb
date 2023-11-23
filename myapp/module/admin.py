from django.contrib import admin
from .models import *


class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'course', 'average')


admin.site.register(Module, ModuleAdmin)
