class Slices(object):
    """
    Object representing the cake slices earned by a player. Each of the colors is represented
    individually and since the player starts the game having won no slices, the colors of each slice are
    set to `False`
    """

    def __init__(self):
        self._red = False
        self._green = False
        self._blue = False
        self._white = False

    @property
    def red(self):
        """
        Getter method representing red slice

        :return: boolean
        """
        return self._red

    @property
    def green(self):
        """
        Getter method representing green slice

        :return: boolean
        """
        return self._green

    @property
    def blue(self):
        """
        Getter method representing blue slice

        :return: boolean
        """
        return self._blue

    @property
    def white(self):
        """
        Getter method representing white slice

        :return: boolean
        """
        return self._white

    @red.setter
    def red(self, red):
        """
        Setter method to set whether slice is earned

        :param red: boolean value for whether slice has been earned
        """
        self._red = red

    @green.setter
    def green(self, green):
        """

        :param green: boolean value for whether slice has been earned
        """
        self._green = green

    @blue.setter
    def blue(self, blue):
        """
        Setter method to set whether slice is earned

        :param blue: boolean value for whether slice has been earned
        """
        self._blue = blue

    @white.setter
    def white(self, white):
        """
        Setter method to set whether slice is earned

        :param white: boolean value for whether slice has been earned
        """
        self._white = white

    def get_slices_won(self):
        """
        Method that returns as a string the slices earned by a player reprsented by the color boolean
        getting set to `True`

        :return: Slices won by a player
        :rtype: str
        """

        slices_won = '['

        if self._red:
            slices_won += 'R '
        if self._green:
            slices_won += 'G '
        if self._blue:
            slices_won += 'B '
        if self._white:
            slices_won += 'W'
        slices_won += "]"

        return slices_won
