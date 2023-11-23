from django import forms
from .models import *


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'average')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
        labels = {
            'title': 'Название курса',
            'description': 'Описание курса',
            'average': 'Часы освоения'
        }
