from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from todo.serializers import ToDoListSerializer
from todo.utils import ToDoUtil
from todo.models import ToDoList
from todo.permissions import ToDoPermission
from functools import partial


# Create your views here.
def index_view(request):
    return render(request, 'todo/index.html')



class ToDoView(APIView):
    permission_classes = (partial(ToDoPermission, ['GET','POST']),)
    def get(self, request):
        todo_data = ToDoListSerializer(ToDoUtil(request.user).get_user_todo(),many=True).data
        return Response(todo_data)

    def post(self, request, *args, **kwargs):
        data = request.data
        ToDoList.objects.create(text=data.get("text"), user=request.user)
        return Response({"data":"Item created successfully"})

    def patch(self, request, *args, **kwargs):
        data = request.data
        print(data.get("id"))
        qs = ToDoList.objects.get(id=data.get("id"), user=request.user)
        serializer = ToDoListSerializer(qs, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        data = request.data
        qs = ToDoList.objects.get(id=data.get("id"), user=request.user)
        qs.delete()
        return Response({"data":"Item deleted successfully"})




