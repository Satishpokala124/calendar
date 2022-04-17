from copy import copy


class Date:
    d: int = 0
    m: int = 0
    y: int = 0

    def __init__(self, day: int, month: int, year: int):
        self.month_days = None
        self.setYear(year)
        self.setMonthDays()
        self.setMonth(month)
        self.setDay(day)

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
        while new_date.d + days > new_date.maxDaysInThisMonth():
            days -= (new_date.maxDaysInThisMonth() - new_date.d)
            new_date.d = 0
            new_date.m = new_date.getNextMonth()
            new_date.y += 1 if new_date.m == 1 else 0
        new_date.d += days
        return new_date

    def __sub__(self, other: 'Date'):
        if isinstance(other, int):
            new_date = copy(self)
            while new_date.d - other < 1:
                other -= new_date.d
                new_date.m = new_date.previousMonth()
                new_date.y -= 1 if new_date.m == 12 else 0
                new_date.d = new_date.maxDaysInThisMonth()
            new_date.d -= other
            return new_date
        elif isinstance(other, Date):
            smaller_day, bigger_day = [self, other] if self < other else [other, self]
            if self.y == other.y:
                return bigger_day.numberOfDaysFromYearStart() - smaller_day.numberOfDaysFromYearStart()
            days_between_years = sum(
                [Date(1, 1, i).numberOfDaysInThisYear() for i in range(smaller_day.y + 1, bigger_day.y)])
            return (
                    smaller_day.numberOfDaysRemainingInThisYear() +
                    days_between_years +
                    bigger_day.numberOfDaysFromYearStart()
                )
        else:
            raise TypeError(f'Expected argument of type {type(self)} or {type(1)} but got {type(other)}')

    def isLeapYear(self) -> bool:
        year = self.y
        if (not (year % 4) and year % 100) or (not (year % 400)):
            return True
        return False

    def maxDaysInThisMonth(self) -> int:
        return self.month_days[self.m - 1]

    def getDay(self) -> int:
        return self.d

    def getMonth(self) -> int:
        return self.m

    def getNextMonth(self) -> int:
        return self.m + 1 if self.m < 12 else 1

    def getYear(self) -> int:
        return self.y

    def setDay(self, day: int):
        if not isinstance(day, int):
            raise TypeError(f'Expected argument of type {type(1)} but got {type(day)}')
        if not 1 <= day <= self.maxDaysInThisMonth():
            raise AttributeError(f'Argument "day" is out of the expected range {1} to {self.maxDaysInThisMonth()}.')
        self.d = day

    def setMonth(self, month: int):
        if not isinstance(month, int):
            raise TypeError(f'Expected argument of type {type(1)} but got {type(month)}')
        if not 1 <= month <= 12:
            raise AttributeError(f'Argument "month" is out of the expected range 1 to 12.')
        self.m = month

    def setYear(self, year: int) -> None:
        if not isinstance(year, int):
            raise TypeError(f'Expected argument of type {type(1)} but got {type(year)}')
        self.y = year

    def setMonthDays(self):
        self.month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear():
            self.month_days[1] = 29

    def previousMonth(self):
        return 12 if self.m == 1 else self.m - 1

    def firstDayOfTheYear(self):
        return Date(1, 1, self.y)

    def numberOfDaysFromYearStart(self) -> int:
        return sum(self.month_days[:self.m - 1]) + self.d

    def numberOfDaysInThisYear(self):
        return 366 if self.isLeapYear() else 365

    def numberOfDaysRemainingInThisYear(self):
        return self.numberOfDaysInThisYear() - self.numberOfDaysFromYearStart()


if __name__ == '__main__':
    print('Running tests :')
    print(f'1: 1-1-2000 = 1-1-2000 : {Date(1, 1, 2000) == Date(1, 1, 2000)}')
    print(f'2: 1-1-2000 = 1-1-2001 : {Date(1, 1, 2000) == Date(1, 1, 2001)}')
    print(f'3: 1-1-2001 = 1-1-2000 : {Date(1, 1, 2001) == Date(1, 1, 2000)}')
    print(f'4: 1-2-2000 = 1-1-2000 : {Date(1, 2, 2000) == Date(1, 1, 2000)}')
    print(f'5: 1-1-2000 = 1-2-2000 : {Date(1, 1, 2000) == Date(1, 2, 2000)}')
    print(f'6: 2-1-2000 = 1-1-2000 : {Date(2, 1, 2000) == Date(1, 1, 2000)}')
    print(f'7: 1-1-2000 < 1-1-2000 : {Date(1, 1, 2000) < Date(1, 1, 2000)}')
    print(f'8: 1-1-2000 < 1-1-2001 : {Date(1, 1, 2000) < Date(1, 1, 2001)}')
    print(f'9: 1-1-2001 < 1-1-2000 : {Date(1, 1, 2001) < Date(1, 1, 2000)}')
    print(f'10: 1-2-2000 < 1-1-2000 : {Date(1, 2, 2000) < Date(1, 1, 2000)}')
    print(f'11: 1-1-2000 < 1-2-2000 : {Date(1, 1, 2000) < Date(1, 2, 2000)}')
    print(f'12: 2-1-2000 < 1-1-2000 : {Date(2, 1, 2000) < Date(1, 1, 2000)}')
    print(f'13: 1-1-2000 > 1-1-2000 : {Date(1, 1, 2000) > Date(1, 1, 2000)}')
    print(f'14: 1-1-2000 > 1-1-2001 : {Date(1, 1, 2000) > Date(1, 1, 2001)}')
    print(f'15: 1-1-2001 > 1-1-2000 : {Date(1, 1, 2001) > Date(1, 1, 2000)}')
    print(f'16: 1-2-2000 > 1-1-2000 : {Date(1, 2, 2000) > Date(1, 1, 2000)}')
    print(f'17: 1-1-2000 > 1-2-2000 : {Date(1, 1, 2000) > Date(1, 2, 2000)}')
    print(f'18: 2-1-2000 > 1-1-2000 : {Date(2, 1, 2000) > Date(1, 1, 2000)}')
    d1 = Date(1, 2, 2000)
    print(d1 + 10)
    print(d1 + 20)
    print(d1 + 30)
    print(d1 + 40)
    print(d1 + 50)
    print(d1 + 60)
    d2 = Date(28, 1, 2000)
    d3 = Date(1, 2, 2000)
    d4 = Date(1, 1, 2001)
    print(d2.isLeapYear())
    print(d1.maxDaysInThisMonth())
    print(d2 - d1)
    print(d3 - d1)
    print(d4 - d1)
