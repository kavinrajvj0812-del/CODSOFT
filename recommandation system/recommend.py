import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Movie Recommendation System 🎬")

# Load dataset
data = pd.read_csv("movies.csv")

# Convert genre text → numbers
cv = CountVectorizer()
genre_matrix = cv.fit_transform(data["genre"])

# Find similarity
similarity = cosine_similarity(genre_matrix)

def recommend(movie_name):
    movie_index = data[data["title"] == movie_name].index[0]
    scores = list(enumerate(similarity[movie_index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:")
    for i in sorted_scores[1:6]:
        print(data.iloc[i[0]]["title"])

movie = input("\nEnter a movie name: ")
recommend(movie)