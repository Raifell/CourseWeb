from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from course.models import Course


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    title = models.CharField('Title', max_length=255, unique=True)
    description = models.TextField('Description')
    average = models.PositiveIntegerField('Average', validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return self.title
