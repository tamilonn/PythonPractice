from Car import Car

def main():
    honda = Car("Honda", make="City")
    print("make= "+ honda.make)
    print("model= "+ honda.model)

    honda.display()
    print("------------------------------------")

    toyota = Car("Toyota", make="Etios", year="2024")
    print("make= "+ toyota.make)
    print("model= "+ toyota.model)

    toyota.display()
    print("------------------------------------")

    

    maruti = Car("Maruti", make="", year="2024")
    print("make= "+ maruti.make)
    print("model= "+ maruti.model)
    print("year= "+ maruti.year)

    maruti.display()
    print("------------------------------------")

    hyundai = Car("Hyundai", make="")
    hyundai.display()

    hyundai.make="Creta"
    hyundai.display()

if __name__ == '__main__':
    main()