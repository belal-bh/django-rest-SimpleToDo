from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todos.models import ToDo
from todos.serializers import ToDoSerializer, UserSerializer

from todos.utils import get_user_or_none, get_normalized_username, generate_email_from_username

User = get_user_model()

@api_view(['POST'])
def login_or_register(request):
    username = request.data.get('username', '')
    username = get_normalized_username(username)
    if not username:
        return Response({"message": "Invalid"}, status=status.HTTP_400_BAD_REQUEST)
    
    email = generate_email_from_username(username)

    user = User.objects.filter(username=username).first()
    
    if not user:
        user_serialiser = UserSerializer(data={'username': username, 'email': email})
    else:
        user_serialiser = UserSerializer(user)

    if not user and user_serialiser.is_valid():
        user = user_serialiser.save()
        return Response(user_serialiser.data, status=status.HTTP_201_CREATED)

    if user:
        return Response(user_serialiser.data, status=status.HTTP_200_OK)

    return Response({"message": "Invalid"}, status=status.HTTP_400_BAD_REQUEST)



class ToDoViewset(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer

    def get_queryset(self):
        userid = self.request.headers.get('userid', None)
        try:
            userid = int(userid)
        except:
            pass

        # print(type(userid), isinstance(userid, int))
        # handle bad header request
        if not isinstance(userid, int):
            return ToDo.objects.none()

        # get the user
        user = User.objects.filter(id=userid).first()
        if not user:
            return ToDo.objects.none()
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