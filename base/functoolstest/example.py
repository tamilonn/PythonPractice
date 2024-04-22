from functools import partial

# Original function
def multiply(x, y):
    return x * y
# Create a new function that multiplies by 2

doubleValue = partial(multiply, y=2)
result = doubleValue(5)

print(result)  # Output: 10

print('-------------- partial end -------------------------------')

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """This is the wrapper function."""
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def my_function():
    """This is my function."""
    pass

print(my_function.__name__)  # Output: 'my_function'
print(my_function.__doc__)   # Output: 'This is my function.'
print('-------------- wraps end -------------------------------')

from functools import lru_cache

@lru_cache(maxsize=None)  # None means no limit on cache size
def add(a, b):
    print(f'Adding {a}, {b}')
    return a + b

result = add(10, 5)
print(result)  

result = add(10, 5)
print(result)

result = add(20,10)
print(result)

result = add(10, 5)
print(result)

result = add(20,10)
print(result)
print('-------------- lru_cache end -------------------------------')

from functools import total_ordering

@total_ordering
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

# Create instances of Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 30)

print(person1 == person2) # False
print(person1 < person2)  # False
print(person1 <= person2) # False
print(person1 > person2)  # True
print(person1 == person3) # True
print('-------------- total_ordering end -------------------------------')

from functools import reduce

data = [1, 2, 3, 4, 5]

# Calculate the product of all elements
product = reduce(lambda x, y: x * y, data)

print(product)  # Output: 120
print('-------------- reduce end -------------------------------')