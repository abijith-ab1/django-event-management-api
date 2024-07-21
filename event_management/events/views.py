from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Event, Registration
from .serializers import UserSerializer, EventSerializer, RegistrationSerializer
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.select_related('organizer').all()
    serializer_class = EventSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        # user = self.request.user
        # if not user.is_authenticated:
        #     raise PermissionDenied("User is not authenticated")
        event = serializer.save()
        self.send_event_notification(event, created=True)

    def perform_update(self, serializer):
        event = serializer.save()
        self.send_event_notification(event, created=False)

    def send_event_notification(self, event, created):
        subject = 'New Event Created' if created else 'Event Updated'
        message = f'Event: {event.name}\nDescription: {event.description}\nDate: {event.date}'
        recipient_list = [user.email for user in User.objects.filter(Q(role='attendee') | Q(role='organizer'))]
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.select_related('organizer').all()
    serializer_class = EventSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

class RegistrationListCreateView(generics.ListCreateAPIView):
    queryset = Registration.objects.select_related('event', 'user').all()
    serializer_class = RegistrationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

class RegistrationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.select_related('event', 'user').all()
    serializer_class = RegistrationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

class UserReportView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        user_data = [{'username': user.username, 'role': user.role} for user in users]
        return Response(user_data)

class EventReportView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        events = Event.objects.select_related('organizer').all()
        event_data = [{'name': event.name, 'organizer': event.organizer.username} for event in events]
        return Response(event_data)

class CountView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        event_count = Event.objects.count()
        registration_count = Registration.objects.count()
        return Response({'event_count': event_count, 'registration_count': registration_count})
