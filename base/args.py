
def myfunc(*args):
    for i in args:
        print(f"Arguments -{i}")


myfunc("I", "am", "passing", "multiple", "arguments")

def myfunc(arg1, *args):
    print(f"First argement= {arg1}")
    for i in args:
        print(f"Arguments -{i}")

myfunc("I", "am", "passing", "multiple", "arguments")


#keywork arguments **kwargs-----------------------------------------------------------------------
def states(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s" % (key,value))

states(TN='Tamil Nadu', KA='Karnataka', AN='Andhra')


def country_states(*args, **kwargs):
    for i in args:
        print(f'non keyward argement={i}')

    for key,value in kwargs.items():
        print("%s == %s" % (key,value))


country_states('India', 'China', 'Russia', TN='Tamil Nadu', KA='Karnataka', AN='Andhra')

#call *args and **kwargs to single function-----------------------------------------------------------
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ("I","Love","India")
kwargs = {"arg1": "I", "arg2": "Love", "arg3": "India"}
myFun(*args)
myFun(**kwargs)

# defining car class *args-------------------------------------------------------------------------------------
class car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        # access args index like array does
        self.speed = args[0]
        self.color = args[1]
 
 
# creating objects of car class
audi = car(200, 'red')
bmw = car(250, 'black')
mb = car(190, 'white')
 
# printing the color and speed of the cars
print(audi.color)
print(bmw.speed)

# defining car class *kwargs-------------------------------------------------------------------------------------
# defining car class
class car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, **kwargs):
        # access args index like array does
        self.speed = kwargs['s']
        self.color = kwargs['c']
 
 
# creating objects of car class
audi = car(s=200, c='red')
bmw = car(s=250, c='black')
mb = car(s=190, c='white')
 
# printing the color and speed of cars
print(bmw.color)
print(bmw.speed)