import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os


# Google Drive file IDs
movie_dict_id = "1VimjrTkX7CNPytmuveClGnlG6CG72SQB"
movies_id = "17qnjGJF32d5-4jSD389CURKZWIxC32vG"
similarity_id = "1a6dTcpWSf2uMVwE8BHRMGKOvgbh1cYdZ"


# File names
movie_dict_file = "movie_dict.pkl"
movies_file = "movies.pkl"
similarity_file = "similarity.pkl"


# Download files if not already downloaded
if not os.path.exists(movie_dict_file):
    gdown.download(f"https://drive.google.com/uc?id={movie_dict_id}", movie_dict_file, quiet=False)

if not os.path.exists(movies_file):
    gdown.download(f"https://drive.google.com/uc?id={movies_id}", movies_file, quiet=False)

if not os.path.exists(similarity_file):
    gdown.download(f"https://drive.google.com/uc?id={similarity_id}", similarity_file, quiet=False)


# Load pickle files
movies_dict = pickle.load(open(movie_dict_file,'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open(similarity_file,'rb'))


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8dc4f087d16d2907c6481660ccbad2ee&language=en-US"
    
    response = requests.get(url)
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values
)

if st.button('Recommend'):

    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])