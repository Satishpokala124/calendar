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
        return self>other and self==other

    def __lt__(self, other) -> bool:
        return not self>=other

    def __le__(self, other) -> bool:
        return self<other and self==other

    def __add__(self, days) -> None:
        pass

    def isLeapYear(self) -> bool:
        year = self.y
        if (not (year % 4) and year % 100) or (not (year % 400)):
            return True
        return False

    def maxDays(self) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear():
            days[1] = 29
        return days[self.m-1]

    def getDay(self) -> int:
        return self.d

    def getMonth(self) -> int:
        return self.m

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
