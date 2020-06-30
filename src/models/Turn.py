class Turn(object):
    def __init__(self, player_turn=1):
        self._player_turn = player_turn

    @property
    def player_turn(self):
        return self._player_turn

    @player_turn.setter
    def player_turn(self, total_players):
        if self._player_turn < total_players:
            self._player_turn = self._player_turn + 1
        else:
            self._player_turn = 1

# TODO delete
# turn = Turn()
#
# print(str(turn.player_turn))
# turn.player_turn = 4 # this is how you pass values to an attribue in python
# print(turn.player_turn)