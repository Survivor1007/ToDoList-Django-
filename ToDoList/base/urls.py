
from django.urls import path
from .views import TaskList, DetailList,CreateList,UpdateList,TaskDelete,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(), name= "login" ),
    path('logout/', LogoutView.as_view(next_page= "login"), name = "logout"),
    path('register/',RegisterPage.as_view(),name = 'register'),


    path('', TaskList.as_view(), name = "tasks"),
    path('task/<int:pk>', DetailList.as_view(), name = "details"),
    path('create-task/', CreateList.as_view(), name = "create-task"),
    path('update-task/<int:pk>', UpdateList.as_view(), name = "update-task"),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name = "delete-task"),

]
