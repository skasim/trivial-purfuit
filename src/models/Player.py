from src.models.Slices import Slices


class Player(object):
    def __init__(self, name):
        self._name = name
        self._slices = Slices()

    @property
    def name(self):
        return self._name

    @property
    def slices(self):
        return self._slices

    @name.setter
    def name(self, name):
        self._name = name

    @slices.setter
    def slices(self, slices):
        self._slices = slices
