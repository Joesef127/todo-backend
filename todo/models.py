# models.py
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    due_date = models.DateField()
    priority = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CompletedTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='completed_tasks')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    due_date = models.DateField()
    priority = models.CharField(max_length=255)

    def __str__(self):
        return self.name
