from Date import Date
from Time import Time


class TimeStamp:
    date: Date = None
    time: Time = None

    def __init__(self, date: Date, time: Time):
        self.set_date(date)
        self.set_time(time)

    def set_date(self, date):
        if not isinstance(date, Date):
            return TypeError
        self.date = date

    def set_time(self, time):
        if not isinstance(time, Time):
            raise TypeError
        self.time = time

    def __str__(self):
        return f'{self.date}T{self.time}'

    def __eq__(self, other):
        if not isinstance(other, TimeStamp):
            raise TypeError
        return self.date == other.date and self.time == other.time

    def __lt__(self, other) -> bool:
        if not isinstance(other, TimeStamp):
            raise TypeError
        if self.date > other.date:
            return False
        elif self.date == other.date:
            return False if self.time >= other.time else True
        return True