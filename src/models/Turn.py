class Turn(object):
    """
    Object representing a turn. The object answers the question: "whose turn is it?"
    1 = player 1
    2 = player 2
    3 = player 3
    4 = player 4

    :param `player_turn`: At object instantiation player turn is set to 1
    :type `player_turn`: int
    """

    def __init__(self, player_turn=1):
        self._player_turn = player_turn

    @property
    def player_turn(self):
        """
        Getter method to return current players turn.

        :return: the turn of the current player
        :rtype: iht
        """
        return self._player_turn

    def increment_player_turn(self, total_players):
        """
        Method when called increments the player turn to the next player. After reaching the final player, the turn is
        incremented to 1

        :param total_players: number of total players playing the game
        :return: the Player turn
        :rtype: int
        """
        if self._player_turn < total_players:
            self._player_turn = self._player_turn + 1
        else:
            self._player_turn = 1
