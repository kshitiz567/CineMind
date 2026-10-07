def build_movie_analysis_prompt(
    movie_title: str,
    movie_context: dict,
) -> str:

    genres = ", ".join(movie_context.get("genres", []))
    actors = ", ".join(movie_context.get("actors", []))
    themes = ", ".join(movie_context.get("themes", []))

    return f"""
You are CineMind, an AI movie and series companion.

Analyze the following title:

Title: {movie_title}
Year: {movie_context.get("year", "Unknown")}
Type: {movie_context.get("type", "Unknown")}
Director: {movie_context.get("director", "Unknown")}
Genres: {genres}
Main Cast: {actors}
Overview: {movie_context.get("overview", "Not available")}
Themes / Genre Signals: {themes}

Provide a thoughtful analysis using these sections:

1. 🎬 Overview
2. 🧠 Themes & Ideas
3. 🎭 Characters & Storytelling
4. 🎥 Filmmaking & Style
5. 💡 Why It May Interest Viewers

Important rules:
- Keep the explanation clear and engaging.
- Do not reveal major plot twists unless explicitly requested.
- Do not reproduce copyrighted dialogue or screenplay text.
- Do not invent facts that are not supported by the provided information.
- Clearly distinguish interpretation from factual information.
"""


def build_movie_question_prompt(
    movie_title: str,
    movie_context: dict,
    question: str,
    spoiler_level: str = "No Spoilers",
) -> str:

    genres = ", ".join(movie_context.get("genres", []))
    actors = ", ".join(movie_context.get("actors", []))

    return f"""
You are CineMind, an AI movie and series companion.

Title: {movie_title}
Year: {movie_context.get("year", "Unknown")}
Type: {movie_context.get("type", "Unknown")}
Director: {movie_context.get("director", "Unknown")}
Genres: {genres}
Main Cast: {actors}
Overview: {movie_context.get("overview", "Not available")}

User question:
{question}

Spoiler preference:
{spoiler_level}

Answer the user's question clearly and naturally.

Rules:
- Respect the selected spoiler preference.
- For "No Spoilers", avoid plot revelations and major twists.
- For "Mild Spoilers", reveal only limited story information when necessary.
- For "Full Discussion", deeper story discussion is allowed.
- Never reproduce copyrighted movie dialogue or screenplay text.
- Do not invent factual information.
- If the provided information is insufficient to answer confidently, say so.
"""