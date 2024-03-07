from person import Person

class Manager(Person):

    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)


if __name__ == '__main__':
    tom = Manager("Thomas Alwa", 25, 2000, job = "Manager")
    print (tom.name, tom.pay)

    # tom.giveRaise(.20)
    print(tom.pay)

    tamil = Person("Tamilselvan Radhakrishnan", 49, 10000, "Architect")      
    tarun = Person("Tarun Karthik", 18, 40000)

    people = [tamil, tarun, tom]

    for guy in people:
        guy.giveRaise(0.1)
        print(guy.name, guy.pay)