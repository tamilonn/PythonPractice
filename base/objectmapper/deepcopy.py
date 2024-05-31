from dataclasses import dataclass
from automapper import mapper

@dataclass
class Address:
    street: str
    number: int
    zip_code: int
    city: str
  
class PersonInfo:
    def __init__(self, name: str, age: int, address: Address):
        self.name = name
        self.age = age
        self.address = address

class PublicPersonInfo:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

address = Address(street="Main Street", number=1, zip_code=100001, city='Test City')
info = PersonInfo('John Doe', age=35, address=address)

# default deepcopy behavior
public_info = mapper.to(PublicPersonInfo).map(info)
print("Target public_info.address is same as source address: ", address is public_info.address)
# Target public_info.address is same as source address: False

# disable deepcopy
public_info = mapper.to(PublicPersonInfo).map(info, use_deepcopy=False)
print("Target public_info.address is same as source address: ", address is public_info.address)
# Target public_info.address is same as source address: True