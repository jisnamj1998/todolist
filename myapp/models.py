from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoList(models.Model):
    title=models.CharField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=True)
    user_object=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.title