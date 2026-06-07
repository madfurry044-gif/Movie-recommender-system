
import streamlit as st
import pickle
import pandas as pd
import requests

# ---------- Page config ----------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# ---------- Load model ----------
@st.cache_resource
def load_data():
    movies = pickle.load(open('movies.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

movies, similarity = load_data()

# ---------- Fetch poster from TMDB (optional) ----------
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8"
        data = requests.get(url).json()
        poster = data.get('poster_path', '')
        if poster:
            return "https://image.tmdb.org/t/p/w500" + poster
    except:
        pass
    return "https://via.placeholder.com/500x750?text=No+Poster"

# ---------- Recommend function ----------
def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[idx])),
        reverse=True,
        key=lambda x: x[1]
    )
    names, posters = [], []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return names, posters

# ---------- UI ----------
st.title("🎬 Movie Recommender System")
st.markdown("Select a movie and get 5 similar recommendations instantly.")

selected_movie = st.selectbox(
    "Type or select a movie:",
    movies['title'].values
)

if st.button("Get Recommendations"):
    with st.spinner("Finding similar movies..."):
        names, posters = recommend(selected_movie)

    st.subheader("You might also like:")
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.image(posters[i], use_column_width=True)
            st.caption(names[i])