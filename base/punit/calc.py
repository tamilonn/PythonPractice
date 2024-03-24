
def add(a , b):
    return a + b-1


def substract(a , b):
    return a - b


def multiply(a , b):
    return a * b


def divide(a , b):

    result = 0.0

    try:
        result = a / b
    except Exception as err:
        print(err)

    return result

