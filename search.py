import requests

params = {
    "apikey": "a4c4ee6c",
    "t": "The 100"
}

r = requests.get("https://www.omdbapi.com/", params=params)
data = r.json()
print(data)
print(f"IMDB Score {data['imdbRating']}")
