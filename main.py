import os
from fastapi import FastAPI, HTTPException
from utils import (
    tle
)
from dotenv import load_dotenv

load_dotenv()

N2YO_API_KEY = os.getenv('N2YO_API_KEY')
N2YO_USER = os.getenv('N2YO_USER')
URL = 'https://api.n2yo.com/rest/v1/satellite/'
TLE = '/tle/{id}'
SATELLITE_POSITIONS = '/positions/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{seconds}'
VISUAL_PASSES = '/visualpasses/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{days}/{min_visibility}'
RADIO_PASSES = '/visualpasses/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{days}/{min_visibility}'
# Galileo Id = 22

id=22
tle(URL+f'tle/{id}544&apiKey='+N2YO_API_KEY, N2YO_USER, N2YO_API_KEY)

# app = FastAPI()

# @app.get("/ny2c/tle", tags=['TLE'])
# async def tle() -> JSONResponse:
