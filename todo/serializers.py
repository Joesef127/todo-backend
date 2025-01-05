from rest_framework import serializers
from todo.models import Task, CompletedTask

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'


class CompletedTaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = CompletedTask
    fields = '__all__'