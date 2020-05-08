from django.urls import path
from . import views

urlpatterns = [
    path('Hello/', views.Hello),
    path('',views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name='new-task'),
    path('edit/<int:id>', views.editTask, name='edit-task'),
    path('yourname/<str:name>', views.yourname, name='your-name'),
]
