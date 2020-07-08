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
    LIGHT_BLUE = 'light blue', '#ADD8E6'

    def __str__(self) -> str:
        return self.name

    def return_color_from_hex(self):
        if self == Color.RED.description:
            return Color.RED.color
        elif self == Color.WHITE.description:
            return Color.WHITE.color
        elif self == Color.BLUE.description:
            return Color.BLUE.color
        elif self == Color.GREEN.description:
            return Color.GREEN.color
        elif self == Color.ORANGE.description:
            return Color.ORANGE.color
        elif self == Color.ORANGE.description:
            return Color.ORANGE.color
        elif self == Color.YELLOW.description:
            return Color.YELLOW.color
        elif self == Color.BLACK.description:
            return Color.BLACK.color
        elif self == Color.LIGHT_BLUE.description:
            return Color.LIGHT_BLUE.color
