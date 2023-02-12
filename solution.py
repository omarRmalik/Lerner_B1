from collections import Counter, defaultdict
from operator import itemgetter

visits = defaultdict(list)

def collect_places():
  while True:
    place = input('Tell me where you went: ')
    if not place:
      break
    if "," not in place:
      print("That's not a legal city, country combination")
      continue
    city, country = place.strip().split(",")
    visits[country].append(city)
  return visits

def display_places():
  output = "You visited:\n"
  for key, value in visits.items():
    output += f'{key[1]}\n\t{key[0]}\t({value if value > 1 else None})\n'
  return output