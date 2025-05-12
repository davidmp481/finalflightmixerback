import os
import httpx

async def search_flights(payload: dict):
    url = "https://api.flightapi.io/api/v1/searchMultiCityFlights"
    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
