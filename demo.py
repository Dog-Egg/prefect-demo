# /// script
# dependencies = [
#     "nicely",
# ]
# ///

import requests
from prefect import flow


@flow(name="test_request", log_prints=True)
def test_request():
    import nicely

    response = requests.get("https://httpbin.org/get")
    print(response.json())
