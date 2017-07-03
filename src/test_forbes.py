"""Tests sourced from Erik Enderlein; Test for the flight path program."""

import pytest


data = [
    {
        "name": "Bill Gates",
        "age": 60,
        "rank": 1,
        "net_worth (USD)": 75000000000,
        "source": "Microsoft",
        "country": "United States"
    },
    {
        "name": "Amancio Ortega",
        "age": 80,
        "rank": 2,
        "net_worth (USD)": 67000000000,
        "source": "Zara",
        "country": "Spain"
    },
    {
        "name": "Warren Buffett",
        "age": 85,
        "rank": 3,
        "net_worth (USD)": 60800000000,
        "source": "Berkshire Hathaway",
        "country": "United States"
    },
    {
        "name": "Carlos Slim Helu",
        "age": 76,
        "rank": 1,
        "net_worth (USD)": 50000000000,
        "source": "telecom",
        "country": "Mexico"
    },
    {
        "name": "Jeff Bezos",
        "age": 52,
        "rank": 5,
        "net_worth (USD)": 45200000000,
        "source": "Amazon.com",
        "country": "United States"
    }
]

def test_search_rich_folks():
    """Tests the forbes function return oldest (80<) and youngest bn."""
    from forbes import search_rich_folks
    poop = print(search_rich_folks(data))
    assert search_rich_folks(data) == 'The oldest (under 80yo) billionaire is: Carlos Slim Helu\n    with a net worth of $50000000000\n    from the industry of: telecom\n    at the age of: 76.\n    The youngest billionaire is: Jeff Bezos\n    with a net worth of $45200000000\n    from the industry of: Amazon.com\n    at the age of: 52 years old.'
