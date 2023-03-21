"""
Написать класс Iterator, который принимает необязательный параметр start_year: int - начальный год,
который по умолчанию равен году вашего рождения, при передаче объекта этого класса в for, он может
бесконечно возвращать объекты класса Birthday, который, в свою очередь, при передаче в print возвращает
"<год> <дунь недели>"
bd_iter = Iterator(2006)
for bd in bd_iter:
    print(bd)
# 2006 вторник
# 2007 среда
# ...
"""

import datetime



class Birthday(object):
    """class that represtnts birthday"""
    weekdays = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    def __init__(self, year: int, month: int = 11, day: int = 5) -> None:
        self.year = year
        self.month = month
        self.day = day

    def weekday_for_next(self) -> int:
        """ 
        Method for convert date in weekday in int format
        """
        weekday = datetime.datetime.weekday(datetime.date(self.year, self.month, self.day))
        return weekday


    def __str__(self) -> str:
        """ 
        returns: 
        """
        day = self.weekday_for_next()
        return f"{self.year} {Birthday.weekdays[day]}"



class Iterator():
    """Iterator for generate birthday objects"""
    def __init__(self, start_year: int = 1990):
        """:param start_year: year fo start iteration"""
        self.start_year = start_year

    def __iter__(self):
        """Turn object into iterator"""
        self.year = self.start_year
        return self


    def __next__(self):
        """
        Method for return birthday object in each call
        :return: birthday object
        """
        if self.year <= datetime.MAXYEAR:
            birthday = Birthday(self.year)
            self.year += 1
            return birthday
        else:
            raise StopIteration



bd_iter = Iterator()
for bd in bd_iter:
    print(bd)

