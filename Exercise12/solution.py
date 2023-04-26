import random

class RandMemory(object):
    def __init__(self, lowest, highest):
        self.lowest = lowest
        self.highest = highest
        self._history = []

    @property
    def get(self):
        number = random.randint(self.lowest, self.highest)
        self._history.append(number)
        return number

    def history(self):
        return self._history
