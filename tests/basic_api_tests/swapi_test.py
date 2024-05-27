import requests
import pytest


@pytest.fixture()
def get_han_solo_data():
    response = requests.get("https://swapi.dev/api/people/14")
    return response


def test_han_solo_is_in_empire_strikes_back(get_han_solo_data):
    data = get_han_solo_data.json()
    assert data["name"] == "Han Solo"
    assert "https://swapi.dev/api/films/2/" in data["films"]




