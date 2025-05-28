import json
import requests
from requests.auth import HTTPBasicAuth

async def tle(URL: str, N2YO_USER: str, N2YO_API_KEY: str):
    """
    Function to call TLE API 
    """
    basic = HTTPBasicAuth(N2YO_USER, N2YO_API_KEY)

    response = requests.get(url=URL, auth=basic)
    content = json.loads(response.content)

    return content

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
