from dataclasses import dataclass, field, asdict, replace

@dataclass
class InventoryItem(object):
    id: str
    name: str
    price: float


@dataclass
class C:
    x: int
    y: int = field(repr=True)
    z: int = field(repr=True, default=10)
    t: int = 20

if __name__ == '__main__':
    obj = InventoryItem('1','Laptop', 850.99)
    print(obj)

    obj2 = InventoryItem('2','Laptop', 850.99)
    print(obj2)

    print(obj.__eq__(obj2))


    cobj = C(1,2)
    print(cobj)# This will hide y and z attributes here

    print (asdict(cobj))# converts instance into dict values

    replObj = replace(cobj)
    print(replObj)


