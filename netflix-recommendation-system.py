# Import necessary libraries
import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
data = pd.read_csv('path/to/your/netflixData.csv')

# Select relevant columns
data = data[["Title", "Description", "Genres", "Content Type"]]

import nltk
import re
nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
from nltk.corpus import stopwords
import string 
stop_words = set(stopwords.words('english'))

# Function to clean text data
def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    
    text = [word for word in text.split(' ') if word not in stop_words]
    text = " ".join(text)
    return text

# Apply the cleaning function to the Title column
data["Title"] = data["Title"].apply(clean)
print(data.Title.sample(10))

# Prepare the TF-IDF matrix
feature = data['Genres'].tolist()
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(feature)
similarity = cosine_similarity(tfidf_matrix)
indices = pd.Series(data.index, index = data['Title']).drop_duplicates()

# Function to recommend movies based on title
def netflix_recommendation(title):
    if title not in indices:
        return "Title not found in the dataset."

    index = indices[title]
    sig_scores = list(enumerate(similarity[index]))
    sig_scores = sorted(sig_scores, key = lambda x: x[1], reverse = True)
    sig_scores = sig_scores[1:11]
    movies_indices = [i[0] for i in sig_scores]
    return data['Title'].iloc[movies_indices]

# Example recommendation
print(netflix_recommendation("alive"))
