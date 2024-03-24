# using decorator to calculate execution time.

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        returned_value = func(*args, **kwargs)
        endTime = time.time()
        print(f"Execution time: {endTime - startTime} seconds")
        return returned_value
    return wrapper

@measure_time
def add(a,b):
    print("Inside add() function....")
    return a + b

# @measure_time
# def sub(a,b):
#     return a-b

# def multiply(a,b):
#     return a*b

@measure_time
def hello():
    print("Hello World!!")




if __name__ == '__main__':
    

    # hello()

    a,b = 1,2
    print("sum =  ", add(a,b))
    


    
    