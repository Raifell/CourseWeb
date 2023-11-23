from django import forms
from .models import *


class CreateLesson(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('title', 'content', 'module', 'duration')
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
        labels = {
            'title': 'Название урока',
            'content': 'Информация урока',
            'module': 'Для какого модуля',
            'duration': 'Кол-во часов (от 1 до 4)'
        }
