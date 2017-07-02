"""Flight paths function sourced from Erik Enderlein."""

from graph import Graph  # flight paths will use graph and bellman_ford traversal
import json  # needed to utilize json
with open('src/cities_with_airports.json') as data_file:
    data = json.load(data_file)


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3  # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])


    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934  # convert km to miles


def flight_paths(city1, city2, data=data):
    """Function sourced from Erik Enderlein, function takes two city arguments and returns distance in miles and city connections."""
    cities_to_travel = Graph()  # instantiate a new graph
    location_dict = {}  # empty dictionary to hold city, location, and distances
    for city in data:  # creates dictionary of key cities, values: lat and long
        try:
            location_dict[city['city']]  # check if city is already in dictionary
        except KeyError:
            location_dict[city['city']] = city['lat_lon']  # add's city as key and it's lat/long as value
    for city in data:  # adds distances between each connected city
        for destination in city['destination_cities']:
            try:  # adding edge and weights (distances) between cities
                cities_to_travel.add_edge(city['city'], destination, calculate_distance(city['lat_lon'], location_dict[destination]))
            except KeyError:  # edge case; if connection already exists or points to city that doesn't have a lat/long
                pass
    try:
        to_return = cities_to_travel.bellman_ford(city1, city2)  # Bellman Ford shortest path through city
        if to_return[0] == float("inf"):
            raise KeyError("City does not exist")
        else:
            return to_return
    except KeyError:
        raise KeyError('City has no Lat or Long given, or does not exist')


if __name__ == '__main__':

    print(flight_paths("Sydney", "Calgary"))
