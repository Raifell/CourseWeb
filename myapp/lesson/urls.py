from django.urls import path
from . import views

urlpatterns = [
    path('create-lesson/', views.add_lesson_page, name='add_lesson_page'),
    path('edit-lesson/<slug:lesson_slug>/', views.edit_lesson_page, name='edit_lesson_page'),
    path('delete-lesson/<slug:lesson_slug>/', views.delete_lesson_page, name='delete_lesson_page'),
    path('<slug:lesson_slug>/', views.lesson_page, name='lesson_page'),
]
