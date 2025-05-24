import requests
from requests.auth import HTTPBasicAuth

def tle(URL: str, N2YO_USER: str, N2YO_API_KEY: str):
    """
    """
    basic = HTTPBasicAuth(N2YO_USER, N2YO_API_KEY)

    r = requests.get(url=URL, auth=basic)
    print(r.content)

def satellite_positions(URL: str, N2YO_USER: str, N2YO_API_KEY: str):
    """
    """
    basic = HTTPBasicAuth(N2YO_USER, N2YO_API_KEY)

    r = requests.get(url=URL, auth=basic)
    print(r)

def visual_passes(URL: str, N2YO_USER: str, N2YO_API_KEY: str):
    """
    """
    basic = HTTPBasicAuth(N2YO_USER, N2YO_API_KEY)

    r = requests.get(url=URL, auth=basic)
    print(r)

def radio_passes(URL: str, N2YO_USER: str, N2YO_API_KEY: str):
    """
    """
    basic = HTTPBasicAuth(N2YO_USER, N2YO_API_KEY)

    r = requests.get(url=URL, auth=basic)
    print(r)
