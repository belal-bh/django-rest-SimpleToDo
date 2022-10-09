from django.db import models


class ToDo(models.Model):
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