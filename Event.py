from TimeStamp import TimeStamp


class Event:
    start_timestamp = None
    end_timestamp = None

    def __init__(self, start_timestamp: TimeStamp, end_timestamp: TimeStamp) -> None:
        self.set_start_timestamp(start_timestamp)
        self.set_end_timestamp(end_timestamp)

    def validate(self):
        pass

    def set_start_timestamp(self, start_timestamp) -> None or TypeError:
        if not isinstance(start_timestamp, TimeStamp):
            raise TypeError
        self.start_timestamp = start_timestamp

    def set_end_timestamp(self, end_timestamp) -> None or TypeError:
        if not isinstance(end_timestamp, TimeStamp):
            raise TypeError
        self.end_timestamp = end_timestamp

    def no_of_hours(self) -> int:
        if self.start_timestamp.date == self.end_timestamp.date:
            return self.end_timestamp.time - self.start_timestamp.time
        else:
            pass

    def no_of_days(self) -> int:
        return self.end_timestamp.date - self.start_timestamp.date
