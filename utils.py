from statistics import mean


def calculate_rating(ratings):
    return round(mean(ratings), 1)
