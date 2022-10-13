from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets

from todos.models import ToDo
from todos.serializers import ToDoSerializer

from todos.utils import get_or_create_user, get_user_or_none

User = get_user_model()

class ToDoViewset(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer

    def get_queryset(self):
        username = self.request.META.get('User-Name', None)

        # handle bad header request
        if not username:
            return ToDo.objects.none()

        # get the user
        user, created = get_or_create_user(username)

        return user.todos.all()


class ToDoList(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer