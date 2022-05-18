from django.db import models

from account.models import User
from commons.core.Time import Time
from commons.core.TimeStamp import TimeStamp


class EventManager(models.Manager):
    def create_event(self, host_id: int, start_timestamp: str, end_timestamp: str, name: str = 'Event',
                     description: str = 'NA', completed: bool = False, cancelled: bool = False):
        if not User.objects.filter(id=host_id).exists():
            raise AttributeError(f'User with the specified id: {host_id} does not exist.')
        start_timestamp = TimeStamp.make(start_timestamp)
        end_timestamp = TimeStamp.make(end_timestamp)
        if not start_timestamp < end_timestamp:
            raise AttributeError('start_timestamp is expected to be before end_timestamp')
        host = User.objects.get(id=host_id)
        self.create(
            host=host,
            start_timestamp=f'{start_timestamp}+00:00',
            end_timestamp=f'{end_timestamp}+00:00',
            name=name,
            description=description,
            completed=completed,
            cancelled=cancelled
        )


class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    start_timestamp = models.DateTimeField(null=False, blank=False)
    end_timestamp = models.DateTimeField(null=False, blank=False)
    name = models.TextField(max_length=100, default='Event')
    description = models.TextField(max_length=500, default='NA')
    completed = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)

    # Connecting the custom Manager
    objects = EventManager()

    def validate(self):
        start_timestamp = TimeStamp.make(self.start_timestamp.strftime('%Y-%m-%dT%H:%M'))
        end_timestamp = TimeStamp.make(self.end_timestamp.strftime('%Y-%m-%dT%H:%M'))
        if start_timestamp > end_timestamp:
            raise AttributeError('start_timestamp is expected to be before end_timestamp')

    def set_start_timestamp(self, start_timestamp: TimeStamp) -> None:
        if not isinstance(start_timestamp, TimeStamp):
            raise TypeError(f'Expected start_timestamp of type {type(TimeStamp)} but got {type(start_timestamp)}')
        self.start_timestamp = f'{start_timestamp}'

    def set_end_timestamp(self, end_timestamp: TimeStamp) -> None:
        if not isinstance(end_timestamp, TimeStamp):
            raise TypeError(f'Expected end_timestamp of type {type(TimeStamp)} but got {type(end_timestamp)}')
        self.end_timestamp = f'{end_timestamp}'

    def no_of_hours(self) -> int:
        start_timestamp = TimeStamp.make(self.start_timestamp.strftime('%Y-%m-%dT%H:%M'))
        end_timestamp = TimeStamp.make(self.end_timestamp.strftime('%Y-%m-%dT%H:%M'))
        if start_timestamp.date == end_timestamp.date:
            return end_timestamp.time - start_timestamp.time
        hours_remaining_in_start_day = Time(23, 59) - start_timestamp.time
        hours_for_each_day_in_between = 24 * (end_timestamp.date - start_timestamp.date)
        hours_done_in_end_day = end_timestamp.time - Time(0, 0)
        return round(hours_remaining_in_start_day + hours_for_each_day_in_between + hours_done_in_end_day)

    def no_of_days(self) -> int:
        start_timestamp = TimeStamp.make(self.start_timestamp.strftime('%Y-%m-%dT%H:%M'))
        end_timestamp = TimeStamp.make(self.end_timestamp.strftime('%Y-%m-%dT%H:%M'))
        return end_timestamp.date - start_timestamp.date
