"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
from pathlib import Path

# Importing markdowns
def read_markdown_file(markdown_file):
	return Path(markdown_file).read_text()

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Homepage", "Recommender System", "Information", "Solution Overview", "About Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------

    # Building out the "Homepage" page
    if page_selection == "Homepage":
        st.write('# RR3 Movies :film_frames:')
        st.write('### Entertainment to ease off the stress')
        st.image('resources/imgs/movies_01.jpg', use_column_width=True)
        info_markdown = read_markdown_file("resources/info_01.md")
        st.markdown(info_markdown)
        st.subheader("   ")# just a way to create space between texts
        st.subheader("   ")
        st.write("Navigate through the app with the side bar...")

    # Building out the "Information" page
    if page_selection == "Information":
        options = ["General Information", "EDA", "Model Information"]
        selection = st.sidebar.selectbox("What do you want to know?", options)

        if selection == "General Information":
            st.info("General Information")
            info_markdown = read_markdown_file("resources/info_02.md")
            st.markdown(info_markdown)

        if selection == "EDA":
            st.info("Exploratory Data Analysis")
            st.write('## Some cool insights we got from the data')
            st.subheader('Rating Frequency')
            st.image('resources/imgs/EDA1.png', width = 600)
            st.write('The bar plot indicates most common ratings used are 4.0, 5.0, 3.0, and 3.5. \
                     This means that most reviews are relatively positive and this can skew \
                     recommendations as most ratings end up being highly positive. \
                     This may indicate that collaborative model may not be as useful as content \
                     based model because content based models do not rely on ratings but rather \
                     shared characteristics of different items (such as genre for movies).')
            st.subheader("")# creating space between the texts and images
            st.subheader("")# creating space between the texts and images

            st.subheader('Average Rating')
            st.image('resources/imgs/EDA2.png', width = 600)
            st.write('The average rating in the dataset hovers just below 4 and shows that \
                     ratings for movies are most commonly in the more positive range. \
                     This further buttresses our previous sentiment.')
            st.subheader("")# creating space between the texts and images
            st.subheader("")# creating space between the texts and images

            st.subheader('Average number of movies rated')
            st.image('resources/imgs/EDA3.png', width = 600)
            st.write('Majority of movies have been rated a fewer times and ends up skewing the\
                      dataset to the right. This may mean that majority of the dataset\'s movies \
                     have average ratings that may not represent the true valuation of the movies \
                     because a sample size of less than 10 ratings may not indicate the general \
                     human population\'s rating of the movie if it has been seen by more people \
                     than those who have given a rating.')
            st.subheader("")# creating space between the texts and images
            st.subheader("")# creating space between the texts and images

            st.subheader('Ten(10) most popular movies')
            st.image('resources/imgs/EDA4.png', width = 550)
            st.write('Here we can see the number of ratings for specific movies which happens to \
                     be the most popular for the dataset, this gives us a good start for movies \
                     we can recommend to users based on the amount of rates by users')

        if selection == "Model Information":
            st.info("Model Information")
            st.image('resources/imgs/Modela.jpg', width = 800)
            info_markdown = read_markdown_file("resources/info_03.md")
            st.markdown(info_markdown)

    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # Building out the 'About us' page
    if page_selection == "About Us":
        st.info("About Us")
        st.image('resources/imgs/tech_team_01.jpg', width= 700)
        st.subheader("`Mission Statement:`:page_with_curl::page_with_curl:")
        st.subheader("At RR3 Tech:registered:, we specialize in transforming challenges into\
					growth opportunities. With a focus on innovation and expertise, we help\
					companies thrive in today's dynamic business landscape. Harnessing the\
					power of advanced technology and data-driven insights, we provide tailored\
					solutions that drive remarkable results.")
        st.subheader("We pride ourselves in applying the latest technology to provide actionable intel,\
					in turn helping businesses to grow and nurture a consumer-first mindset.")
        st.subheader("   ")# just a way to create space between texts
        st.subheader("   ")
        st.subheader("`Meet The Team:`:male-technologist::female-factory-worker:")
        st.subheader("   ")
		
		# First Member
        st.image('resources/imgs/Greensmill.jpg', width = 300)
        st.subheader('Greensmill Emmanuel')
        st.write('#### Data Scientist:', '`Team Lead`')
        st.subheader("   ")

        # Second Member
        st.image('resources/imgs/Brigette.jpg', width = 300)
        st.subheader('Siphosethu Matomela')
        st.write('#### Data Scientist:', '`Admin Lead`')
        st.subheader("   ")

        # Third Member
        st.image('resources/imgs/Buchi.jpeg', width = 300)
        st.subheader('Onyebuchi Madubuko')
        st.write('#### Data Scientist:', '`Tech Lead`')
        st.subheader("   ")

        # Fourth Member
        st.image('resources/imgs/Onyeka1.jpeg', width = 300)
        st.subheader('Onyeka Ekesi')
        st.write('#### Data Scientist:', '`Asst. Tech Lead`')
        st.subheader("   ")

        # Fifth Member
        st.image('resources/imgs/Tebatso1.jpg', width = 300)
        st.subheader('Tebatso Malotane')
        st.write('#### Data Scientist:', '`Product Lead`')
        st.subheader("   ")


if __name__ == '__main__':
    main()
