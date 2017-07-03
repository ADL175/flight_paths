import json
with open('forbes_data.json') as data_file:
    data = json.load(data_file)


def search_rich_folks(data=data):
    new_data = [element for element in data if element['net_worth (USD)'] > 1000000000 and element['age'] < 80 and element['age'] >= 1]
    min_bil = min(new_data, key=lambda d: d['age'])
    max_bil = max(new_data, key=lambda d: d['age'])
    print_max = print(
        "The oldest (under 80yo) billionaire is:  ", max_bil['name'],
        " with a net worth of $", max_bil['net_worth (USD)'],
        " from the industry of: ", max_bil['source'],
        " at the age of: ", max_bil['age'])
    print_min = print(
        "The youngest billionaire is:  ", min_bil['name'],
        " with a net worth of $", min_bil['net_worth (USD)'],
        " from the industry of: ", min_bil['source'],
        " at the age of: ", min_bil['age'])
    return print_max and print_min

if __name__ == '__main__':

    print(search_rich_folks())
