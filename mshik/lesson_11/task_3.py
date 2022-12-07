"""
Задание 3.

Написать класс Iterator, который принимает необязательный параметр start_year: int
- начальный год, который по-умолчанию равен году вашего рождения, и при передаче
объекта этого класса в for, он может бесконечно возвращать объекты класса Birthday,
который, в свою очередь, при передаче в print возвращает "<год> <день недели>".
"""
import datetime
import enum


@enum.unique
class Weekday(enum.Enum):
    понедельник = 0
    вторник = 1
    среда = 2
    четверг = 3
    пятница = 4
    суббота = 5
    воскрсенье = 6


class Birthday:
    """
    A class used to represent a Birthday.

    Arguments:
        year (int): Year
        month (int): Birthday month
        day (int): Birthday day
    """
    __slots__ = ("_year", "_month", "_day")

    def __init__(self, year: int, month: int = 8, day: int = 10) -> None:
        """
        Attrs:
            year (int): Year
            month (int): Birthday month
            day (int): Birthday day
        """
        self._year = year
        self._month = month
        self._day = day

    def get_weekday_from_date(self) -> int:
        "Returns day of the week, where Monday == 0 ... Sunday == 6."
        date = datetime.date(self._year, self._month, self._day)
        return date.weekday()

    def __str__(self) -> str:
        "Returns string with year and weekday."
        weekday = self.get_weekday_from_date()
        return f"{self._year} {Weekday(weekday).name}"
        

class Iterator:
    """
    Iterator to generate birthday objects.
    
    Arguments:
        start_year (int): Year from which start iterating
    """
    def __init__(self, start_year: int = 2001) -> None:
        """
        Attrs:
            start_year (int): Year from which start iterating
        """
        self._start_year = start_year
    
    def __iter__(self):
        return self
    
    def __next__(self) -> str:
        """
        Returns birthday object on each call,if start_year less than datetime.MAXYEAR.
        
        Returns:
            birthday (str): String representation of Birthday object
        
        Exception:
            StopIteration: Error will be raised, if start_year greater than datetime.MAXYEAR
        """
        if self._start_year <= datetime.MAXYEAR:
            birthday = Birthday(self._start_year)
            self._start_year += 1
            return birthday
        else:
            raise StopIteration


bd_iter = Iterator(2000)
for bd in bd_iter:
    print(bd)