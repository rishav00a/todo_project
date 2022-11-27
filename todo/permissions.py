
from rest_framework import permissions
from todo.models import ToDoList
class ToDoPermission(permissions.BasePermission):

    def __init__(self, allowed_methods):
        super().__init__()
        self.allowed_methods = allowed_methods

    def has_permission(self, request, view):
        if request.method in self.allowed_methods:
            return True
            
        id = request.data.get("id")
        if id:
            return (ToDoList.objects.get(id=id).user == request.user)
        return False