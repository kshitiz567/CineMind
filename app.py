import streamlit as st

from src.movie.cinemind_engine import (
    analyze_movie,
    ask_about_movie,
)
from src.movie.movie_context import get_movie_context
from src.movie.omdb_client import search_movies


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="CineMind — AI Movie Companion",
    page_icon="🎬",
    layout="wide",
)


# -----------------------------
# Custom Styling
# -----------------------------

st.markdown(
    """<style>
.main-title {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 0.2rem;
}

.subtitle {
    font-size: 1.15rem;
    color: #6b7280;
    margin-bottom: 2rem;
}

.movie-card {
    padding: 1.5rem;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    background: #ffffff;
    margin-bottom: 1rem;
}

.section-title {
    font-size: 1.4rem;
    font-weight: 650;
    margin-top: 1rem;
    margin-bottom: 0.8rem;
}

.stButton > button {
    border-radius: 10px;
    font-weight: 600;
}

/* =========================
   CineMind Premium Header
   ========================= */

.cinemind-hero {
    padding: 2.2rem 2rem 2rem 2rem;
    margin: 0.5rem 0 2rem 0;
    text-align: center;
    border-radius: 24px;
    background:
        radial-gradient(
            circle at top left,
            rgba(99, 102, 241, 0.16),
            transparent 45%
        ),
        radial-gradient(
            circle at bottom right,
            rgba(168, 85, 247, 0.14),
            transparent 45%
        ),
        #f8fafc;
    border: 1px solid rgba(99, 102, 241, 0.12);
    box-shadow: 0 12px 35px rgba(15, 23, 42, 0.07);
}

.cinemind-badge {
    display: inline-block;
    padding: 0.4rem 0.85rem;
    margin-bottom: 0.9rem;
    border-radius: 999px;
    background: rgba(99, 102, 241, 0.09);
    color: #4f46e5;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.12em;
}

.cinemind-title {
    font-size: 3.2rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    color: #111827;
    line-height: 1.1;
}

.cinemind-subtitle {
    margin-top: 0.7rem;
    font-size: 1.25rem;
    font-weight: 600;
    color: #374151;
}

.cinemind-description {
    max-width: 680px;
    margin: 0.8rem auto 0 auto;
    font-size: 0.95rem;
    line-height: 1.6;
    color: #6b7280;
}

/* =========================
   Search Experience
   ========================= */

.search-heading {
    margin: 0.5rem 0 0.8rem 0;
}

.search-title {
    font-size: 1.25rem;
    font-weight: 750;
    color: #111827;
}

.search-subtitle {
    margin-top: 0.2rem;
    color: #6b7280;
    font-size: 0.9rem;
}

/* =========================
   Movie Details
   ========================= */

.section-label {
    margin: 0.5rem 0 1rem 0;
    color: #6366f1;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.16em;
}

.movie-title {
    margin-top: 0.5rem;
    font-size: 2.4rem;
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -0.035em;
    color: #111827;
}

.movie-meta {
    margin-top: 0.55rem;
    color: #6b7280;
    font-size: 0.95rem;
    font-weight: 600;
}

.movie-overview {
    margin: 1.2rem 0 1.5rem 0;
    padding: 1.15rem;
    border-left: 4px solid #6366f1;
    border-radius: 0 12px 12px 0;
    background: #f8fafc;
    color: #475569;
    line-height: 1.7;
    font-size: 0.98rem;
}

/* =========================
   AI Analysis
   ========================= */

.ai-result-header {
    margin-top: 1.5rem;
    margin-bottom: 1rem;
    padding: 0.65rem 0.9rem;
    border-radius: 10px;
    background: #eef2ff;
    color: #4f46e5;
    font-size: 0.75rem;
    font-weight: 800;
    letter-spacing: 0.12em;
}

/* =========================
   Ask CineMind
   ========================= */

.question-box {
    padding: 1rem;
    border-radius: 14px;
    background: #f8fafc;
    border: 1px solid #e5e7eb;
}

/* =========================
   Explore Cards
   ========================= */

.info-card {
    min-height: 90px;
    padding: 1rem 1.1rem;
    margin-bottom: 0.8rem;
    border-radius: 14px;
    background: #f8fafc;
    border: 1px solid #e5e7eb;
}

.info-label {
    margin-bottom: 0.4rem;
    color: #6366f1;
    font-size: 0.7rem;
    font-weight: 800;
    letter-spacing: 0.12em;
}

.info-value {
    color: #1f2937;
    font-size: 0.95rem;
    font-weight: 600;
    line-height: 1.5;
}

.awards-card {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 1.2rem;
    border-radius: 16px;
    background: linear-gradient(
        135deg,
        #fffbeb,
        #fef3c7
    );
    border: 1px solid #fde68a;
}

.awards-icon {
    font-size: 1.8rem;
}

.awards-text {
    color: #78350f;
    line-height: 1.6;
    font-size: 0.95rem;
}
</style>""",
    unsafe_allow_html=True,
)


