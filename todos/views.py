from todos.models import ToDo
from todos.serializers import ToDoSerializer
from rest_framework import generics


class ToDoList(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer