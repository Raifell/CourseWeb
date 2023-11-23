from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def module_page(request, module_name):
    module = get_object_or_404(Module, title=module_name)
    context = {
        'title': 'Module page',
        'module': module
    }
    return render(request, 'module/index_module.html', context)


def add_module_page(request):
    form = CreateModule()
    if request.method == 'POST':
        form = CreateModule(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')

    context = {
        'title': 'Add Module',
        'form': form,
    }
    return render(request, 'module/index_add_module.html', context)


def edit_module_page(request, module_name):
    module = get_object_or_404(Module, title=module_name)
    form = CreateModule(initial={
        'title': module.title,
        'description': module.description,
        'course': module.course.pk,
        'average': module.average
    })
    if request.method == 'POST':
        form = CreateModule(request.POST or None, instance=module)
        if form.is_valid():
            form.save()
            return redirect('course_page', module.course.title)

    context = {
        'title': 'Edit Module',
        'form': form,
    }
    return render(request, 'module/index_edit_module.html', context)


def delete_module_page(request, module_name):
    target = get_object_or_404(Module, title=module_name)
    course_name = target.course.title
    target.delete()
    return redirect('course_page', course_name)
