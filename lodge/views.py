from django.shortcuts import render, redirect
from .models import Room, Booking
from datetime import datetime
from django.contrib import messages
from .serealizers import RoomSerializers
from rest_framework .generics import ListAPIView,CreateAPIView
from rest_framework import status
from rest_framework .response import Response



def home_page(request):
    return render(request,'lodge/home.html')



class RoomCreateAPIView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




def add_room(request):
    if request.method == 'POST':
        room_number = request.POST['room_number']
        rent_price_per_hour = request.POST['rent_price_per_hour']

        # Create a new room object and save it to the database
        room = Room.objects.create(room_number=room_number, rent_price_per_hour=rent_price_per_hour)
        room.save()
        return redirect('room_list')
    return render(request, 'lodge/add_room.html')




def book_room(request):
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        start_time_str = request.POST.get('start_time')
        end_time_str = request.POST.get('end_time')

        try:
            start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M')
            end_time = datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M')

            room = Room.objects.get(room_number=room_number)

            if Booking.objects.filter(room=room, start_time__lte=end_time, end_time__gte=start_time).exists():
                messages.error(request, 'Room not available. Please choose another time slot.')
            else:
                booking = Booking.objects.create(room=room, start_time=start_time, end_time=end_time)
                total_rent_price = (end_time - start_time).seconds / 3600 * float(room.rent_price_per_hour)
                messages.success(request, f'Booked successfully. Total rent price: {total_rent_price:.2f}')

        except ValueError:
            messages.error(request, 'Invalid date format. Please use YYYY-MM-DDTHH:MM.')
    return render(request, 'lodge/book_room.html')


# def room_list(request):
#     rooms = Room.objects.all()
#     return render(request, 'lodge/room_list.html', {'rooms': rooms})

class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    lookup_field = 'room_number'