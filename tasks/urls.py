from django.urls import path
from . import views

urlpatterns = [
    path('Hello/', views.Hello),
    path('',views.taskList, name='task-list'),
    path('yourname/<str:name>', views.yourname, name='your-name'),
]
