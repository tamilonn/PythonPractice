from typing import ClassVar

class MyClass:
    counter: ClassVar[int]=1
    clsName: ClassVar[str]=''
    name: str

    def __init__(self, name) -> None:
        self.name=name

    def display(self)  -> None:
        print(MyClass.counter)
        print(MyClass.clsName)
        print(self.name)
        


if __name__ == '__main__':
    class1 = MyClass('India')
    class1.display()
    MyClass.clsName="MyClass"

    class1.name = 'pak'

    class1.counter +=1

    class1.display()
    MyClass.counter=100


    class2 = MyClass('Nepal')
    class2.display()

    class3= MyClass('China')
    class3.display()


