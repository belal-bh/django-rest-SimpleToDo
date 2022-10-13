from django.contrib.auth import get_user_model
from rest_framework import viewsets

from todos.models import ToDo
from todos.serializers import ToDoSerializer

from todos.utils import get_or_create_user, get_user_or_none

User = get_user_model()

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