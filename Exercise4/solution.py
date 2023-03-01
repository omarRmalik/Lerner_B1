import re
from operator import itemgetter

class LogDicts:
    def __init__(self, filename):
        with open(filename, 'r') as infile:
            self.infile = filename.read()

    def dicts(self, key=None):
        pass

    def iterdicts(self, key=None):
        pass

    def earliest(self, key=None):
        pass

    def latest(self, key=None):
        pass

    def for_ip(self, ip_address, key=None):
        pass

    def for_request(self, text, key=None):
        pass


