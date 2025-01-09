from rest_framework import serializers
from todo.models import Task, CompletedTask
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'


class CompletedTaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = CompletedTask
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data["username"],
      email=validated_data["email"],
      # firstname=validated_data["firstname"],
      # lastname=validated_data["lastname"],
    )

    user.set_password(validated_data["password"])
    user.save()
    return user