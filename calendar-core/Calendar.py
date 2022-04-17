from typing import List

from Date import Date
from Event import Event
from Time import Time
from TimeStamp import TimeStamp


class Calendar:
    completed_events: List[Event] = []
    events: List[Event] = []

    def __init__(self, events: List[Event]):
        self.events = events
        self.sort_events_start_time()

    def sort_events_start_time(self) -> None:
        self.events.sort(key=lambda event: event.start_timestamp)
        self.completed_events.sort(key=lambda event: event.start_timestamp)

    def sort_events_end_time(self) -> None:
        self.events.sort(key=lambda event: event.end_timestamp)
        self.completed_events.sort(key=lambda event: event.end_timestamp)

    def add_event(self, event: Event) -> None:
        if not isinstance(event, Event):
            raise TypeError(f'Expected argument of type {type(Event)} but got {type(event)}')
        for i, ith_event in enumerate(self.events):
            if event.start_timestamp <= ith_event.start_timestamp:
                self.events.insert(i, event)
                return
        self.events.append(event)

    def mark_event_as_done(self, event):
        pass

    def schedule_meeting(self, other: 'Calendar', date: Date, duration: int) -> Event or int:
        def filter_fun(e):
            return e.start_timestamp.date == date or e.end_timestamp.date == date

        events1 = list(filter(filter_fun, self.events))
        events2 = list(filter(filter_fun, other.events))
        events1.sort(key=lambda e: e.start_timestamp)
        events2.sort(key=lambda e: e.start_timestamp)

        time_line = [Time(0, 0) + i * 15 for i in range(24 * 4)]
        empty_slot = 0
        for time in time_line:
            is_cal1_free = True
            is_cal2_free = True
            for event in events1:
                if event.start_timestamp.time <= time < event.end_timestamp.time:
                    is_cal1_free = False
                    break
            for event in events2:
                if event.start_timestamp.time <= time < event.end_timestamp.time:
                    is_cal2_free = False
                    break

            if duration <= empty_slot:
                start_timestamp = TimeStamp(date, time - duration)
                end_timestamp = TimeStamp(date, time)
                scheduled_event = Event(start_timestamp, end_timestamp)
                return scheduled_event

            if is_cal1_free and is_cal2_free:
                empty_slot += 15
            else:
                empty_slot = 0
        return -1
