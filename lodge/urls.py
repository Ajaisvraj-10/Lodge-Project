from django.urls import path
from . views import *

urlpatterns = [
    path('',home_page, name='home_page'),
    path('add_room/',add_room, name='add_room'),
    path('book_room/',book_room, name='book_room'),
    path('room_list/',room_list, name='room_list'),
]