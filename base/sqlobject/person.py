from sqlobject import *

sqlhub.processConnection = connectionForURI('sqlite:/:memory:')
# sqlhub.processConnection = connectionForURI('sqlite:///testDB.db')


class Person(SQLObject):
    fname = StringCol()
    mi = StringCol(length=1, default=None)
    lname = StringCol()

Person.createTable()

p = Person(fname="John", lname="Doe")
print(p)