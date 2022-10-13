from rest_framework import serializers
from django.contrib.auth import get_user_model
from todos.models import ToDo
from todos.utils import get_or_create_user, get_user_or_none

User = get_user_model()

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'updated_at']
    
    def _get_userid(self):
        request = self.context.get('request', None)
        if not request:
            return None
        username = request.headers.get('Userid', None)
        return username

    def create(self, validated_data):
        username = self._get_userid()
        user, created = get_or_create_user(username)
        if not user:
            raise serializers.ValidationError("Invalid User credentials")
        validated_data['user'] = user
        return super().create(validated_data)