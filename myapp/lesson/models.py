from django.db import models
from django.utils.text import slugify

from module.models import *


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    title = models.CharField('Title', max_length=255)
    content = models.TextField('Content')
    duration = models.PositiveIntegerField('Duration', validators=[MinValueValidator(1), MaxValueValidator(4)])
    slug = models.SlugField('Slug', max_length=255, unique=True, blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify('{}-{}'.format(self.module, self.title))
        super(Lesson, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title
