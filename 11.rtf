import requests
import pytest

#define base url
@pytest.fixture(scope="module")  
def base_url():
    return "https://petstore.swagger.io"

# authentication test
def test_authentication(base_url):  # test autentification
    response = requests.get(f"{base_url}/oauth/authorize", auth=("test", "abc123"))
    assert response.status_code == 200

#adding parametrize
@pytest.mark.parametrize("pet_id, name", [
    (1, "cat1"),  # valid pet_id with name cat1
    (2, "cat2"),  # valid pet_id with name cat2
    (3, "cat3"),  # valid pet_id with name cat3
    (4, "cat4"),  # valid pet_id with name cat4
])

# this test for checking add/put request
def test_put_endpoint(base_url, pet_id, name):
    payload = {"id": pet_id, "category": {"id": 4, "name": "mammal"},
               "name": name,
               "photoUrls": ["string"],
               "tags": [{"id": 6, "name": "dog"}],
               "status": "available"}
    url = f"{base_url}/v2/pet"
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, json=payload, headers=headers)
    assert response.status_code == 200, f"Failed with status {response.status_code}"
    assert response.json()["name"] == name, "Pet name does not match the request"

# this test for checking post request
def test_post_endpoint(base_url):
    payload = {"id": 1, "category": {"id": 1, "name": "string"},
               "name": "Kitty2",
               "photoUrls": ["string"],
               "tags": [{"id": 1, "name": "dog"}],
               "status": "available"}
    url = f"{base_url}/v2/pet"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == "Kitty2"

# example of checkins deleting of existed id
def test_delete_endpoint(base_url, pet_id, name):
    url = f"{base_url}/v2/pet/{pet_id}"
    response = requests.delete(url)
    assert response.status_code == 200

#adding parametrize for invalid ids
@pytest.mark.parametrize("incorrect_pet_id", [
    (-1),
    (99999999)
])

# example of checking invalid ids
def test_delete_negative_cases(base_url, incorrect_pet_id):
    url = f"{base_url}/v2/pet/{incorrect_pet_id}"
    response = requests.delete(url)
    assert response.status_code == 404, "Expected a 404 error with an invalid API key"


# esxeption handling
def test_delete_with_exception_handling(base_url, incorrect_pet_id):
    try:
        url = f"{base_url}/v2/pet/{incorrect_pet_id}"
        response = requests.delete(url)
        response.raise_for_status()
        assert response.status_code == 200, "Expected successful deletion status code"
    except requests.exceptions.HTTPError as e:
        assert response.status_code == 404, f"Expected 404 error but got {response.status_code}"
    except requests.exceptions.RequestException as e:
        pytest.fail(f"An unexpected error occurred: {e}")


##Validate response structure using a schema with the jsonschema library

from jsonschema import validate
schema = {
    "id": {"type": "integer"},
    "category": {
        "id": {"type": "integer"},
        "name": {"type": "string"}
    },
    "name": {"type": "string"},
    "photoUrls": {"type": "list"},
    "tags": {"type": "list"},
    "status": {"type": "string"}
}
response_data = {
    "id": 1,
    "category": {"id": 1, "name": "nameee"},
    "name": "Kitty2",
}

def test_response_schema():
    validate(instance=response_data, schema=schema)


## Create mock tests for each CRUD operation, simulating a successful
# and a failed GET, POST, PUT, and DELETE requests.
from unittest.mock import Mock


# Mock the get request to return a 500 server error
def test_get_pet_server_error(base_url, mocker):
    mocker.patch('requests.get', return_value=Mock(status_code=500))
    response = requests.get(f"{base_url}/v2/pet/1")
    assert response.status_code == 500, "Expected a 500 server error response"

# Mock the post request to simulate invalid data scenario
def test_post_pet_invalid_data(base_url, mocker):
    mocker.patch('requests.post', return_value=Mock(status_code=400, json=lambda: {"message": "Invalid data"}))
    payload = {"id": 1, "name": "", "photoUrls": ["string"]}
    response = requests.post(f"{base_url}/v2/pet", json=payload)
    assert response.status_code == 400
    assert response.json()["message"] == "Invalid data"


def test_put_pet_successful(base_url, mocker):
    mocker.patch('requests.put', return_value=Mock(status_code=200, json=lambda: {"id": 1, "name": "Buddy"}))
    payload = {"id": 1, "name": "Buddy", "photoUrls": ["string"]}
    response = requests.put(f"{base_url}/v2/pet", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Buddy"

def test_delete_pet_network_error(base_url, pet_id, mocker):
    # Simulate a 502 Bad Gateway error on DELETE request
    mocker.patch('requests.delete', return_value=Mock(status_code=502))
    url = f"{base_url}/v2/pet/{pet_id}"
    response = requests.delete(url)
    assert response.status_code == 502, "Expected a 502 Bad Gateway error response"
