import random

class RandMemory(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self._history = []

    @property
    def get(self):
        number = random.randint(self.start, self.stop)
        self._history.append(number)
        return number

    def history(self):
        return self._history

    def lowest(self):
        return min(self._history)

    def highest(self):
        return max(self._history)