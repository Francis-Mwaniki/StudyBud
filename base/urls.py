from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('user_profile/<str:pk>/',views.userProfile,name='user-profile'),
     path('update_user/',views.updateUser,name='update-user'),
    path('create_room',views.createRoom, name='create-room'),
    path('update_room/<str:pk>/',views.updateRoom, name='update-room'),
    path('delete_room/<str:pk>/',views.deleteRoom, name='delete-room'),
    path('delete_message/<str:pk>/',views.deleteMessage, name='delete-message'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('topics/',views.topicsPage,name='topics'),
    path('activity/',views.activitiesPage,name='activity'),
] 