# 🎬 Movie Recommender System
### Content-Based Filtering · Streamlit · Python · Machine Learning

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-link.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0%2B-orange?logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

A **content-based movie recommender system** that suggests 5 similar movies based on a selected title. The model analyzes movie metadata — genres, keywords, cast, crew, and plot overview — to compute similarity scores using **cosine similarity** on vectorized text features.

Built end-to-end in **Google Colab** and deployed as a live web app using **Streamlit Community Cloud**.

> 🔗 **Live Demo:** [Click here to try the app](https://your-app-link.streamlit.app)

---

## 🖼️ Demo

| Select a Movie | Get Recommendations |
|---|---|
| Choose from 5000+ movies | Instantly see 5 similar picks with posters |

---

## 🧠 How It Works

```
Raw Data (TMDB 5000)
      ↓
Feature Extraction (genres + keywords + cast + crew + overview)
      ↓
Text Preprocessing (lowercasing + stemming with PorterStemmer)
      ↓
Vectorization (CountVectorizer, top 2000 features)
      ↓
Cosine Similarity Matrix (5000 × 5000)
      ↓
Top 5 Similar Movies → Fetch Posters via TMDB API
      ↓
Streamlit Web App
```

---

## 🗂️ Dataset

- **Source:** [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) (Kaggle)
- **Files used:**
  - `tmdb_5000_movies.csv` — movie metadata (genres, keywords, overview, etc.)
  - `tmdb_5000_credits.csv` — cast and crew information
- **Size:** ~5000 movies after cleaning

---

## 🏗️ Project Structure

```
movie-recommender/
│
├── app.py                  # Streamlit web application
├── movies.pkl              # Preprocessed movie dataframe (pickled)
├── similarity.pkl          # Cosine similarity matrix (pickled)
├── requirements.txt        # Python dependencies
├── Movie_Recommender.ipynb # Full Google Colab notebook
└── README.md
```

---

## ⚙️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.9+ |
| Data Processing | Pandas, NumPy |
| NLP & ML | Scikit-learn, NLTK (PorterStemmer) |
| Vectorization | CountVectorizer (Bag of Words) |
| Similarity | Cosine Similarity |
| Web App | Streamlit |
| Poster API | TMDB API |
| Deployment | Streamlit Community Cloud |
| Development | Google Colab |

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/movie-recommender.git
cd movie-recommender
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python -m streamlit run app.py
```

The app will open at `http://localhost:8501`

> **Note:** `movies.pkl` and `similarity.pkl` must be present in the root folder. If missing, run the Colab notebook to regenerate them.

---

## 📓 Rebuild the Model (Google Colab)

If you want to retrain or modify the model:

1. Open `Movie_Recommender.ipynb` in [Google Colab](https://colab.research.google.com)
2. Upload your `kaggle.json` API key
3. Run all cells top to bottom
4. Download the generated `movies.pkl` and `similarity.pkl`
5. Place them in the project root and run the app

---

## 🔍 Feature Engineering Details

The model builds a unified `tags` field for each movie by combining:

| Feature | Example |
|---|---|
| Overview | `"a thief who steals corporate secrets..."` |
| Genres | `Action`, `Science Fiction`, `Thriller` |
| Keywords | `based on novel`, `dystopia`, `artificial intelligence` |
| Top 3 Cast | `Leonardo DiCaprio`, `Joseph Gordon-Levitt` |
| Director | `Christopher Nolan` |

All tags are **lowercased** and **stemmed** (e.g., `loving → love`) before vectorization to reduce vocabulary noise.

---

## 🧪 Example

**Input:** `Inception`

**Output:**
| # | Recommended Movie |
|---|---|
| 1 | The Dark Knight Rises |
| 2 | Interstellar |
| 3 | The Prestige |
| 4 | Memento |
| 5 | Batman Begins |

---

## 📦 Requirements

```
streamlit
pandas
numpy
scikit-learn
nltk
requests
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 🌐 Deployment

This app is deployed for free on **Streamlit Community Cloud**:

1. Push all files to a public GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set main file as `app.py`
5. Click **Deploy** — live in ~3 minutes

---

## 🙋 FAQ

**Q: Why content-based and not collaborative filtering?**  
A: Content-based filtering works without user interaction data (ratings, watch history). It's ideal for cold-start scenarios and works purely on movie metadata.

**Q: Why is similarity.pkl large?**  
A: It stores a 5000×5000 float matrix. Reducing `max_features` in CountVectorizer from 5000 to 2000 shrinks it significantly with minimal accuracy loss.

**Q: Can I add more movies?**  
A: Yes — update the dataset, rerun the Colab notebook, and replace the pkl files.

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 🙌 Acknowledgements

- [TMDB](https://www.themoviedb.org/) for the dataset and poster API
- [Kaggle](https://www.kaggle.com/) for hosting the dataset
- [Streamlit](https://streamlit.io/) for the free deployment platform
- [CampusX](https://www.youtube.com/@campusx-official) for ML project inspiration

---

## 👤 Author

**Your Name**  
[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-black?logo=github)](https://github.com/YOUR_USERNAME)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/YOUR_PROFILE)

---

*If you found this project helpful, please consider giving it a ⭐ on GitHub!*
