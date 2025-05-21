import os
import requests
from requests.auth import HTTPBasicAuth

N2YO_API_KEY = os.getenv('N2YO_API_KEY')
N2YO_USER = os.getenv('N2YO_USER')

def all_satellites():
    """
    """
    basic = HTTPBasicAuth(N2YO_USER, N2YO_API_KEY)

    URL = 'https://api.n2yo.com/rest/v1/satellite/'
    r = requests.get(url=URL, auth=basic)

    print(r.status_code)


all_satellites()