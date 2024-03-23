class Person:

    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def giveRaise(self, percent):
        self.pay *= 1.0 + percent

if __name__ == '__main__':
    tamil = Person("Tamilselvan Radhakrishnan", 49, 10000, "Architect") 

    print(tamil)     
    tarun = Person("Tarun Karthik", 18, 40000)
    print(tamil.name, tarun.pay)

    tarun.giveRaise(10)
    print(tarun.pay)
