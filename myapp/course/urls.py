from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('course/<str:course_name>/', views.course_page, name='course_page'),
    path('create-course/', views.add_course_page, name='add_course_page'),
    path('edit-course/<str:course_name>/', views.edit_course_page, name='edit_course_page'),
    path('delete-course/<str:course_name>/', views.delete_course_page, name='delete_course_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
