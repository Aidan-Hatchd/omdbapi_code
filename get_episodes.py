import requests
from statistics import mean

params = {
    "apikey": "a4c4ee6c",
    "t": "The 100"
}

r = requests.get("https://www.omdbapi.com/", params=params)
data = r.json()

max_seasons = int(data['totalSeasons'])
season = 0
show_rating = []
episode_list = []


while season < max_seasons:
    season += 1
    params = {
    "apikey": "a4c4ee6c",
    "t": "The 100",
    "season": season
    }

    r = requests.get("https://www.omdbapi.com", params=params)
    data = r.json()
    episode_ratings = []
    for episode in data["Episodes"]:
        if episode["imdbRating"] != "N/A":
            episode_ratings.append(float(episode["imdbRating"]))
        episode_list.append((season,episode["Episode"],episode["imdbRating"]))
    season_rating = round(mean(episode_ratings), 1)
    show_rating.append(float(season_rating))
show_ratings = round(mean(show_rating), 1)

import csv
header = ['Season', 'Episode number', 'IMDB Rating']
data = [f'{season}', episode, episode_ratings]

with open('episodes.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(episode_list)