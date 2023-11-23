from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


def lesson_page(request, lesson_slug):
    lesson = get_object_or_404(Lesson, slug=lesson_slug)
    context = {
        'title': 'Lesson page',
        'lesson': lesson,
    }
    return render(request, 'lesson/index_lesson.html', context)


def add_lesson_page(request):
    form = CreateLesson()
    if request.method == 'POST':
        form = CreateLesson(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')

    context = {
        'title': 'Add Lesson',
        'form': form,
    }
    return render(request, 'module/index_add_module.html', context)


def edit_lesson_page(request, lesson_slug):
    lesson = get_object_or_404(Lesson, slug=lesson_slug)
    form = CreateLesson(initial={
        'title': lesson.title,
        'content': lesson.content,
        'module': lesson.module.pk,
        'duration': lesson.duration
    })
    if request.method == 'POST':
        form = CreateLesson(request.POST or None, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('module_page', lesson.module.title)

    context = {
        'title': 'Edit Lesson',
        'form': form,
    }
    return render(request, 'module/index_edit_module.html', context)


def delete_lesson_page(request, lesson_slug):
    target = get_object_or_404(Lesson, slug=lesson_slug)
    module_name = target.module.title
    target.delete()
    return redirect('module_page', module_name)

