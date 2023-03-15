from collections import Counter

all_people = [{'name': 'Reuven', 'age': 50, 'hobbies': ['Python', 'cooking', 'reading']},
              {'name': 'Atara', 'age': 20, 'hobbies': ['horses', 'cooking', 'art', 'reading']},
              {'name': 'Shikma', 'age': 18, 'hobbies': ['Python', 'piano', 'cooking', 'reading']},
              {'name': 'Amotz', 'age': 15, 'hobbies': ['boxing', 'cooking']}]


def average_age_under(people, limit):
    return sum([one_person['age']
                for one_person in people
                if one_person['age'] >= 1 and
                one_person['age'] <= limit]) / len(people)


def all_hobbies(people):
    return set(one_hobby
               for one_person in people
               for one_hobby in one_person['hobbies'])


def hobby_counter(people):
    return Counter([one_hobby
                    for one_person in people
                    for one_hobby in one_person['hobbies']])


def n_most_common(people, n):
    return [one_tuple[0] for one_tuple in hobby_counter(people).most_common(n)]