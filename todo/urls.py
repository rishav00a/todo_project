from django.conf.urls import url
from django.urls import path, include
from todo.views import index_view, ToDoView


urlpatterns = [
    path('api/todo_data', ToDoView.as_view()),
    path('', index_view),
    
]

