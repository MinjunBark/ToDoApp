from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list'),
    path('create/', views.task_create, name='task-create'),
    path('update/<int:pk>', views.task_update, name='task-update'),
    path('delete/<int:pk>/', views.task_delete, name='task-delete'),
    path('toggle/<int:pk>', views.task_toggle, name='task-toggle'),
]
