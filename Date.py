from copy import copy


class Date:
    def __init__(self, day: int, month: int, year: int):
        self.d: int = 0
        self.m: int = 0
        self.y: int = 0
        self.month_days = None
        self.setYear(year)
        self.setMonthDays()
        self.setMonth(month)
        self.setDay(day)

    def __str__(self) -> str:
        return f'{self.d}-{self.m}-{self.y}'

    def __eq__(self, other) -> bool:
        return self.d == other.d and self.m == other.m and self.y == other.y

    def __gt__(self, other) -> bool:
        if self.y > other.y:
            return True
        elif self.y == other.y:
            if self.m > other.m:
                return True
            elif self.m == other.m:
                if self.d > other.d:
                    return True
        return False

    def __ge__(self, other) -> bool:
        return self > other or self == other

    def __lt__(self, other) -> bool:
        return not self >= other

    def __le__(self, other) -> bool:
        return self < other or self == other

    def __add__(self, days: int):
        new_date = copy(self)
        while new_date.d + days > new_date.maxDaysInThisMonth():
            days -= (new_date.maxDaysInThisMonth() - new_date.d)
            new_date.d = 0
            new_date.m = new_date.getNextMonth()
            new_date.y += 1 if new_date.m == 1 else 0
        new_date.d += days
        return new_date

    def __sub__(self, other):
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
            days_remaining_in_the_year_of_smaller_day = smaller_day.numberOfDaysRemainingInThisYear()
            days_from_year_start_bigger_day = bigger_day.numberOfDaysFromYearStart()
            days_between_years = sum([Date(1, 1, i).numberOfDaysInThisYear() for i in range(smaller_day.y+1, bigger_day.y)])
            return days_remaining_in_the_year_of_smaller_day + days_between_years + days_from_year_start_bigger_day
        else:
            return TypeError

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

    def setDay(self, day: int) :
        if 0 < day <= self.maxDaysInThisMonth():
            self.d = day
        else:
            print("Invalid Day :", day)
            return RuntimeError

    def setMonth(self, month: int):
        if 0 < month <= 12:
            self.m = month
        else:
            print("Invalid Month :", month)
            return RuntimeError

    def setYear(self, year: int) -> None:
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
        return sum(self.month_days[:self.m-1]) + self.d

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
