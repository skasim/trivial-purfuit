class Slices(object):
    """
    Object representing the cake slices earned by a player. Each of the colors is represented
    individually and since the player starts the game having won no slices, the colors of each slice are
    set to `False`
    """

    def __init__(self):
        self._category1 = False
        self._category4 = False
        self._category3 = False
        self._category2 = False

    @property
    def category1(self):
        """
        Getter method representing category1 slice

        :return: boolean
        """
        return self._category1

    @property
    def category4(self):
        """
        Getter method representing category4 slice

        :return: boolean
        """
        return self._category4

    @property
    def category3(self):
        """
        Getter method representing category3 slice

        :return: boolean
        """
        return self._category3

    @property
    def category2(self):
        """
        Getter method representing category2 slice

        :return: boolean
        """
        return self._category2

    @category1.setter
    def category1(self, category1):
        """
        Setter method to set whether slice is earned

        :param category1: boolean value for whether slice has been earned
        """
        self._category1 = category1

    @category4.setter
    def category4(self, category4):
        """

        :param category4: boolean value for whether slice has been earned
        """
        self._category4 = category4

    @category3.setter
    def category3(self, category3):
        """
        Setter method to set whether slice is earned

        :param category3: boolean value for whether slice has been earned
        """
        self._category3 = category3

    @category2.setter
    def category2(self, category2):
        """
        Setter method to set whether slice is earned

        :param category2: boolean value for whether slice has been earned
        """
        self._category2 = category2

    def get_slices_won(self):
        """
        Method that returns as a string the slices earned by a player reprsented by the color boolean
        getting set to `True`

        :return: Slices won by a player
        :rtype: str
        """

        slices_won = '['

        if self._category1:
            slices_won += 'R '
        if self._category4:
            slices_won += 'G '
        if self._category3:
            slices_won += 'B '
        if self._category2:
            slices_won += 'W'
        slices_won += "]"

        return slices_won
