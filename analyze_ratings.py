import csv
from utils import calculate_rating
show_ratings = 0
number_of_ratings = 0
season = input("What season? ")
season_rating = 0
number_of_season_ratings = 0
ranks_total = 0

season_rankings = {}
all_rankings = []

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def isint(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

with open("episodes.csv", newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    for ep_season, ep_num, ep_rating in rows:
        if ep_season == "Season":
            continue

        if ep_season not in season_rankings:
            season_rankings[ep_season] = []

        if isfloat(ep_rating):
            season_rankings[ep_season].append(float(ep_rating))
            all_rankings.append(float(ep_rating))

if season and season in season_rankings:
    average_rankings = calculate_rating(season_rankings[season])
    print(season, average_rankings)
else:
    # go through the season_rankings, printing out the season number and average ranking
    for seasons, rankings in season_rankings.items():
        average_ratings = calculate_rating(rankings)
        print(f"Season {seasons}: {average_ratings}")


    # print out the overall average ranking
    all_average = calculate_rating(all_rankings)
    print(f"Overall Average: {all_average}")
