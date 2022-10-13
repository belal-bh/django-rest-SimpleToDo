from rest_framework import serializers
from todos.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    # title = serializers.CharField()
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'updated_at']