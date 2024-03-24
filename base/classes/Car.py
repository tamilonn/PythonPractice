class Car:
    __model = ""
    __make = ""

    def __init__(self, model, *, make, year=""):
        self.model = model
        self.make = make
        self.year = year
        self.val = 10


    # def __init__(self, model, make, year):
    #     self.model = model
    #     self.make = make
    #     self.year = year    


    def display(self):
        print("Car is "+ self.model + ", "+ self.make + ", "+ self.year  + ", " + str(self.val ))


