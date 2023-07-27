from django.urls import path
from . views import *

urlpatterns = [
    path('',home_page, name='home_page'),
    path('api/add_room/',RoomCreateAPIView.as_view(), name='add_room'),
    path('api/book_room/',BookingCreateAPIView.as_view(), name='book_room'),
    path('api/room_list/',RoomListAPIView.as_view(), name='room_list'),
]