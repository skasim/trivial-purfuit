from collections import namedtuple
from enum import Enum


class Color(namedtuple('color', 'color description'), Enum):
    RED = 'red', '#FF6347'
    WHITE = 'white', '#FFF5C3'
    BLUE = 'blue', '#3333FF'
    GREEN = 'green', '#2C6700'
    ORANGE = 'orange', '#FF9900'
    PURPLE = 'purple', '#CC99CC'
    YELLOW = 'yellow', '#FFFF66'
    BLACK = 'black', '#000000'

    def __str__(self) -> str:
        return self.name
