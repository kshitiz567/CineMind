import os

import requests
from dotenv import load_dotenv


load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")

if not OMDB_API_KEY:
    raise ValueError(
        "OMDB_API_KEY was not found. "
        "Add it to your .env file."
    )

OMDB_URL = "https://www.omdbapi.com/"


def search_movies(query: str) -> list[dict]:
    if not query.strip():
        return []

    response = requests.get(
        OMDB_URL,
        params={
            "apikey": OMDB_API_KEY,
            "s": query.strip(),
            "type": "movie",
        },
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    if data.get("Response") == "False":
        return []

    return data.get("Search", [])


def get_movie_details(imdb_id: str) -> dict:
    if not imdb_id.strip():
        raise ValueError("IMDb ID cannot be empty.")

    response = requests.get(
        OMDB_URL,
        params={
            "apikey": OMDB_API_KEY,
            "i": imdb_id,
            "plot": "full",
        },
        timeout=10,
    )

    response.raise_for_status()

    data = response.json()

    if data.get("Response") == "False":
        raise ValueError(
            data.get("Error", "Movie not found.")
        )

    return data