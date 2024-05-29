import requests
import pytest


def get_neuromancer_data():
    response = requests.get("https://openlibrary.org/search.json?q=neuromancer")
    return response


print(get_neuromancer_data())
