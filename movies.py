import re

# ─── Datos de prueba ───────────────────────────────────────────────────────────

words  = ["mystery", "brother", "aviator", "crocodile", "pearl", "orchard", "crackpot"]
words2 = ["machine", "subset", "trouble", "starting", "matter", "eating", "truth", "disobedience"]
numbers  = [6, 12, 1, 18, 13, 16, 2, 1, 8, 10]
numbers2 = [2, 6, 9, 10, 7, 4, 1, 9]

movies = [
    {"title": "The Shawshank Redemption", "year": 1994, "director": "Frank Darabont",       "duration": "2h 22min", "genre": ["Crime", "Drama"],                  "score": 9.3},
    {"title": "The Godfather",             "year": 1972, "director": "Francis Ford Coppola", "duration": "2h 55min", "genre": ["Crime", "Drama"],                  "score": 9.2},
    {"title": "Schindler's List",          "year": 1993, "director": "Steven Spielberg",     "duration": "3h 15min", "genre": ["Biography", "Drama", "History"],   "score": 9.0},
    {"title": "The Dark Knight",           "year": 2008, "director": "Christopher Nolan",    "duration": "2h 32min", "genre": ["Action", "Crime", "Drama"],        "score": 9.0},
    {"title": "Pulp Fiction",              "year": 1994, "director": "Quentin Tarantino",    "duration": "2h 34min", "genre": ["Crime", "Drama"],                  "score": 8.9},
    {"title": "Forrest Gump",              "year": 1994, "director": "Robert Zemeckis",      "duration": "2h 22min", "genre": ["Drama", "Romance"],                "score": 8.8},
    {"title": "Inception",                 "year": 2010, "director": "Christopher Nolan",    "duration": "2h 28min", "genre": ["Action", "Adventure", "Sci-Fi"],   "score": 8.8},
    {"title": "The Matrix",                "year": 1999, "director": "Lana Wachowski",       "duration": "2h 16min", "genre": ["Action", "Sci-Fi"],                "score": 8.7},
    {"title": "Goodfellas",                "year": 1990, "director": "Martin Scorsese",      "duration": "2h 26min", "genre": ["Biography", "Crime", "Drama"],     "score": 8.7},
    {"title": "Amistad",                   "year": 1997, "director": "Steven Spielberg",     "duration": "2h 35min", "genre": ["Biography", "Drama", "History"],   "score": 7.3},
    {"title": "Interstellar",              "year": 2014, "director": "Christopher Nolan",    "duration": "2h 49min", "genre": ["Adventure", "Drama", "Sci-Fi"],    "score": 8.7},
    {"title": "Saving Private Ryan",       "year": 1998, "director": "Steven Spielberg",     "duration": "2h 49min", "genre": ["Drama", "War"],                    "score": 8.6},
    {"title": "The Silence of the Lambs",  "year": 1991, "director": "Jonathan Demme",       "duration": "1h 58min", "genre": ["Crime", "Drama", "Thriller"],      "score": 8.6},
    {"title": "City of God",               "year": 2002, "director": "Fernando Meirelles",   "duration": "2h 10min", "genre": ["Crime", "Drama"],                  "score": 8.6},
    {"title": "Parasite",                  "year": 2019, "director": "Bong Joon-ho",         "duration": "2h 12min", "genre": ["Comedy", "Drama", "Thriller"],     "score": 8.6},
]


# ─── Parte 1: Funciones y Arrays ──────────────────────────────────────────────

def max_of_two_numbers(a, b):
    if a >= b:
        return a
    return b


def find_longest_word(words):
    if not words:
        return None
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def sum_numbers(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def average_numbers(numbers):
    if not numbers:
        return None
    return sum_numbers(numbers) / len(numbers)


def does_word_exist(words, word):
    if not words:
        return None
    return word in words


# ─── Parte 2: Las Mejores Películas ──────────────────────────────────────────

def get_all_directors(movies):
    return [movie["director"] for movie in movies]


def get_all_directors_unique(movies):
    seen = set()
    result = []
    for movie in movies:
        if movie["director"] not in seen:
            seen.add(movie["director"])
            result.append(movie["director"])
    return result


def how_many_movies(movies):
    return len([
        m for m in movies
        if m["director"] == "Steven Spielberg" and "Drama" in m["genre"]
    ])


def scores_average(movies):
    if not movies:
        return 0
    total = sum(m["score"] for m in movies)
    return round(total / len(movies), 2)


def drama_movies_score(movies):
    dramas = [m for m in movies if "Drama" in m["genre"]]
    return scores_average(dramas)


def order_by_year(movies):
    return sorted(movies, key=lambda m: (m["year"], m["title"]))


def order_alphabetically(movies):
    sorted_movies = sorted(movies, key=lambda m: m["title"])
    return [m["title"] for m in sorted_movies[:20]]


def turn_hours_to_minutes(movies):
    def parse(duration):
        match = re.search(r"(\d+)h\s*(\d*)m?i?n?", duration)
        hours = int(match.group(1)) if match else 0
        mins  = int(match.group(2)) if match and match.group(2) else 0
        return hours * 60 + mins

    return [{**movie, "duration": parse(movie["duration"])} for movie in movies]


def best_year_avg(movies):
    if not movies:
        return None

    by_year = {}
    for movie in movies:
        by_year.setdefault(movie["year"], []).append(movie["score"])

    best_year, best_avg = None, -1
    for year, scores in by_year.items():
        avg = sum(scores) / len(scores)
        if avg > best_avg or (avg == best_avg and year < best_year):
            best_avg = avg
            best_year = year

    return f"The best year was {best_year} with an average score of {round(best_avg, 2)}"


# ─── Tests ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("--- Parte 1 ---")
    print(max_of_two_numbers(4, 7))           # 7
    print(find_longest_word(words))            # crocodile
    print(sum_numbers(numbers))               # 87
    print(average_numbers(numbers2))          # 6.0
    print(does_word_exist(words2, "truth"))   # True
    print(does_word_exist(words2, "coding"))  # False

    print("\n--- Parte 2 ---")
    print(get_all_directors(movies))
    print(get_all_directors_unique(movies))
    print(how_many_movies(movies))            # 3
    print(scores_average(movies))
    print(drama_movies_score(movies))
    print(order_by_year(movies)[0]["title"])  # The Godfather (1972)
    print(order_alphabetically(movies)[:3])

    print("\n--- Bonus ---")
    converted = turn_hours_to_minutes(movies)
    print(converted[0]["title"], converted[0]["duration"], "min")
    print(best_year_avg(movies))