# -----------------------------
# Header
# -----------------------------

with st.container():
    _, center, _ = st.columns([1, 3, 1])

    with center:
        st.caption("✦ AI MOVIE & SERIES COMPANION")

        st.title("🎬 CineMind")

        st.subheader(
            "Discover stories. Explore characters. "
            "Get smarter movie insights."
        )

        st.write(
            "Search any movie or series and unlock "
            "AI-powered analysis, spoiler-aware answers, "
            "cast insights and more."
        )


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:
    st.header("🎯 CineMind Controls")

    # -----------------------------
    # Movie / Series Search
    # -----------------------------

    if "search_results" not in st.session_state:
        st.session_state.search_results = []

    if "selected_imdb_id" not in st.session_state:
        st.session_state.selected_imdb_id = None

    st.markdown("**🔎 Find something to watch**")
    st.caption("Search movies and series by title")

    search_col1, search_col2 = st.columns([4, 1])

    with search_col1:
        search_query = st.text_input(
            "Search",
            placeholder="Try Interstellar, Stranger Things, Dune...",
            label_visibility="collapsed",
        )

    with search_col2:
        search_clicked = st.button(
            "🔍 Search",
            type="primary",
            width="stretch",
        )

    search_query = search_query.strip()

    if search_clicked and search_query:

        try:
            st.session_state.search_results = search_movies(
                search_query
            )

            st.session_state.selected_imdb_id = None

        except Exception as e:
            st.error(f"Search failed: {e}")

    # -----------------------------
    # Search Results
    # -----------------------------

    search_results = st.session_state.search_results

    selected_imdb_id = st.session_state.selected_imdb_id

    if search_results:

        selected_result = st.selectbox(
            "Select a title",
            search_results,
            format_func=lambda movie: (
                f"{movie['Title']} ({movie['Year']})"
            ),
        )

        selected_imdb_id = selected_result["imdbID"]

        st.session_state.selected_imdb_id = selected_imdb_id

    spoiler_level = st.selectbox(
        "Spoiler preference",
        [
            "No Spoilers",
            "Mild Spoilers",
            "Full Discussion",
        ],
    )

    st.divider()

    st.caption(
        "CineMind uses an LLM to analyze movies "
        "and answer natural-language questions."
    )


# -----------------------------
# Load Selected Movie
# -----------------------------

movie = None

if selected_imdb_id:
    try:
        movie = get_movie_context(selected_imdb_id)
    except Exception as e:
        st.error(f"Could not load movie details: {e}")


# -----------------------------
# Movie Information
# -----------------------------

if not movie:

    with st.container(border=True):
        _, center, _ = st.columns([1, 2, 1])

        with center:
            st.header("🎬")
            st.subheader("Welcome to CineMind")
            st.write(
                "Search for any movie or series to explore "
                "its story, themes, cast and AI-powered insights."
            )
            st.caption("Powered by OMDb + Groq")

    st.stop()


# -----------------------------
# Selected Movie Details
# -----------------------------

st.caption("NOW EXPLORING")

detail_col1, detail_col2 = st.columns(
    [1, 2.4],
    gap="large",
)

# -----------------------------
# Poster
# -----------------------------

with detail_col1:

    poster = movie.get("poster", "N/A")

    if poster and poster != "N/A":
        st.image(
            poster,
            width="stretch",
        )
    else:
        st.info("Poster unavailable.")


# -----------------------------
# Main Movie Information
# -----------------------------

with detail_col2:

    st.title(movie["title"])

    st.write(
        f"{movie['year']}  •  "
        f"{movie['type'].title()}  •  "
        f"⭐ {movie['imdb_rating']}"
    )

    st.write(movie["overview"])

    st.markdown("### 🎬 Title Details")

    info_col1, info_col2 = st.columns(2)

    with info_col1:
        st.write(
            f"**Director**  \n{movie['director']}"
        )

        st.write(
            f"**Genres**  \n{', '.join(movie['genres'])}"
        )

    with info_col2:
        st.write(
            f"**Runtime**  \n{movie.get('runtime', 'N/A')}"
        )

        st.write(
            f"**Language**  \n{movie.get('language', 'N/A')}"
        )


st.divider()


# -----------------------------
# Tabs
# -----------------------------

tab1, tab2, tab3 = st.tabs(
    [
        "🧠 AI Analysis",
        "💬 Ask CineMind",
        "🔎 Explore",
    ]
)


# -----------------------------
# AI Analysis
# -----------------------------
 
