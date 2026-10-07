from src.llm.groq_client import ask_llm
from src.prompts.movie_prompts import (
    build_movie_analysis_prompt,
    build_movie_question_prompt,
)


def analyze_movie(movie_context: dict) -> str:
    """Generate an AI analysis for a selected movie or series."""

    movie_title = movie_context["title"]

    prompt = build_movie_analysis_prompt(
        movie_title=movie_title,
        movie_context=movie_context,
    )

    return ask_llm(prompt)


def ask_about_movie(
    movie_context: dict,
    question: str,
    spoiler_level: str = "No Spoilers",
) -> str:
    """Answer a user's question about the selected movie or series."""

    movie_title = movie_context["title"]

    prompt = build_movie_question_prompt(
        movie_title=movie_title,
        movie_context=movie_context,
        question=question,
        spoiler_level=spoiler_level,
    )

    return ask_llm(prompt)