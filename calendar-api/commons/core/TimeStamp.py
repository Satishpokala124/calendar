from commons.core.Date import Date
from commons.core.Time import Time


class TimeStamp:
    date: Date = None
    time: Time = None

    def __init__(self, date: Date, time: Time):
        self.set_date(date)
        self.set_time(time)

    def set_date(self, date: Date):
        if not isinstance(date, Date):
            return TypeError
        self.date = date

    def set_time(self, time: Time):
        if not isinstance(time, Time):
            raise TypeError
        self.time = time

    def __str__(self):
        return f'{self.date}T{self.time}'

    def __eq__(self, other: 'TimeStamp'):
        if not isinstance(other, TimeStamp):
            raise TypeError
        return self.date == other.date and self.time == other.time

    def __lt__(self, other: 'TimeStamp') -> bool:
        if not isinstance(other, TimeStamp):
            raise TypeError
        if self.date > other.date:
            return False
        elif self.date == other.date:
            return False if self.time >= other.time else True
        return True

    def __le__(self, other: 'TimeStamp'):
        return self < other or self == other

    def __gt__(self, other: 'TimeStamp'):
        return not self <= other

    def __ge__(self, other: 'TimeStamp'):
        return not self < other

    @staticmethod
    def make(timestamp: str) -> 'TimeStamp':
        if not isinstance(timestamp, str):
            raise TypeError(f'Expected argument of type {type(str)} but got {type(timestamp)}')
        if len(timestamp) != 16:
            raise AttributeError('Malformed argument "timestamp"')
        date, time = timestamp.split('T')
        date = Date.make(date)
        time = Time.make(time)
        return TimeStamp(date, time)
