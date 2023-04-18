import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import altair as alt
from wordcloud import WordCloud, STOPWORDS
import glob, nltk, os, re
from nltk.corpus import stopwords
import random




st.markdown('''
# Analyzing Shakespeare Texts
''')


# Create a dictionary (not a list)
books = {" ":" ","A Mid Summer Night's Dream":"data/summer.txt","The Merchant of Venice":"data/merchant.txt","Romeo and Juliet":"data/romeo.txt"}


# Sidebar
st.sidebar.header('Word Cloud Settings')
max_word = st.sidebar.slider("Max Words",min_value=10, max_value=200, value=100, step=10)
max_font = st.sidebar.slider("Size of the largest Word", min_value=50, max_value=350, value=100, step=10)
image_width= st.sidebar.slider("Image Width", min_value=100, max_value=800, value=100, step=10)
random_state = st.sidebar.slider("Random State", min_value=20, max_value=100, value=100, step=1)
remove_stop_words = st.sidebar.checkbox("Remove Stop Words?",value=True)


st.sidebar.header('Word Count Settings')
min_count = st.sidebar.slider("Minimum count of words", min_value=5, max_value=100, value=100, step=5)




## Select text files
image = st.selectbox("Choose a text file", books.keys())


## Get the value
image = books.get(image)




if image != " ":
    stop_words = []
    raw_text = open(image,"r").read().lower()
    stop_words = stopwords.words('english')
   
    if remove_stop_words:
        stop_words = set(stop_words)
        stop_words.update(['us', 'one', 'though','will', 'said', 'now', 'well', 'man', 'may',
        'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
        'put', 'seem', 'asked', 'made', 'half', 'much',
        'certainly', 'might', 'came','thou'])
        # These are all lowercase
    tokens = nltk.word_tokenize(raw_text)



tab1, tab2, tab3 = st.tabs(['Word Cloud', 'Bar Chart', 'View Text'])


with tab1:
    st.write('These are some of the most common word in the book')
    if image is not None:
        cloud = WordCloud(background_color = "black",
                            max_words = max_word,
                            max_font_size=max_font,
                            stopwords = stop_words,
                            random_state=random)
        cloud.generate_from_text(' '.join(tokens))
        fig= plt.figure(figsize=(image_width/100, image_width/100), facecolor=None)
        plt.imshow(cloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(fig)


with tab2:
    st.write('This is word bar_chart')
           
   
with tab2:
    if image != " ":
        raw_text = open(image,"r").read().lower()
        st.write(raw_text)
