from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', views.tasks, name="tasks"),
    path('api/tasks/<int:id>', views.task, name='task'),
    path('api/completed-tasks/', views.completedTasks, name='completed-tasks')
]
