from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, Event, Registration

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
        
        def create(self, validated_data):
            # Here you can add any custom user creation logic if needed
            user = User.objects.create_user(**validated_data)
            return user

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'date', 'organizer']

        def create(self, validated_data):
            # Ensure the organizer is provided from the request user
            return Event.objects.create(**validated_data)
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'event', 'user']

