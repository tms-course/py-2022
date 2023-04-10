from datetime import date


class Birthday:
    weekday_map: list = [
        'понедельник',
        'вторник',
        'среда',
        'четверг',
        'пятница',
        'суббота',
        'воскресение',
    ]

    def __init__(self, year: int, month: int = 1, day: int = 27) -> None:
        self.year = year
        self.month = month
        self.day = day

    def __str__(self) -> str:
        dt = date(self.year, self.month, self.day)
        return f"{self.year} {self.weekday_map[dt.weekday()]}"

class Iterator:
    def __init__(self, start_year: int = 1994) -> None:
        self.start_year = start_year

    def __iter__(self) -> 'Iterator':
        self.year = self.start_year

        return self
    
    def __next__(self) -> Birthday:
        year = self.year
        self.year += 1

        return Birthday(year)
        
from time import sleep
bd_iter = Iterator(2006)
for bd in bd_iter:
    print(bd)
    sleep(1)