from enum import Enum

class Color(Enum):
    RED='1'
    GREEN='2'
    BLUE='3'



Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])
print(Color)
for color in Color:
    print(f"{color.name} , {color.value}")