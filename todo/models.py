from django.db import models

class Task(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  due_date = models.DateField()
  priority = models.CharField(max_length=255)

class CompletedTask(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  due_date = models.DateField()
  priority = models.CharField(max_length=255)