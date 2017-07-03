"""Tests sourced from Erik Enderlein; Test for the flight path program."""

import pytest


data = [
    {'city': 'city1', 'destination_cities': ['city2', 'city3'], 'lat_lon': [0, 0]},
    {'city': 'city2', 'destination_cities': ['city1'], 'lat_lon': [0, 0]},
    {'city': 'city3', 'destination_cities': ['city4', 'city2'], 'lat_lon': [0, 0]},
    {'city': 'city5', 'destination_cities': ['city6', 'city7'], 'lat_lon': [0, 0]}
]

PARAMS_TABLE = [
    ('city2', 'city3', [0, ['city2', 'city1', 'city3']]),
    ('city1', 'city2', [0, ['city1', 'city2']]),
]


@pytest.mark.parametrize("location1, location2, result", PARAMS_TABLE)
def test_flight(location1, location2, result):
    """Test to ensure that the correct path is chosen, not able to test for distances.
    """
    from flight_paths import track_path
    print(track_path(location1, location2, data))
    assert track_path(location1, location2, data) == result


def test_error_for_invalid_city():
    """Test if error raises for cities that do not have a given location."""
    from flight_paths import track_path
    with pytest.raises(KeyError):
        track_path('city1', 'city4', data)
    with pytest.raises(KeyError):
        track_path('city1', 'city5', data)
    with pytest.raises(KeyError):
        track_path('city12', 'city1', data)
