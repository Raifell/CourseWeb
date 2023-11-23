from django.urls import path
from . import views

urlpatterns = [
    path('create-module/', views.add_module_page, name='add_module_page'),
    path('edit-module/<str:module_name>/', views.edit_module_page, name='edit_module_page'),
    path('delete-module/<str:module_name>/', views.delete_module_page, name='delete_module_page'),
    path('<str:module_name>/', views.module_page, name='module_page'),
]
