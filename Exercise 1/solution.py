from collections import Counter, defaultdict

visits = defaultdict(list)


# Collect places function

def collect_places():
    while True:
        place = input('Tell me where you went: ')
        if not place:
            break
        if "," not in place:
            print("That's not a legal city, country combination")
            continue
        city, country = place.strip().split(",")
        global visits
        visits[country].append(city)
    for key, value in sorted(visits.items()):
        visits[key] = sorted(value)


# Display places function

def display_places():
    counts_dict = defaultdict(dict)
    for key, value in visits.items():
        counts = Counter(value)
        for item, count in counts.items():
            if isinstance(item, str):
                counts_dict[key][item] = count

    output = 'You visited:\n'

    for key, value in counts_dict.items():
        output += f'{key}\n\t'
        for city, times in value.items():
            output += f'{city}\t ({times if times > 1 else 1})\n'
    return output