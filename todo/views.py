from todo.models import Task
from todo.serializers import TaskSerializer
from django.http import JsonResponse

def tasks(request):
  data = Task.objects.all()
  serializer = TaskSerializer(data, many=True)
  return JsonResponse({'tasks': serializer.data})