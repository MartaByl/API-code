import requests
import pytest


def test_lyric_author_data():
    response = requests.get("https://wolnelektury.pl/api/authors/cyprian-kamil-norwid/kinds/liryka/books/")
    data = response.json()
    assert data[0]["kind"] == "Liryka"


def test_epic_author_data():
    response = requests.get("https://wolnelektury.pl/api/authors/cyprian-kamil-norwid/kinds/epika/books/")
    data = response.json()
    assert data[0]["kind"] == "Epika"



def test_drama_author_data():
    response = requests.get("https://wolnelektury.pl/api/authors/cyprian-kamil-norwid/kinds/dramat/books/")
    data = response.json()
    assert data[0]["kind"] == "Dramat"


def test_painting_author_data():
    response = requests.get("https://wolnelektury.pl/api/authors/cyprian-kamil-norwid/kinds/malarstwo/books/")
    data = response.json()
    assert data [0] ["kind"] == "Malarstwo"
