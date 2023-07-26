from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=20, unique=True)
    rent_price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.room_number

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.room.room_number} - {self.start_time} to {self.end_time}"
