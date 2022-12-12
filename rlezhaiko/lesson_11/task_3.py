""" 
2. Написать класс Iterator, который принимает необязательный параметр start_year: int -
начальный год, который по умолчанию равен году вашего рождения, и при передаче
объекта этого класс в for, он может бесконечно возвращать объекты класса Birthday,
который, в свою очередь, при передаче в print возвращает "<год> <день недели>".
bd_iter = Iterator(2006)
for bd in bd_iter:
    print(bd)
# 2006 вторник
# 2007 среда
# ...
"""
from __future__ import annotations
import datetime


class Iterator(object):
    """ 
    Iterator for generate birthday objects from start_year to 9999 year.
    """
    def __init__(self, start_year: int = 1997) -> None:
        """ 
        :param start_year: year for start iteration. Defaults 1997 
        """
        self.start_year = start_year
    
    
    def __iter__(self):
        """ 
        Turn an iterable object into an iterator
        """
        self.year = self.start_year
        return self
    
    
    def __next__(self) -> Birthday:
        """ 
        Method for return birthday object on each call
        
        :returns: return Birthday object
        """
        if self.year <= datetime.MAXYEAR:
            birthday = Birthday(self.year)
            self.year += 1
            return birthday
        else:
            raise StopIteration


class Birthday(object):
    """ 
    A class representing a person's birthday
    """
    def __init__(self, year: int, month: int = 7, day: int = 5) -> None:
        """ 
        :param year: year of birthday
        :param month: month of birthday
        :param day: day of birthday
        """
        self.year = year
        self.month = month
        self.day = day
        self.weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    
    
    def weekday_from_date(self) -> int:
        """ 
        Method for convert date in weekday in int format. 
        
        :returns: return weekday in in format. 0 - Sunday, 6 - Saturday
        """
        weekday = datetime.datetime.weekday(datetime.date(self.year, self.month, self.day))
        return weekday
    
    
    def __str__(self) -> str:
        """ 
        returns: return a string consisting of the year and the day of the week
        """
        day = self.weekday_from_date()
        return f"{self.year} {self.weekdays[day]}"
    

bd_iter = Iterator(2006)
for bd in bd_iter:
    print(bd)