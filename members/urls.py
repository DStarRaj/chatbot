from django.urls import path
from . import views

urlpatterns = [
    path('members', views.members, name='members'),
    path('send', views.send, name='send'),
    path('getMessages', views.getMessages, name='getMessages'),
]