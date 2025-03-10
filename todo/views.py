from todo.models import Task, CompletedTask
from todo.serializers import TaskSerializer, CompletedTaskSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['GET', 'POST',])
#@permission_classes([IsAuthenticated])
def tasks(request):
  if request.method == 'GET':
    data = Task.objects.filter(user=request.user)
    serializer = TaskSerializer(data, many=True)
    return Response({'tasks': serializer.data})
  
  elif request.method == 'POST':
    serializer = TaskSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response({'task': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE',])
#@permission_classes([IsAuthenticated])
def task(request, id):
  try:
    data = Task.objects.get(pk=id)
  except Task.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = TaskSerializer(data)
    return Response({'task': serializer.data})
  
  elif request.method == 'POST':
    serializer = TaskSerializer(data, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'task': serializer.data}, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  else:
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
  

@api_view(['GET', 'POST', 'DELETE',])
#@permission_classes([IsAuthenticated])
def completedTasks(request):
    if request.method == 'GET':
        data = CompletedTask.objects.filter(user=request.user)
        serializer = CompletedTaskSerializer(data, many=True)
        return Response({'completed_tasks': serializer.data})
    
    elif request.method == 'POST':
        try:
            task = Task.objects.get(pk=request.data['id'], user=request.user)
            serializer = CompletedTaskSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(user=request.user)
                task.delete()
                return Response({'completed_task': serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        completed_tasks = CompletedTask.objects.filter(user=request.user)
        completed_tasks.delete()
        return Response({'message': 'All completed tasks have been deleted.'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def register(request):
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    tokens = {
      'refresh': str(refresh),
      'access': str(refresh.access_token)
    }
    return Response(tokens, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

