import streamlit as st
import pickle
import requests

# def fetch_poster(movie_id):
movie_new = pickle.load((open('movies.pkl','rb')))
movie_list = movie_new['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(option):
    i = movie_new[movie_new['title'] == option].index[0]
    distance = similarity[i]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        #fetch the movie poster using API
        recommended_movies.append(movie_new.iloc[i[0]].title)
    return recommended_movies


st.title("Movie Recommender System")
option = st.selectbox(
'Select your movie',
(movie_list))

if st.button("Predict", type="primary"):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)


st.write('You selected:', option)