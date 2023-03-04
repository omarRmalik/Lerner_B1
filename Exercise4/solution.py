import arrow
import operator


class LogDicts:
    def __init__(self, filename):
        with open(filename, 'r') as infile:
            self.infile = infile.readlines()

    def dicts(self, key=None):
        if key is None:
            return [self.line_to_dict(line) for line in self.infile]
        else:
            return sorted([self.line_to_dict(line) for line in self.infile], key=key)

    def line_to_dict(self, line):
        if not line.strip():
            return {}

        ip_address = line.split()[0]

        timestamp_start = line.index('[') + 1
        timestamp_end = line.index(']')
        timestamp = line[timestamp_start:timestamp_end]

        request_start = line.index('"') + 1
        request_end = line[request_start:].index('"')
        request = line[request_start:request_start + request_end]

        return {'ip_address': ip_address,
                'timestamp': arrow.get(timestamp, 'DD/MMM/YYYY:HH:mm:ss', tzinfo='UTC'),
                'request': request}

    def iterdicts(self, key=None):
        if key is None:
            return iter(self.dicts(key=None))
        else:
            return iter(self.dicts(key=key))

    def earliest(self):
        return self.dicts(key=operator.itemgetter('timestamp'))[0]

    def latest(self):
        return self.dicts(key=operator.itemgetter('timestamp'))[-1]

    def for_ip(self, ip_address):
        output = []
        for one_dict in self.dicts():
            if one_dict['ip_address'] == ip_address:
                output.append(one_dict)
        return output

    def for_request(self, request):
        output = []
        for one_dict in self.dicts():
            if one_dict['request'] == request:
                output.append(one_dict)
        return output