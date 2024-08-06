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
    
## Contributing

Contributions are welcome! Please follow these steps to contribute:

    1.Fork the repository.
    2.Create a new branch (git checkout -b feature-branch).
    3.Commit your changes (git commit -m 'Add some feature').
    4.Push to the branch (git push origin feature-branch).
    5.Create a new Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
Feel free to reach out with any questions or suggestions:

    Email: mihirsathvara32@gmail.com
    
