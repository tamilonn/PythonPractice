class Car:
    __model = ""
    __make = ""

    def __init__(self, model, *, make, year="", __prival=0):
        self.model = model
        self.make = make
        self.year = year
        self.__prival = 10


    # def __init__(self, model, make, year):
    #     self.model = model
    #     self.make = make
    #     self.year = year    


    def display(self):
        print("Car is "+ self.model + ", "+ self.make + ", "+ self.year  + ", " + self.__prival )


