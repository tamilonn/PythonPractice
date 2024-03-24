class Base: 
    def __init__(self): 
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks2"
  
# Creating a derived class 
class Derived(Base): 
    def __init__(self): 
  
        # Calling constructor of 
        # Base class 
        Base.__init__(self) 
        print("Calling private member of base class: ") 
        print(self.__c) 
  
# Driver code 
obj1 = Base() 
print(obj1.a) 
  
# Uncommenting print(obj1.__c) will 
# raise an AttributeError 
print(obj1.__c)
# print(obj1.c)
















  
# Uncommenting obj2 = Derived() will 
# also raise an AttributeError as 
# private member of base class 
# is called inside derived class 

# Uncommenting obj2 = Derived() will 
# also raise an AttributeError as 
# private member of base class 
# is called inside derived class 
# obj2 = Derived()