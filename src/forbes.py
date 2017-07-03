"""Searches JSON data for oldest and youngest bn-aires."""


import json
with open('forbes_data.json') as data_file:
    data = json.load(data_file)


def search_rich_folks(data=data):
    new_data = [element for element in data if element['net_worth (USD)'] > 1000000000 and element['age'] < 80 and element['age'] >= 1]
    min_bil = min(new_data, key=lambda d: d['age'])
    max_bil = max(new_data, key=lambda d: d['age'])
    print_max = """The oldest (under 80yo) billionaire is: {max_name}
    with a net worth of ${max_bill}
    from the industry of: {max_source}
    at the age of: {max_age}.
    The youngest billionaire is: {min_name}
    with a net worth of ${min_bill}
    from the industry of: {min_source}
    at the age of: {min_age} years old.""".format(
                         max_name=max_bil['name'],
                         max_bill=max_bil['net_worth (USD)'],
                         max_source=max_bil['source'],
                         max_age=max_bil['age'],
                         min_name=min_bil['name'],
                         min_bill=min_bil['net_worth (USD)'],
                         min_source=min_bil['source'],
                         min_age=min_bil['age']
                         )

    return print_max

if __name__ == '__main__':

    search_rich_folks()