with tab1:
 
    st.subheader("AI Movie Analysis")
 
    st.write(
        "CineMind analyzes the title's themes, storytelling, "
        "characters and filmmaking style."
    )
 
    # -----------------------------
    # Quick Take
    # -----------------------------
 
    st.markdown("### ⚡ Quick Take")
 
    quick_col1, quick_col2, quick_col3 = st.columns(3)
 
    with quick_col1:
        st.metric(
            "Release Year",
            movie["year"],
        )
 
    with quick_col2:
        st.metric(
            "IMDb Rating",
            movie["imdb_rating"],
        )
 
    with quick_col3:
        st.metric(
            "Type",
            movie["type"].title(),
        )
 
    # -----------------------------
    # Genres
    # -----------------------------
 
    st.markdown("### 🎭 Genres")
 
    genre_text = "  •  ".join(movie["genres"])
 
    st.info(
        genre_text
    )
 
    # -----------------------------
    # AI Analysis
    # -----------------------------
 
    st.markdown("### 🧠 CineMind Intelligence")
 
    st.write(
        "Generate an AI-powered analysis based on the "
        "available movie information."
    )
 
    if st.button(
        "✨ Analyze Movie",
        type="primary",
        width="stretch",
    ):
 
        with st.spinner(
            "CineMind is analyzing the movie..."
        ):
 
            try:
 
                analysis = analyze_movie(movie)
 
                st.subheader("✦ CINE MIND INSIGHT")
 
                st.write(analysis)
 
            except Exception as e:
 
                st.error(
                    f"Something went wrong: {str(e)}"
                )


# -----------------------------
# Ask CineMind
# -----------------------------

with tab2:
    st.markdown("### 💬 Ask CineMind")

    st.write(
        "Choose a suggested question or ask your own."
    )

    suggested_questions = [
        "What are the main themes of this title?",
        "What makes this title interesting?",
        "What should I know before watching it?",
        "What kind of viewer might enjoy this?",
    ]

    selected_question = st.selectbox(
        "Suggested questions",
        ["Choose a question..."] + suggested_questions,
    )

    st.markdown(
        '<div class="section-title">'
        "Ask CineMind"
        "</div>",
        unsafe_allow_html=True,
    )

    question = st.text_area(
        "Your question",
        value=(
            ""
            if selected_question == "Choose a question..."
            else selected_question
        ),
        placeholder="Ask CineMind anything about this title...",
        height=120,
    )

    if st.button(
        "💬 Ask CineMind",
        type="primary",
        width="stretch",
    ):

        if not question.strip():
            st.warning(
                "Please enter a question first."
            )

        else:
            with st.spinner(
                "CineMind is thinking..."
            ):

                try:
                    answer = ask_about_movie(
                        movie_context=movie,
                        question=question,
                        spoiler_level=spoiler_level,
                    )

                    st.markdown("### 🤖 CineMind")
                    st.markdown(answer)

                except Exception as e:
                    st.error(
                        f"Something went wrong: {str(e)}"
                    )


# -----------------------------
# Explore
# -----------------------------
 
with tab3:
 
    st.subheader("Explore Movie Details")
 
    st.write(
        "Explore the cast, crew, technical details and "
        "recognition associated with this title."
    )
 
    # -----------------------------
    # Cast & Crew
    # -----------------------------
 
    st.markdown("### 🎭 Cast & Crew")
 
    crew_col1, crew_col2 = st.columns(2)
 
    with crew_col1:
        with st.container(border=True):
            st.caption("DIRECTOR")
            st.write(movie["director"])
 
    with crew_col2:
        with st.container(border=True):
            st.caption("MAIN CAST")
            st.write(", ".join(movie["actors"]))
 
    st.divider()
 
    # -----------------------------
    # Title Information
    # -----------------------------
 
    st.markdown("### 📊 Title Information")
 
    info_col1, info_col2, info_col3 = st.columns(3)
 
    with info_col1:
        with st.container(border=True):
            st.caption("RUNTIME")
            st.write(movie["runtime"])
 
    with info_col2:
        with st.container(border=True):
            st.caption("LANGUAGE")
            st.write(movie["language"])
 
    with info_col3:
        with st.container(border=True):
            st.caption("IMDb RATING")
            st.write(f"⭐ {movie['imdb_rating']}")
 
    # -----------------------------
    # Series Information
    # -----------------------------
 
    if movie["type"].lower() == "series":
 
        st.markdown("### 📺 Series Information")
 
        with st.container(border=True):
            st.caption("TOTAL SEASONS")
            st.write(movie["total_seasons"])
 
    st.divider()
 
    # -----------------------------
    # Awards
    # -----------------------------
 
    st.markdown("### 🏆 Awards & Recognition")
 
    st.success(f"🏆 {movie['awards']}")


# -----------------------------
# Footer
# -----------------------------

st.divider()

st.caption(
    "🎬 CineMind — AI Movie & Series Companion | "
    "Built with Python, Streamlit and Groq"
)