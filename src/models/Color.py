from collections import namedtuple
from enum import Enum


class Color(namedtuple('color', 'color description'), Enum):
    """
    Enum representing Color string and hex value
    """
    RED = 'red', '#FF6347'
    WHITE = 'white', '#FFFFFF'
    BLUE = 'blue', '#3333FF'
    GREEN = 'green', '#2C6700'
    ORANGE = 'orange', '#FF9900'
    PURPLE = 'purple', '#CC99CC'
    YELLOW = 'yellow', '#FFFF66'
    BLACK = 'black', '#000000'
    LIGHT_BLUE = 'light blue', '#ADD8E6'
    LIGHT_GREEN = 'light green', '#90EE90'
    LIGHT_PURPLE = 'light purple', '#E0BBE4'

    def __str__(self) -> str:
        return self.name

    def return_color_from_hex(self):
        """
        Method takes the enum description (i.e., hex value) and return color

        :return: Color
        :rtype: str
        """
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
        elif self == Color.LIGHT_GREEN.description:
            return Color.LIGHT_GREEN.color
        elif self == Color.LIGHT_PURPLE.description:
            return Color.LIGHT_PURPLE.color

    def return_hex_from_color(self):
        """
        Method takes a color string and returns its hex value

        :return: str
        """
        if self == 'red':
            return Color.RED.description
        elif self == 'white':
            return Color.WHITE.description
        elif self == 'blue':
            return Color.BLUE.description
        elif self == 'green':
            return Color.GREEN.description
