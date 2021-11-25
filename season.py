import requests

from utils import calculate_rating


def get_show(type):
    valid_show = False

    while not valid_show:
        Show = input("What show would you like to research? ")

        params = {
            "apikey": "a4c4ee6c",
            "t": f"{Show}"
        }

        r = requests.get("https://www.omdbapi.com/", params=params)
        data = r.json()

        if data["Response"] == "False":
            print(data["Error"])
            continue

        if data["Type"] != type:
            print(f"Show is wrong type: {data['Type']}")
            continue

        # valid show found
        valid_show = True

    return data


data = get_show(type="series")
max_seasons = int(data['totalSeasons'])
season = 0
show_rating = []
episode_list = []


while season < max_seasons:
    season += 1
    print()
    print(f"Season {season}")
    params = {
    "apikey": "a4c4ee6c",
    "t": data["Title"],
    "season": season
    }

    r = requests.get("https://www.omdbapi.com", params=params)
    data = r.json()
    episode_ratings = []
    for episode in data["Episodes"]:
        print(f"{episode['Episode']}: {episode['Title']} \n {episode['imdbRating']}")

        if episode["imdbRating"] != "N/A":
            episode_ratings.append(float(episode["imdbRating"]))

        episode_list.append((season,episode["Episode"],episode["imdbRating"]))

    season_rating = calculate_rating(episode_ratings)
    print(f"Season Rating: {season_rating}")

    show_rating.append(float(season_rating))


show_ratings = calculate_rating(show_rating)
print(f"Average show rating: {show_ratings}")

import csv

header = ['Season', ' Episode number', ' IMDB Rating']
data = [f'{season}', episode, episode_ratings]

with open('episodes.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(episode_list)