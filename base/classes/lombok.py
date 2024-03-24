from dataclasses import dataclass

@dataclass()
class Name:
    first_name: str
    last_name: str

yoni = Name("Yoni", "Alaluf")
yoni2 = Name("Jony", "Alaluf")
print(yoni) # Name(first_name='Yoni', last_name='Alaluf')
print(yoni2) # Name(first_name='Jony', last_name='Alaluf')
print(yoni == yoni2) # False