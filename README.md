# Netflix-Recommedetion-System
A Netflix recommendation system based on genres. Uses TF-IDF Vectorization and Cosine Similarity to suggest similar titles. Helps users discover new content by calculating the similarity between Netflix titles. Built with Python, Pandas, Scikit-learn, and NLTK.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The Netflix Recommendation System uses a TF-IDF Vectorizer to transform genres into vectors and cosine similarity to find the most similar titles. This system helps users discover new content based on their interests.

## Features

- Clean and preprocess Netflix data
- Calculate similarity between titles based on genres
- Recommend similar titles for a given title

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/netflix-recommendation-system.git
    cd netflix-recommendation-system
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Download the dataset and place it in the project directory:
    - [Netflix Data](netflixData.csv)

## Usage

1. Ensure your dataset is in the specified path.
2. Run the script `netflix-recommendation-system.py` to see an example recommendation:
    ```sh
    python netflix-recommendation-system.py
    ```

3. Modify the script to input your own title:
    ```python
    title = "your title here"
    print(netflix_recommendation(title))
    ```

## Code

```python
# Import necessary libraries
import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import re
from nltk.corpus import stopwords
import string

# Download stopwords
nltk.download('stopwords')

# Load the data
data = pd.read_csv('path/to/your/netflixData.csv')

# Select relevant columns
data = data[["Title", "Description", "Genres", "Content Type"]]

# Initialize stopwords
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
```

##Contributing

Contributions are welcome! Please follow these steps to contribute:

    1.Fork the repository.
    2.Create a new branch (git checkout -b feature-branch).
    3.Commit your changes (git commit -m 'Add some feature').
    4.Push to the branch (git push origin feature-branch).
    5.Create a new Pull Request.

##License

This project is licensed under the MIT License. See the LICENSE file for details.
Contact

Feel free to reach out with any questions or suggestions:

    Email: your-email@example.com
    GitHub: your-username
