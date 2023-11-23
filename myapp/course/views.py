from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from module.models import *
from .forms import *


def main_page(request):
    courses = Course.objects.all()
    context = {
        'title': 'Main page',
        'courses': courses,
    }
    return render(request, 'course/index_main.html', context)


def course_page(request, course_name):
    course = get_object_or_404(Course, title=course_name)
    modules = Module.objects.filter(course__pk=course.pk)
    context = {
        'title': 'Course page',
        'course': course,
        'modules': modules,
    }
    return render(request, 'course/index_course.html', context)


def add_course_page(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')

    context = {
        'title': 'Add Course',
        'form': form,
    }
    return render(request, 'course/index_add_course.html', context)


def edit_course_page(request, course_name):
    course = get_object_or_404(Course, title=course_name)
    form = CourseForm(initial={'title': course.title,
                               'description': course.description,
                               'average': course.average})
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    context = {
        'title': 'Edit Course',
        'form': form,
    }
    return render(request, 'course/index_edit_course.html', context)


def delete_course_page(request, course_name):
    get_object_or_404(Course, title=course_name).delete()
    return redirect('main_page')
