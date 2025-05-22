import requests
from requests.auth import HTTPBasicAuth

def all_satellites(URL: str, N2YO_USER: str, N2YO_API_KEY: str):
    """
    """
    basic = HTTPBasicAuth(N2YO_USER, N2YO_API_KEY)

    r = requests.get(url=URL, auth=basic)
    print(r)
    print(r.status_code)