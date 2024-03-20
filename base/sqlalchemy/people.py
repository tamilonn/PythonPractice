from sqlalchemy import create_engine, ForeignKey, Column, Integer, CHAR, String
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self,ssn, first, last, gen,age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gen
        self.age = age

    
    def __repr__(self):
        return f"({self.ssn})  {self.firstname} {self.lastname}({self.gender}, {self.age})"
    
    
engine = create_engine("sqlite:///testDB.db", echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()

person = Person(12345, 'Tamilselvan', 'Radhakrishnan', 'M', 49)
session.add(person)
session.commit()

# #Add more person records

p1 = Person(56789, 'Padmini', 'Tamilselvan', 'F', 43)
p2 = Person(77777, 'Tarun', 'Tamilselvan', 'M', 18)
p3 = Person(88889, 'Navya', 'Tamilselvan', 'F', 9)
p4 = Person(99999, 'Mohan', 'Raj', 'M', 26)

session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)
session.commit()

resultSet = session.query(Person).all()



print('-----------------------------------')
for i in resultSet:
    print(i)


resultSet = session.query(Person).filter(Person.lastname == 'Tamilselvan')

print('-----------------------------------')
for i in resultSet:
    print(i)


resultSet = session.query(Person).filter(Person.firstname.in_(["Mohan"]))

print('-----------------------------------')
for i in resultSet:
    print(i)
