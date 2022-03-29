from django.shortcuts import render
from .serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo


@api_view(['GET'])
def Getall(request):
    allTasks = Todo.objects.all()
    serializer_class = TodoSerializer(allTasks, many=True)
    return Response(serializer_class.data)


@api_view(['POST'])
def Additem(request):
    title = request.data.get('title')
    description = request.data.get('description')
    if title is not None and description is not None:
        todoItem = Todo()
        todoItem.Task = title
        todoItem.Description = description
        Todo.save(todoItem)
        return Response(status=200,data="Done")
    return Response(status=500,data="Error happened")


@api_view(['PATCH'])
def Updatecompleted(request):
    taskId = request.data.get('id')
    if taskId is not None:
        changeStatusTask = Todo.objects.get(id=taskId)
        changeStatusTask.Completed = not changeStatusTask.Completed
        Todo.save(changeStatusTask)
        return Response(status=200,data="Updated")
    return Response(status=500,data="Error hapened try again ltr")


@api_view(['DELETE'])
def Deletetask(request):
    taskId = request.data.get('id')
    if taskId is not None:
        deletedTask=Todo.objects.get(id=taskId)
        deletedTask.delete()
        return Response(status=200,data="Deleted successfully")
    return Response(status=500,data="Error Happened try again Later")
