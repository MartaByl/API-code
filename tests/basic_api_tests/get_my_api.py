import requests
import pytest


@pytest.fixture(scope="module")
def myip():
    response = requests.get("https://api.ipify.org/?format=json")
    return response


def test_myip_response_code_is_200(myip):
    assert myip.status_code == 200


def test_myip_request_has_a_body(myip):
    data = myip.json()
    assert data is not None
    assert data["ip"] is not None


def test_myip_request_has_json_header(myip):
    assert myip.headers["Content-Type"] == "application/json"
