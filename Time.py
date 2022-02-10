from copy import copy


class Time:
    hour: int = 0
    minute: int = 0

    def __init__(self, h, m) -> None:
        self.set_hour(h)
        self.set_minute(m)

    def set_hour(self, h):
        if not 0 <= h < 24:
            raise AttributeError('Argument "h" is out of the expected range 0 to 23')
        self.hour = int(h)

    def set_minute(self, m):
        if not 0 <= m < 60:
            raise AttributeError('Argument "m" is out of the expected range 0 to 59')
        self.minute = int(m)

    def __str__(self):
        return f'{str(self.hour).rjust(2, "0")}:{str(self.minute).rjust(2, "0")}'

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __lt__(self, other):
        if not isinstance(other, Time):
            raise TypeError(f'Expected argument of type {type(Time)} but got {type(other)}')
        if self.hour > other.hour:
            return False
        if self.hour == other.hour:
            return self.minute < other.minute
        return True

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __sub__(self, other):
        if not isinstance(other, Time):
            raise TypeError
        small_ts, big_ts = [self, other] if self < other else [other, self]
        hr_diff = big_ts.hour - small_ts.hour
        min_diff = big_ts.minute - small_ts.minute
        return hr_diff + (min_diff / 60)

    def __add__(self, minutes: int):
        if not isinstance(minutes, int):
            raise TypeError(f'Expected argument of type {type(int)} but got {type(minutes)}')
        if self.minute + minutes < 60:
            return Time(self.hour, self.minute + minutes)
        new_time = copy(self)
        while new_time.minute + minutes >= 60:
            new_time.hour += 1
            minutes -= 60
        new_time.minute += minutes
        return new_time
