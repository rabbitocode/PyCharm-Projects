from bs4 import BeautifulSoup

import requests


# Step 1: Send a GET request to the webpage
url = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find the section containing the top 100 movies
# Inspect the HTML and update the class accordingly
# Movie titles are under <h3> tags with class that starts with "title" (based on inspection)

movies = soup.find_all('h3')

# Step 4: Extract the movie titles and store them in a list
top_100_movies = [movie.get_text(strip=True) for movie in movies if movie.get_text(strip=True)]

# Step 5: Save the movie titles to a txt file
with open('top_100_movies.txt', 'w') as file:
    for i, movie in enumerate(top_100_movies, start=1):
        file.write(f"{i}. {movie}\n")

print("Top 100 movies have been saved to top_100_movies.txt")