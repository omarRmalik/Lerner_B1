from collections import namedtuple, Counter
from operator import itemgetter

Person = namedtuple('Person', ['first', 'last'])


class TableFull(Exception):
    pass


class GuestList(TableFull):
    def __init__(self):
        self.guest_list = []

    def assign(self, person, table_num):
        counter = Counter([table_count
                           for (person, table_count) in self.guest_list])
        if table_num in counter and counter[table_num] < 10:
            self.guest_list.append((person, table_num))
        elif table_num not in counter:
            self.guest_list.append((person, table_num))
        elif table_num in counter and counter[table_num] == 10:
            raise TableFull('There is no room at this table!')

    def table(self, table_num):
        return [person
                for (person, table_num) in self.guest_list
                if table_num == table_num]

    def unassigned(self):
        return [person
                for (person, table_num) in self.guest_list
                if table_num == None]

    def free_space(self):
        counter = Counter([table_count
                           for (person, table_count) in self.guest_list])
        return {key: 10 - value
                for key, value in counter.items()
                if value < 10 and key != None}

    def guests(self):
        return sorted([(one_guest, table_num)
                       for (one_guest, table_num) in self.guest_list
                       if table_num != None], key=lambda x: (x[1], x[0].last, x[0].first))

    def __repr__(self):
        guests = self.guests()
        table_strings = []
        for table_num in sorted(set([guest[1] for guest in guests])):
            table_string = f"{table_num}\n"
            table_guests = [guest for guest in guests if guest[1] == table_num]
            table_guests.sort(key=lambda x: (x[0].last, x[0].first))
            for guest in table_guests:
                table_string += f"{guest[0].last}, {guest[0].first}\n"
            table_strings.append(table_string)
        return '\n'.join(table_strings)