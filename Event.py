from TimeStamp import TimeStamp
from Time import Time


class Event:
    start_timestamp: TimeStamp = None
    end_timestamp: TimeStamp = None

    def __init__(self, start_timestamp: TimeStamp, end_timestamp: TimeStamp) -> None:
        self.set_start_timestamp(start_timestamp)
        self.set_end_timestamp(end_timestamp)
        self.validate()

    def validate(self):
        if self.start_timestamp < self.end_timestamp:
            raise AttributeError('start_timestamp is expected to be before end_timestamp')

    def set_start_timestamp(self, start_timestamp: TimeStamp) -> None:
        if not isinstance(start_timestamp, TimeStamp):
            raise TypeError(f'Expected start_timestamp of type {type(TimeStamp)} but got {type(self.start_timestamp)}')
        self.start_timestamp = start_timestamp

    def set_end_timestamp(self, end_timestamp: TimeStamp) -> None:
        if not isinstance(end_timestamp, TimeStamp):
            raise TypeError(f'Expected end_timestamp of type {type(TimeStamp)} but got {type(self.end_timestamp)}')
        self.end_timestamp = end_timestamp

    def no_of_hours(self) -> int:
        if self.start_timestamp.date == self.end_timestamp.date:
            return self.end_timestamp.time - self.start_timestamp.time
        hours_remaining_in_start_day = Time(23, 59) - self.start_timestamp.time
        hours_for_each_day_in_between = 24 * (self.end_timestamp.date - self.start_timestamp.date)
        hours_done_in_end_day = self.end_timestamp.time - Time(0, 0)
        return round(hours_remaining_in_start_day + hours_for_each_day_in_between + hours_done_in_end_day)

    def no_of_days(self) -> int:
        return self.end_timestamp.date - self.start_timestamp.date
