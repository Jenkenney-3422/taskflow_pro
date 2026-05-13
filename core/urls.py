from django.contrib import admin
from django.urls import path
from tasks_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
]