from rest_framework import serializers
from .models import Room
from .models import Booking



class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        
        

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'