from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Course(models.Model):
    title = models.CharField('Title', max_length=255, unique=True)
    description = models.TextField('Description')
    average = models.PositiveIntegerField('Average', validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return self.title