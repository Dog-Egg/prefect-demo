import requests
from prefect import flow


@flow(name="test_request", log_prints=True)
def test_request():
    response = requests.get("https://httpbin.org/get")
    print(response.json())
