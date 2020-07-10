from src.models.Slices import Slices


class Player(object):
    """
    Object representing a player marker

    :param name: The variable name is used to store the name of the player
    :type name` str

    """

    def __init__(self, name):
        self._name = name
        self._slices = Slices()

    @property
    def name(self):
        """
        Getter method to get name of player

        :return: name of player
        :rtype: str
        """
        return self._name

    @property
    def slices(self):
        """
        Getter method to return Slices object for the player

        :return: Slices player has won
        :rtype: Slices
        """
        return self._slices

    @name.setter
    def name(self, name):
        """
        Setter method to set player name

        :param name: Represents the player name as game marker
        """
        self._name = name

    @slices.setter
    def slices(self, slices):
        """
        Setter method to set Slices object for the player

        :param slices: Slices object
        """
        self._slices = slices
