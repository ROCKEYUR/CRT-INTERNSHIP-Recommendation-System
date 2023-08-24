import streamlit as st
import pickle
import pandas as pd
import requests
    
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list[0:10]:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetching poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommend System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)
    col9, col10 = st.columns(2)

    with st.container():
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

    with st.container():

        with col5:
            st.text(names[4])
            st.image(posters[4])

        with col6:
            st.text(names[5])
            st.image(posters[5])

        with col7:
            st.text(names[6])
            st.image(posters[6])

        with col8:
            st.text(names[7])
            st.image(posters[7])

    with st.container():
        with col9:
            st.text(names[8])
            st.image(posters[8])

        with col10:
            st.text(names[9])
            st.image(posters[9])

    # col1, col2, col3, col4, col5, col6 = st.columns(6)
    #
    # # Define the data for the first and second lines
    # line1_data = [(names[0], posters[0]), (names[1], posters[1]), (names[2], posters[2])]
    # line2_data = [(names[3], posters[3]), (names[4], posters[4]), (names[5], posters[5])]
    #
    # # Loop through the data and populate the columns
    # for col, (name, poster) in zip([col1, col2, col3], line1_data):
    #     with col:
    #         st.text(name)
    #         st.image(poster)
    #
    # for col, (name, poster) in zip([col4, col5, col6], line2_data):
    #     with col:
    #         st.text(name)
    #         st.image(poster)
