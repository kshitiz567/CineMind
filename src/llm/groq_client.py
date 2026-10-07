import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY was not found. "
        "Add it to your .env file."
    )

client = Groq(api_key=GROQ_API_KEY)

MODEL_NAME = "openai/gpt-oss-120b"


def ask_llm(
    question: str,
    system_prompt: str = (
        "You are CineMind, an AI movie and series companion. "
        "Give helpful, thoughtful and spoiler-aware answers. "
        "Do not reproduce copyrighted movie or TV dialogue."
    ),
) -> str:

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
        temperature=0.4,
        max_completion_tokens=500,
    )

    return response.choices[0].message.content