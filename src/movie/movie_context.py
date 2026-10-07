from src.movie.omdb_client import get_movie_details


def build_movie_context(movie_data: dict) -> dict:
    """Convert OMDb data into CineMind's internal movie context."""

    genres = [
        genre.strip()
        for genre in movie_data.get("Genre", "").split(",")
        if genre.strip()
    ]

    actors = [
        actor.strip()
        for actor in movie_data.get("Actors", "").split(",")
        if actor.strip()
    ]

    return {
    "title": movie_data.get("Title", "Unknown"),
    "year": movie_data.get("Year", "Unknown"),
    "type": movie_data.get("Type", "Unknown"),
    "genres": genres,
    "director": movie_data.get("Director", "Unknown"),
    "actors": actors,
    "overview": movie_data.get(
        "Plot",
        "No overview available."
    ),
    "themes": genres,
    "imdb_rating": movie_data.get(
        "imdbRating",
        "N/A"
    ),
    "poster": movie_data.get(
        "Poster",
        "N/A"
    ),
    "imdb_id": movie_data.get(
        "imdbID",
        ""
    ),
    "runtime": movie_data.get(
        "Runtime",
        "N/A"
    ),
    "language": movie_data.get(
        "Language",
        "N/A"
    ),
    "awards": movie_data.get(
        "Awards",
        "N/A"
    ),
    "total_seasons": movie_data.get(
        "totalSeasons",
        "N/A"
    ),
}


def get_movie_context(imdb_id: str) -> dict:
    """Fetch and prepare a movie/series from OMDb."""

    movie_data = get_movie_details(imdb_id)

    return build_movie_context(movie_data)