from rest_framework import serializers
from django.contrib.auth.models import User
from todo.models import ToDoList


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['id', 'text', 'is_completed', 'created_at', 'updated_at']