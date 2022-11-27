from todo.models import ToDoList

class ToDoUtil:
    def __init__(self, user):
        self.user = user
    
    def get_user_todo(self):
        return self.user.user_todo_list.all().order_by('is_completed', '-created_at')
