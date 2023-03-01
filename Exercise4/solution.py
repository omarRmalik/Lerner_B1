import re
from operator import itemgetter
import arrow

class LogDicts:
    def __init__(self, filename):
        with open(filename, 'r') as infile:
            self.infile = filename.read()

    def dicts(self, key=None):
        if key is None:
            return [self.line_to_dict(line) for line in self.infile]
        else:
            return sorted([self.line_to_dict(line) for line in self.infile], key=key)

    def line_to_dict(self,line):
        if not line.strip():
            return {}

        regexp = r'''
        ((?:\d{1,3}\.){3}\d{1,3})       # IP addresses contain four numbers (each with 1-3 digits)
        .*                              # Junk between IP address and timestamp
        \[([^\]]+)\]                    # Timestamp, defined to be anything between [ and ]
        .*                              # Junk between timestamp and request
        "(GET[^"]+)"                    # Request, starting with GET
        '''
        m = re.search(regexp, line, re.X)

        if m:
            ip_address = m.group(1)
            timestamp = m.group(2)
            request = m.group(3)

        else:
            ip_address = 'No IP address found'
            timestamp = 'No timestamp found'
            request = 'No request found'

        output = {'ip_address': ip_address,
                  'timestamp': timestamp,
                  'request': request}
        return output

    def iterdicts(self, key=None):
        if key is None:
            return iter(self.dicts(key=None))
        else:
            return iter(self.dicts(key=key))

    def earliest(self, key=None):
        pass

    def latest(self, key=None):
        pass

    def for_ip(self, ip_address, key=None):
        pass

    def for_request(self, text, key=None):
        pass


