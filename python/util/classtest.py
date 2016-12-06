# -*- coding: UTF-8 -*-
from __future__ import print_function

class A:
    def __init__(self):
        self.one = 'one'
        print('init A')
class B:
    def __init__(self):
        self.two = 'two'
        print('init B')

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
    def printselfnum(self):
        print(self.one, self.two)
c = C()
c.printselfnum()
print(c.one)
print(c.two)
print(C.__dict__.keys())



class Person:
    def __init__(self):
       self.__name = 'haha'  # private property
       self.age = 22          # public
       self._title = 'manager'  # public

    def __get_name(self):  # private method
        return self.__name

    def get_age(self):
        return self.age

    @property
    def title(self):
        return self._title


person = Person()
print(person.get_age(), person.age)
person.age = 30
print(person.get_age(), person.age)
print(person._title, person.title)
person._title = 'PM'
print(person._title)
print(person._title, person.title)
# print(person.__name)    # AttributeError: Person instance has no attribute '__name'
# print(person.__get_name())    # AttributeError: Person instance has no attribute '__get_name'


class Date1(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, day=0, month=0, year=0):
       self.day = day
       self.month = month
       self.year = year

    @classmethod
    def from_string(cls, date_as_string):
       day, month, year = map(int, date_as_string.split('-'))
       date1 = cls(day, month, year)
       return date1

    @staticmethod
    def is_date_valid(date_as_string):
       day, month, year = map(int, date_as_string.split('-'))
       return day <= 31 and month <= 12 and year <= 3999

# usage:
date2 = Date1.from_string('11-09-2012')
print(date2)
is_date = Date1.is_date_valid('11-09-2012')
print(is_date)


class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day   = day
        self.year  = year

    def display(self):
        print("{0}-{1}-{2}".format(self.month, self.day, self.year))


    @staticmethod
    def millenium(month, day):
        return Date(month, day, 2000)

new_year = Date(1, 1, 2013)               # Creates a new Date object
millenium_new_year = Date.millenium(1, 1) # also creates a Date object. 

# Proof:
print(new_year.display())           # "1-1-2013"
print(millenium_new_year.display()) # "1-1-2000"

isinstance(new_year, Date) # True
isinstance(millenium_new_year, Date) # True


class DateTime(Date):
    def display(self):
        print("{0}-{1}-{2} - 00:00:00PM".format(self.month, self.day, self.year))


datetime1 = DateTime(10, 10, 1990)
datetime2 = DateTime.millenium(10, 10)

print(isinstance(datetime1, DateTime)) # True
print(isinstance(datetime2, DateTime)) # False

datetime1.display() # "10-10-1990 - 00:00:00PM"
datetime2.display() # "10-10-2000" because it's not a DateTime object but a Date object. Check the implementation of the millenium method on the Date class