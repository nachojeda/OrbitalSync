import os

from utils import (
    all_satellites
)

N2YO_API_KEY = os.getenv('N2YO_API_KEY')
N2YO_USER = os.getenv('N2YO_USER')
URL = 'https://api.n2yo.com/rest/v1/satellite/'

all_satellites(URL, N2YO_USER, N2YO_API_KEY)