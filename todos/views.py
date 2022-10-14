from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todos.models import ToDo
from todos.serializers import ToDoSerializer, UserSerializer

from todos.utils import get_or_create_user, get_user_or_none, get_normalized_username, generate_email_from_username

User = get_user_model()

@api_view(['POST'])
def login_or_register(request):
    username = request.data.get('username', '')
    username = get_normalized_username(username)
    if not username:
        return Response({"message": "Invalid"}, status=400)
    
    email = generate_email_from_username(username)
    user = None

    try:
        user = User.objects.get(username=username)
    except:
        pass

    if not user:
        user_serialiser = UserSerializer(data={'username': username, 'email': email})
    else:
        user_serialiser = UserSerializer(user)

    if not user and user_serialiser.is_valid():
        user = user_serialiser.save()
        return Response(user_serialiser.data, status=200)

    if user:
        return Response(user_serialiser.data, status=200)

    return Response({"message": "Invalid"}, status=400)



class ToDoViewset(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer

    def _get_user_or_none(self):
        username = self.request.headers.get('userid', None)
        return get_user_or_none(username)

    def get_queryset(self):
        username = self.request.headers.get('userid', None)
        # handle bad header request
        if not username:
            return ToDo.objects.none()

        # get the user
        user = self._get_user_or_none()
        if not user:
            user, created = get_or_create_user(username)
        print(user)

        return user.todos.all()
    
    def list(self, request):
        return super().list(request)

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass