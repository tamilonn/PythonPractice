class Computer:
    def __init__(self):
        self.a='a value'
        self.__maxprice = 900

    # def sell(self):
    #     print("Selling Price: {}".format(self.__maxprice))

    # def setMaxPrice(self, price):
    #     self.__maxprice = price

# Creating a derived class 
class Derived(Computer): 
    def __init__(self): 
  
        # Calling constructor of 
        # Base class 
        Computer.__init__(self) 
        print("Calling private member of base class: ") 
        print(self.__maxprice) 

obj = Computer()
print(obj.a)

# Original selling price
# obj.sell()

# Attempting to change the price directly (This won't work because __maxprice is a private attribute)
# obj.__maxprice = 1000
print(obj.__maxprice)