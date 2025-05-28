import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

from utils import (
    tle
)

from models import (
    Response
)

load_dotenv()

N2YO_API_KEY = os.getenv('N2YO_API_KEY')
N2YO_USER = os.getenv('N2YO_USER')

if not N2YO_API_KEY or not N2YO_USER:
    raise ValueError("Missing required environment variables: N2YO_API_KEY and N2YO_USER")

BASE_URL = 'https://api.n2yo.com/rest/v1/satellite'

# TLE = '/tle/{id}'
# SATELLITE_POSITIONS = '/positions/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{seconds}'
# VISUAL_PASSES = '/visualpasses/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{days}/{min_visibility}'
# RADIO_PASSES = '/visualpasses/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{days}/{min_visibility}'
# Galileo Id = 22
# id=22544
# tle(URL+f'tle/{id}&apiKey='+N2YO_API_KEY, N2YO_USER, N2YO_API_KEY)

app = FastAPI()

@app.get("/ny2c/tle")
async def get_tle(id: int) -> Response:
    if id <= 0:
        raise HTTPException(status_code=400, detail="Satellite ID must be positive")
    
    try:
        url = f"{BASE_URL}/tle/{id}?apiKey={N2YO_API_KEY}"
        response = await tle(url, N2YO_USER, N2YO_API_KEY)
        return response
    except Exception as error:
        print(f"Error fetching TLE for satellite {id}: {error}")
        raise HTTPException(status_code=500, detail="Failed to fetch satellite TLE data")
