import requests
import csv

gist_url = ' https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json'


def cities_to_csv(url, filename):
    response = requests.get(url)

    if response.status_code == 200:
        infile = response.json()

        with open(filename, 'w', newline='') as outfile:
            file_writer = csv.writer(outfile, delimiter='\t')
            for one_dict in infile:
                file_writer.writerow([one_dict['city'], one_dict['state'], one_dict['rank'], one_dict['population']])
    else:
        print('Request failed with status code{response.status_code}')
