#!usr/bin/env python3
"""This script fetches weather information for a specified
location using the wttr.in service."""

from fastapi import FastAPI
import uvicorn
import httpx

app = FastAPI()


@app.get("/")
async def read_root():
    """Root endpoint to welcome users."""
    return {"message": "Welcome to the Weather API"}


@app.get("/weather/{location}")
async def get_weather(location: str):
    """Fetch weather information for a specified location."""
    url = f"https://wttr.in/{location}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return {"lookup": location, "weather": response.text}
    return {"error": "Could not fetch weather information"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
