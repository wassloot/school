from rest_framework import serializers
from .models import Room, Booking, User, Resource


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        overlapping = Booking.objects.filter(
            room=data['room'],
            start_time__It=data['end_time'],
            end_time__gt=data['start_time'],
        )
        if overlapping.exists():
            raise serializers.ValidationError("Room is already taken for this time")
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']