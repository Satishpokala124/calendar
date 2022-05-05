from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User


@receiver(post_save, sender=User, dispatch_uid='create_calendar')
def create_calendar(sender, instance, created, **kwargs):
    if created:
        # call create_calendar() to make a calendar for the user.
        print(f'create_calendar({sender}, {instance}, {created}, {kwargs}) called')
