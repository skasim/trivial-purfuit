class Slices(object):
    def __init__(self):
        self._red = False
        self._green = False
        self._blue = False
        self._white = False

    @property
    def red(self):
        return self._red

    @property
    def green(self):
        return self._green

    @property
    def blue(self):
        return self._blue

    @property
    def white(self):
        return self._white

    @red.setter
    def red(self, red):
        self._red = red

    @green.setter
    def green(self, green):
        self._green = green

    @blue.setter
    def blue(self, blue):
        self._blue = blue

    @white.setter
    def white(self, white):
        self._white = white

    def get_slices_won(self):

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
