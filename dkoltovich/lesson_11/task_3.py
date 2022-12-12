"""
Задание 3.
Написать класс Iterator, который принимает необязательный параметр start_year: int
- начальный год, который по-умолчанию равен году вашего рождения, и при передаче
объекта этого класса в for, он может бесконечно возвращать объекты класса Birthday,
который, в свою очередь, при передаче в print возвращает "<год> <день недели>".
"""
import datetime


class Birthday:
    """
    Class that represents birthday
    Attributes:
        weekdays: dict - dict where keys are ordered numbers and values are weekdays
    """
    weekdays = {0: 'понедельник',
                1: 'вторник',
                2: 'среда',
                3: 'четверг',
                4: 'пятница',
                5: 'суббота',
                6: 'воскресенье'
                }

    def __init__(self, year: int = 2004, month: int = 7, day: int = 5):
        """
        Initialization of birthday objects.
        :param year: birth year
        :param month: birth month
        :param day: birthday
        """
        self.year = year
        self.weekday = self.weekdays[datetime.date(year, month, day).weekday()]

    def __str__(self):
        """
        Representation of Birthday object as a string with birth year and weekday
        """
        return '{} {}'.format(self.year, self.weekday)


class Iterator:
    """
    Class represents iterator for Birthday objects
    Attributes:
        int start_year: start year for iteration
        int current_year: current year, last year for iteration
    """
    def __init__(self, start_year: int = 2004, birth_month: int = 7, birth_day: int = 5):
        """
        Initialization of Iterator objects.
        :param start_year: start year for iteration
        """
        self.start_year = start_year
        self.month = birth_month
        self.day = birth_day
        self.current_year = datetime.datetime.now().year

    def __next__(self):
        """
        Returns Birthday object and increases birth year each time it's called
        while birth year less or equal current year
        :return: Birthday object
        """
        if self.start_year > self.current_year:
            raise StopIteration
        birthday = Birthday(self.start_year, self.month, self.day)
        self.start_year += 1
        return birthday

    def __iter__(self):
        """
        :return: Iterator object
        """
        return self



bd_iter = Iterator()
for bd in bd_iter:
    print(bd)


