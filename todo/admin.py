from django.contrib import admin
from todo.models import ToDoList
# Register your models here.

class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'user', 'is_completed', 'created_at', 'updated_at']
    list_filter = ['user', 'is_completed']

admin.site.register(ToDoList, ToDoListAdmin)