from collections import Counter
from operator import itemgetter

visits = [ ]

def collect_places():
  while True:
    place = input('Tell me where you went: ')
    if not place:
      break
    if "," not in place:
      print("That's not a legal city, country combination")
      continue
    city, country = place.strip().split(",")
    visits.append((city, country))
  return visits

def display_places():
  sorted_places = sorted(visits, key = itemgetter(1,0))
  counted_places = Counter(sorted_places)
  output = "You visited:\n"
  for key, value in counted_places.items():
    output += f'{key[1]}\n\t{key[0]}\t({value})\n'
  return output