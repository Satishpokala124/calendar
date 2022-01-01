from copy import copy


class Date:
    def __init__(self, day: int, month: int, year: int):
        self.d: int = 0
        self.m: int = 0
        self.y: int = 0
        self.setYear(year)
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
        if self.y < self.y:
            return False
        elif self.m < other.m:
            return False
        elif self.d < self.d:
            return False
        return True

    def __lt__(self, other) -> bool:
        if self.y < other.y:
            return True
        elif self.y == other.y:
            if self.m < other.m:
                return True
            elif self.m == other.m:
                if self.d < other.d:
                    return True
        return False

    def __le__(self, other) -> bool:
        if self.y > other.y:
            return False
        elif self.m > other.m:
            return False
        elif self.d > other.d:
            return False
        return True

    def __add__(self, days: int):
        newDay = copy(self)
        while newDay.d + days > newDay.maxDays():
            days -= (newDay.maxDays() - newDay.d)
            newDay.d = 0
            newDay.m = newDay.getNextMonth()
            if newDay.m == 1:
                newDay.y += 1
        newDay.d += days
        return newDay

    def __sub__(self, other):
        # "other" can be a Date object or an integer.
        pass

    def isLeapYear(self) -> bool:
        year = self.y
        if (not year % 4 and year % 100) or (not year % 400):
            return True
        return False

    def maxDays(self) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear():
            days[1] = 29
        return days[self.m - 1]

    def getDay(self) -> int:
        return self.d

    def getMonth(self) -> int:
        return self.m

    def getNextMonth(self) -> int:
        return self.m + 1 if self.m <= 12 else 1

    def getYear(self) -> int:
        return self.y

    def setDay(self, day: int) -> None:
        if 0 < day <= self.maxDays():
            self.d = day

    def setMonth(self, month: int) -> None:
        if 0 < month <= 12:
            self.m = month

    def setYear(self, year: int) -> None:
        self.y = year


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
    print(d1.isLeapYear())
    print(d1.maxDays())
    print(d1 + 10)
    print(d1 + 20)
    print(d1 + 30)
    print(d1 + 40)
    print(d1 + 50)
    print(d1 + 60)
