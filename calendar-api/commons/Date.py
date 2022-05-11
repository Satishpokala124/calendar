from copy import copy


class Date:
    d: int = 0
    m: int = 0
    y: int = 0

    def __init__(self, day: int, month: int, year: int):
        self.month_days = None
        self.set_year(year)
        self.set_month_days()
        self.set_month(month)
        self.set_day(day)

    def __str__(self) -> str:
        d = str(self.d).rjust(2, '0')
        m = str(self.m).rjust(2, '0')
        y = str(self.y).rjust(4, '0')
        return f'{d}-{m}-{y}'

    def __eq__(self, other: 'Date') -> bool:
        if not isinstance(other, Date):
            raise TypeError(f'Expected argument of type {type(self)} but got {type(other)}')
        return self.d == other.d and self.m == other.m and self.y == other.y

    def __gt__(self, other: 'Date') -> bool:
        if not isinstance(other, Date):
            raise TypeError(f'Expected argument of type {type(self)} but got {type(other)}')
        if self.y > other.y:
            return True
        elif self.y == other.y:
            if self.m > other.m:
                return True
            elif self.m == other.m:
                if self.d > other.d:
                    return True
        return False

    def __ge__(self, other: 'Date') -> bool:
        if not isinstance(other, Date):
            raise TypeError(f'Expected argument of type {type(self)} but got {type(other)}')
        return self > other or self == other

    def __lt__(self, other: 'Date') -> bool:
        if not isinstance(other, Date):
            raise TypeError(f'Expected argument of type {type(self)} but got {type(other)}')
        return not self >= other

    def __le__(self, other: 'Date') -> bool:
        if not isinstance(other, Date):
            raise TypeError(f'Expected argument of type {type(self)} but got {type(other)}')
        return self < other or self == other

    def __add__(self, days: int):
        if not isinstance(days, int):
            raise TypeError(f'Expected argument of type {type(1)} but got {type(days)}')
        new_date = copy(self)
        while new_date.d + days > new_date.max_days_in_this_month():
            days -= (new_date.max_days_in_this_month() - new_date.d)
            new_date.d = 0
            new_date.m = new_date.get_next_month()
            new_date.y += 1 if new_date.m == 1 else 0
        new_date.d += days
        return new_date

    def __sub__(self, other: 'Date'):
        if isinstance(other, int):
            new_date = copy(self)
            while new_date.d - other < 1:
                other -= new_date.d
                new_date.m = new_date.previous_month()
                new_date.y -= 1 if new_date.m == 12 else 0
                new_date.d = new_date.max_days_in_this_month()
            new_date.d -= other
            return new_date
        elif isinstance(other, Date):
            smaller_day, bigger_day = [self, other] if self < other else [other, self]
            if self.y == other.y:
                return bigger_day.days_from_year_start() - smaller_day.days_from_year_start()
            days_between_years = sum(
                [Date(1, 1, i).days_in_this_year() for i in range(smaller_day.y + 1, bigger_day.y)])
            return (
                    smaller_day.days_remaining_in_this_year() +
                    days_between_years +
                    bigger_day.days_from_year_start()
                )
        else:
            raise TypeError(f'Expected argument of type {type(self)} or {type(1)} but got {type(other)}')

    def is_leap_year(self) -> bool:
        year = self.y
        if (not (year % 4) and year % 100) or (not (year % 400)):
            return True
        return False

    def max_days_in_this_month(self) -> int:
        return self.month_days[self.m - 1]

    def get_day(self) -> int:
        return self.d

    def get_month(self) -> int:
        return self.m

    def get_next_month(self) -> int:
        return self.m + 1 if self.m < 12 else 1

    def get_year(self) -> int:
        return self.y

    def set_day(self, day: int):
        if not isinstance(day, int):
            raise TypeError(f'Expected argument of type {type(1)} but got {type(day)}')
        if not 1 <= day <= self.max_days_in_this_month():
            raise AttributeError(f'Argument "day" is out of the expected range {1} to {self.max_days_in_this_month()}.')
        self.d = day

    def set_month(self, month: int):
        if not isinstance(month, int):
            raise TypeError(f'Expected argument of type {type(1)} but got {type(month)}')
        if not 1 <= month <= 12:
            raise AttributeError(f'Argument "month" is out of the expected range 1 to 12.')
        self.m = month

    def set_year(self, year: int) -> None:
        if not isinstance(year, int):
            raise TypeError(f'Expected argument of type {type(1)} but got {type(year)}')
        self.y = year

    def set_month_days(self):
        self.month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year():
            self.month_days[1] = 29

    def previous_month(self):
        return 12 if self.m == 1 else self.m - 1

    def first_day_of_the_year(self):
        return Date(1, 1, self.y)

    def days_from_year_start(self) -> int:
        return sum(self.month_days[:self.m - 1]) + self.d

    def days_in_this_year(self):
        return 366 if self.is_leap_year() else 365

    def days_remaining_in_this_year(self):
        return self.days_in_this_year() - self.days_from_year_start()
