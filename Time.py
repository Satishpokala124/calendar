class Time:
    hour: int = 0
    minute: int = 0

    def __init__(self, h, m) -> None:
        self.set_hour(h)
        self.set_minute(m)

    def set_hour(self, h):
        if h < 0 or h > 24:
            raise RuntimeError
        self.hour = int(h)

    def set_minute(self, m):
        if m < 0 or m > 60:
            raise RuntimeError
        self.minute = int(m)

    def __str__(self):
        return f'{str(self.hour).rjust(2, "0")}:{str(self.minute).rjust(2, "0")}'

    def __sub__(self, other):
        if not isinstance(other, Time):
            raise TypeError
        small_ts, big_ts = [self, other] if self < other else [other, self]
        hr_diff = big_ts.hour - small_ts.hour
        min_diff = big_ts.minute - small_ts.minute
        return hr_diff + (min_diff / 60)
