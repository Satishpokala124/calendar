from typing import List

from Date import Date
from Event import Event


class Calendar:
    completed_events: List[Event] = []
    events: List[Event] = []

    def __init__(self, events):
        self.events = events
        self.sort_events_start_time()

    def sort_events_start_time(self) -> None:
        self.events.sort(key=lambda event: event.start_timestamp)
        self.completed_events.sort(key=lambda event: event.start_timestamp)

    def sort_events_end_time(self) -> None:
        self.events.sort(key=lambda event: event.end_timestamp)
        self.completed_events.sort(key=lambda event: event.end_timestamp)

    def add_event(self, event: Event) -> None:
        for i, ith_event in enumerate(self.events):
            if event.start_timestamp <= ith_event.start_timestamp:
                self.events.insert(i, event)
                break

    def mark_event_as_done(self):
        pass

    def schedule_meeting(self, other: 'Calendar', date: Date, duration: int):
        events1 = filter(
            lambda event: event.start_timestamp.date == date or event.end_timestamp.date == date,
            self.events
        )
        events2 = filter(
            lambda event: event.start_timestamp.date == date or event.end_timestamp.date == date,
            other.events
        )
        pass
