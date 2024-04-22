class Computer:

    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def __str__(self):
        return ', '.join(self.components)
    
#-------------------------------------------------------------------
from abc import ABC, abstractmethod

class ComputerBuilder(ABC):

    @abstractmethod
    def add_processor(self):
        pass

    @abstractmethod
    def add_memory(self):
        pass

    @abstractmethod
    def add_storage(self):
        pass

    @abstractmethod
    def get_computer(self):
        pass

#-------------------------------------------------------------------
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def add_processor(self):
        self.computer.add_component("High-end Processor")

    def add_memory(self):
        self.computer.add_component("16GB RAM")

    def add_storage(self):
        self.computer.add_component("1TB SSD")

    def get_computer(self):
        return self.computer
    
#-------------------------------------------------------------------
class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_computer(self):
        self.builder.add_processor()
        self.builder.add_memory()
        self.builder.add_storage()

    def get_computer(self):
        return self.builder.get_computer()
    

if __name__ == '__main__':
    gaming_builder = GamingComputerBuilder()
    director = ComputerDirector(gaming_builder)

    director.construct_computer()

    gaming_computer = director.get_computer()
    print(f"Gaming Computer: {gaming_computer}")

# Output:
# Gaming Computer: High-end Processor, 16GB RAM, 1TB SSD