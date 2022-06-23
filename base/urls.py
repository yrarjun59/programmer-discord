from django.urls import path
from . import views

urlpatterns = [
    path("login", views.loginPage, name="login"),
    path("logout", views.LogoutUser, name="logout"),
    path("register", views.registerPage, name="register"),

    path("", views.home, name="home"),
    path("room/<str:pk>", views.room, name="room"),
    path('profile/<str:pk>', views.userProfile, name="user_profile"),
    path('update-user', views.UpdateUser, name="update-user"),

    path('topics', views.topicPage, name="topics"),
    path('activities', views.activityPage, name="activities"),


    path("create_room", views.CreateRoom, name="create_room"),
    path("update_room/<str:pk>", views.UpdateRoom, name="update_room"),
    path("delete_room/<str:pk>", views.DeleteRoom, name="delete_room"),
    path("delete_message/<str:pk>", views.DeleteMessage, name="delete_message"),
]
