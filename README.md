# Netflix-Recommedetion-System
A Netflix recommendation system based on genres. Uses TF-IDF Vectorization and Cosine Similarity to suggest similar titles. Helps users discover new content by calculating the similarity between Netflix titles. Built with Python, Pandas, Scikit-learn, and NLTK.

Features

    Cleans and preprocesses data.
    Uses TF-IDF vectorization for text data.
    Calculates cosine similarity between movies.
    Recommends movies based on a given title.

Installation

Clone the repository:

git clone https://github.com/your-username/netflix-recommendation-system.git
cd netflix-recommendation-system

Install the required libraries:

pip install numpy pandas scikit-learn nltk

Download NLTK stopwords:

import nltk
nltk.download('stopwords')

Usage

Ensure the dataset netflixData.csv is in the project directory.

Run the Python script:

python netflix_recommendation.py

    The script will print a list of recommended movie titles based on the given title.

Project Structure

├── netflix_recommendation.py
├── netflixData.csv
├── README.md
└── .gitignore
