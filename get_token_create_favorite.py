import requests

TEST_URL = "https://regions-test.2gis.com"

def get_token():
    resp = requests.post(f"{TEST_URL}/v1/auth/tokens")
    resp.raise_for_status()
    cookie_header = resp.headers.get("Set-Cookie")
    token = cookie_header.split("token=")[1].split(";")[0]
    return {"token": token}

def create_favorite(data, cookies):
    return requests.post(f"{TEST_URL}/v1/favorites", data=data, cookies=cookies)