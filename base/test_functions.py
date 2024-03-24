


def calcfunc(a, b):
    average = (a + b )/2

    total = a + b

    return average, total


def main():
    ave, tot = calcfunc(4,8)
    print(ave)
    print (tot)

if __name__ == '__main__':
    main()