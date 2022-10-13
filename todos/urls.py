from django.urls import path
from todos.views import ToDoList, ToDoDetail, ToDoViewset

app_name = 'todos'
urlpatterns = [
    # path('', ToDoList.as_view()),
    # path('<int:pk>/', ToDoDetail.as_view()),
    path('', ToDoViewset.as_view())
]