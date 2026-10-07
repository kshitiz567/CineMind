# 🎬 CineMind

### AI-Powered Movie & Series Companion

<p align="center">
  <b>Discover stories. Explore characters. Get smarter movie insights.</b>
</p>

<p align="center">
  CineMind combines real-time movie metadata with generative AI to help users explore movies and TV series through intelligent analysis, spoiler-aware conversations, and rich title insights.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM-F55036?style=for-the-badge)
![OMDb](https://img.shields.io/badge/OMDb-API-1F2937?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)

</p>

---

## 🌐 Live Application

> 🚀 **Try CineMind:**  
> Add your deployed Streamlit URL here.

<p align="center">

<a href="YOUR_STREAMLIT_URL">
<img src="https://img.shields.io/badge/🚀%20Open%20CineMind-Live%20Demo-6366F1?style=for-the-badge">
</a>

<a href="https://github.com/kshitiz567/CineMind">
<img src="https://img.shields.io/badge/⭐%20View%20Repository-GitHub-111827?style=for-the-badge&logo=github">
</a>

</p>

---

# 📌 Overview

**CineMind** is an AI-powered movie and series companion built with **Python, Streamlit, OMDb API and Groq-powered LLMs**.

Instead of simply displaying movie metadata, CineMind transforms that information into an interactive exploration experience.

Users can search for a movie or series and then:

- Explore detailed title information
- Generate AI-powered analysis
- Ask natural-language questions
- Control spoiler levels
- Explore cast and crew
- Inspect ratings, runtime, language and awards

The project demonstrates how **external APIs + structured application logic + generative AI** can be combined into a practical user-facing application.

---

# ✨ Key Features

| Feature | Description |
|---|---|
| 🔎 **Title Search** | Search movies and series using natural-language title queries |
| 🌐 **OMDb Integration** | Retrieve dynamic movie and series metadata |
| 🖼️ **Poster & Metadata** | Display posters, ratings, genres, runtime and more |
| 🧠 **AI Analysis** | Generate structured insights about themes, characters and filmmaking |
| 💬 **Ask CineMind** | Ask questions about the selected title |
| 🚫 **Spoiler Control** | Choose between No Spoilers, Mild Spoilers and Full Discussion |
| 🎭 **Cast & Crew** | Explore directors and major cast members |
| 🏆 **Awards** | View available awards and recognition |
| 📺 **Series Support** | Explore TV-series-specific information such as total seasons |
| ⚡ **Interactive UI** | Responsive Streamlit interface designed for exploration |



# 🖥️ Application Preview

## 🏠 Home & Search

<p align="center">
  <img src="images/home.png" width="900">
</p>

The CineMind home experience provides a focused search interface where users can quickly discover movies and TV series.



## 🧠 AI Movie Analysis

<p align="center">
  <img src="images/ai-analysis.png" width="900">
</p>

The AI Analysis layer transforms title metadata into structured insights covering themes, storytelling, characters, filmmaking style and viewing appeal.



## 🔍 Explore Title Details

<p align="center">
  <img src="images/explore.png" width="900">
</p>

The Explore section provides a deeper look into cast, crew, technical information, ratings, awards and series-specific metadata.



# 🧠 How CineMind Works


                    USER
                     │
                     ▼
             ┌───────────────┐
             │  Streamlit UI │
             └───────┬───────┘
                     │
              Search for Title
                     │
                     ▼
             ┌───────────────┐
             │    OMDb API   │
             └───────┬───────┘
                     │
              Movie / Series
                 Metadata
                     │
                     ▼
             ┌───────────────┐
             │ Movie Context │
             │   Builder     │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │ CineMind      │
             │ AI Engine     │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │  Groq LLM     │
             │ GPT-OSS 120B  │
             └───────┬───────┘
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
   AI Movie Analysis      Ask CineMind
          │                     │
          └──────────┬──────────┘
                     ▼
              Intelligent UI


---

# 🏗️ Architecture

CineMind follows a modular architecture that separates the application interface, movie data layer, prompt engineering, and LLM integration.


                         ┌──────────────────────┐
                         │        USER          │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Streamlit UI      │
                         │       app.py         │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      OMDb API        │
                         │ Movie / Series Data  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Movie Context      │
                         │      Builder         │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   CineMind Engine    │
                         │   Analysis + Q&A     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      Groq LLM        │
                         │    GPT-OSS 120B      │
                         └──────────┬───────────┘
                                    │
                         ┌──────────┴───────────┐
                         ▼                      ▼
                  AI Movie Analysis       Ask CineMind
                         │                      │
                         └──────────┬───────────┘
                                    ▼
                         ┌──────────────────────┐
                         │  Intelligent Output  │
                         └──────────────────────┘

### 🛠️ Tech Stack


Application
- Python
- Streamlit
Artificial Intelligence
- Groq API
- GPT-OSS 120B
- Prompt engineering
- Context-aware generation
Data & APIs
- OMDb API
- REST API integration
- JSON data processing
- requests
Development
- python-dotenv
- Git
- GitHub
- Virtual environments


### 👨‍💻 Author
Kshitiz
BCA Student | Data Analytics | AI / GenAI
Interested in building practical applications across:
Data Analytics • Artificial Intelligence • Generative AI • Software Development