import requests
from prefect import flow


@flow
def test_request():
    response = requests.get("https://httpbin.org/get")
    print(response.json())
