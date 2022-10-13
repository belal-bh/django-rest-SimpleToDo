from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ToDo(models.Model):
    user =  models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "todo"
        verbose_name_plural = "todos"

    def __str__(self):
        return self.title