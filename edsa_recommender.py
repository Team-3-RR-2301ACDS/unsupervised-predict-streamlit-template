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
    page_options = ["Recommender System","Solution Overview"]

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
        st.write('### Entertainment to eaze off the stress')
        st.image('resources/imgs/movies_01.jpg', use_column_width=True)
        st.subheader("Welcome to RR3 Movies:registered:  :man-raising-hand:")
        st.subheader("your favorite № 1 Movie Recommender")
        st.subheader("   ")# just a way to create space between texts
        st.subheader("   ")
        st.write("Navigate through the app with the side bar...")

    # Building out the "Information" page
    if page_selection == "Information":
        options = ["make your choice here ↓", "General Information", "EDA", "Model Information"]
        selection = st.sidebar.selectbox("What do you want to know?", options)

        if selection == "make a choice here ↓":
            st.image('resources/imgs/info_page.jpg', width=500)
            st.subheader("What kind of info do you need :question:")
            st.subheader(":arrow_upper_left: Make your choice from the side bar")

        if selection == "General Information":
            st.info("General Information")

        if selection == "EDA":
            st.info("Exploratory Data Analysis")
            st.write('## Some cool insights we got from the data')

        if selection == "Model Information":
            st.info("Model Information")

    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # Building out the 'About us' page
	if selection == "About us":
			st.info("About Us")
			# Building out the 'about us' page
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
			st.image('resources/imgs/Mati.jpeg', width = 300)
			st.subheader('Greensmill Emmanuel')
			st.write('#### Data Scientist:', '`Team Lead`')
			
			st.subheader("   ")
			# Second Member
			st.image('resources/imgs/Buchi.jpeg', width = 300)
			st.subheader('Onyebuchi Madubuko')
			st.write('#### Data Scientist:', '`Tech Lead`')

			st.subheader("   ")
			# Third Member
			st.image('resources/imgs/Sumaya.jpeg', width = 300)
			st.subheader('Siphosethu Matomela')
			st.write('#### Data Scientist:', '`Admin Lead`')

			st.subheader("   ")
			# Fourth Member
			st.image('resources/imgs/Cinta.jpeg', width = 300)
			st.subheader('Onyeka Ekesi')
			st.write('#### Data Scientist:', '`Asst. Tech Lead`')

			st.subheader("   ")
			# Fifth Member
			st.image('resources/imgs/Bolanle.jpeg', width = 300)
			st.subheader('Tebatso Malotane')
			st.write('#### Data Scientist:', '`PR Lead`')

			st.subheader("   ")
			# Sixth Member
			st.image('resources/imgs/Omolaja.jpeg', width = 300)
			st.subheader('Wale Kolawole')
			st.write('#### Data Scientist')

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
