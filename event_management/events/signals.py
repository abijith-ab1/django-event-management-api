# events/signals.py
from django.conf import settings
from django.db.models import Q
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Event

User = get_user_model()

@receiver(post_save, sender=Event)
def event_notification(sender, instance, created, **kwargs):
    subject = 'New Event Created' if created else 'Event Updated'
    message = f'Event: {instance.name}\nDescription: {instance.description}\nDate: {instance.date}'
    recipient_list = [user.email for user in User.objects.filter(Q(role='attendee') | Q(role='organizer'))]
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
