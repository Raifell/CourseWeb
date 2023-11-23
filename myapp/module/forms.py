from django import forms
from .models import *


class CreateModule(forms.ModelForm):
    class Meta:
        model = Module
        fields = ('title', 'description', 'course', 'average')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
        labels = {
            'title': 'Название модуля',
            'description': 'Описание модуля',
            'course': 'Для какого курса',
            'average': 'Часы освоения'
        }
