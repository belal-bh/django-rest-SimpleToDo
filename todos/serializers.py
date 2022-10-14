from rest_framework import serializers
from django.contrib.auth import get_user_model
from todos.models import ToDo

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=40, allow_blank=False, trim_whitespace=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email']
    
    def create(self, validated_data):
        return super().create(validated_data)



class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'updated_at']
    
    def _get_userid(self):
        request = self.context.get('request', None)
        if not request:
            return None
        userid = request.headers.get('Userid', None)
        try:
            userid = int(userid)
        except:
            return None
        return userid

    def create(self, validated_data):
        userid = self._get_userid()
        user = User.objects.filter(id=userid).first()
        if not user:
            raise serializers.ValidationError({'name': "Invalid User credentials."})
        validated_data['user'] = user
        return super().create(validated_data)