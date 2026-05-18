![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Lab | De JavaScript a Python: Arrays y Datos

## Objetivo

Traducir dos labs clásicos de JavaScript a Python, aplicando correctamente los equivalentes pythónicos de los métodos de array y la lógica de manipulación de datos.

## Contexto

Ya has trabajado con estos labs en JavaScript:
- **LAB | JS Functions & Arrays** — funciones básicas sobre arrays
- **LAB | Greatest Movies** — procesamiento de datos con objetos

Ahora vas a reescribirlos en Python. La lógica es idéntica; lo que cambia es la sintaxis del lenguaje.

## Referencia rápida JS → Python

| JavaScript | Python |
|-----------|--------|
| `array.map(fn)` | `[fn(x) for x in array]` |
| `array.filter(fn)` | `[x for x in array if fn(x)]` |
| `array.reduce(fn, init)` | `sum()`, `max()`, bucle acumulador |
| `array.find(fn)` | `next((x for x in array if fn(x)), None)` |
| `array.includes(val)` | `val in array` |
| `array.sort((a,b) => ...)` | `sorted(array, key=..., reverse=...)` |
| `array.length` | `len(array)` |
| `Math.max(a, b)` | `max(a, b)` |
| `null` | `None` |
| `camelCase` | `snake_case` |

---

## Parte 1 — Funciones y Arrays

### Datos de prueba

```python
words  = ["mystery", "brother", "aviator", "crocodile", "pearl", "orchard", "crackpot"]
words2 = ["machine", "subset", "trouble", "starting", "matter", "eating", "truth", "disobedience"]
numbers  = [6, 12, 1, 18, 13, 16, 2, 1, 8, 10]
numbers2 = [2, 6, 9, 10, 7, 4, 1, 9]
```

### Iteración 1 — El mayor de dos números

**JavaScript de referencia:**
```javascript
function maxOfTwoNumbers(a, b) {
  if (a >= b) return a;
  return b;
}
```

**Tu turno en Python:**
```python
def max_of_two_numbers(a, b):
    pass
```

### Iteración 2 — La palabra más larga

**JavaScript de referencia:**
```javascript
function findLongestWord(words) {
  if (words.length === 0) return null;
  let longest = words[0];
  for (let word of words) {
    if (word.length > longest.length) longest = word;
  }
  return longest;
}
```

**Tu turno en Python:**
```python
def find_longest_word(words):
    # Si la lista está vacía, devuelve None
    # Si hay empate de longitud, devuelve la primera ocurrencia
    pass
```

### Iteración 3 — Suma de números

**JavaScript de referencia:**
```javascript
function sumNumbers(numbers) {
  let total = 0;
  for (let n of numbers) total += n;
  return total;
}
```

**Tu turno en Python:**
```python
def sum_numbers(numbers):
    pass
```

### Iteración 4 — Media de números

**JavaScript de referencia:**
```javascript
function averageNumbers(numbers) {
  if (numbers.length === 0) return null;
  return sumNumbers(numbers) / numbers.length;
}
```

**Tu turno en Python:**
```python
def average_numbers(numbers):
    # Devuelve None si la lista está vacía
    pass
```

### Iteración 5 — ¿Existe la palabra?

**JavaScript de referencia:**
```javascript
function doesWordExist(words, word) {
  if (words.length === 0) return null;
  return words.includes(word);
}
```

**Tu turno en Python:**
```python
def does_word_exist(words, word):
    # Devuelve None si la lista está vacía
    pass
```

---

## Parte 2 — Las Mejores Películas

### Datos

```python
movies = [
    {"title": "The Shawshank Redemption", "year": 1994, "director": "Frank Darabont",    "duration": "2h 22min", "genre": ["Crime", "Drama"],          "score": 9.3},
    {"title": "The Godfather",             "year": 1972, "director": "Francis Ford Coppola", "duration": "2h 55min", "genre": ["Crime", "Drama"],       "score": 9.2},
    {"title": "Schindler's List",          "year": 1993, "director": "Steven Spielberg",  "duration": "3h 15min", "genre": ["Biography", "Drama", "History"], "score": 9.0},
    {"title": "The Dark Knight",           "year": 2008, "director": "Christopher Nolan", "duration": "2h 32min", "genre": ["Action", "Crime", "Drama"],  "score": 9.0},
    {"title": "Pulp Fiction",              "year": 1994, "director": "Quentin Tarantino", "duration": "2h 34min", "genre": ["Crime", "Drama"],            "score": 8.9},
    {"title": "Forrest Gump",              "year": 1994, "director": "Robert Zemeckis",   "duration": "2h 22min", "genre": ["Drama", "Romance"],          "score": 8.8},
    {"title": "Inception",                 "year": 2010, "director": "Christopher Nolan", "duration": "2h 28min", "genre": ["Action", "Adventure", "Sci-Fi"], "score": 8.8},
    {"title": "The Matrix",                "year": 1999, "director": "Lana Wachowski",    "duration": "2h 16min", "genre": ["Action", "Sci-Fi"],          "score": 8.7},
    {"title": "Goodfellas",                "year": 1990, "director": "Martin Scorsese",   "duration": "2h 26min", "genre": ["Biography", "Crime", "Drama"], "score": 8.7},
    {"title": "Amistad",                   "year": 1997, "director": "Steven Spielberg",  "duration": "2h 35min", "genre": ["Biography", "Drama", "History"], "score": 7.3},
    {"title": "Interstellar",              "year": 2014, "director": "Christopher Nolan", "duration": "2h 49min", "genre": ["Adventure", "Drama", "Sci-Fi"], "score": 8.7},
    {"title": "Saving Private Ryan",       "year": 1998, "director": "Steven Spielberg",  "duration": "2h 49min", "genre": ["Drama", "War"],              "score": 8.6},
    {"title": "The Silence of the Lambs",  "year": 1991, "director": "Jonathan Demme",    "duration": "1h 58min", "genre": ["Crime", "Drama", "Thriller"], "score": 8.6},
    {"title": "City of God",               "year": 2002, "director": "Fernando Meirelles","duration": "2h 10min", "genre": ["Crime", "Drama"],            "score": 8.6},
    {"title": "Parasite",                  "year": 2019, "director": "Bong Joon-ho",      "duration": "2h 12min", "genre": ["Comedy", "Drama", "Thriller"], "score": 8.6},
]
```

### Iteración 1 — Todos los directores

**JavaScript de referencia:**
```javascript
function getAllDirectors(movies) {
  return movies.map(movie => movie.director);
}
```

**Tu turno en Python:**
```python
def get_all_directors(movies):
    pass
```

### Iteración 1.1 — Sin duplicados (Bonus)

**JavaScript de referencia:**
```javascript
function getAllDirectors(movies) {
  return [...new Set(movies.map(movie => movie.director))];
}
```

**Tu turno en Python:**
```python
def get_all_directors_unique(movies):
    # Sin directores repetidos
    pass
```

### Iteración 2 — Steven Spielberg y el Drama

**JavaScript de referencia:**
```javascript
function howManyMovies(movies) {
  return movies.filter(
    movie => movie.director === "Steven Spielberg" && movie.genre.includes("Drama")
  ).length;
}
```

**Tu turno en Python:**
```python
def how_many_movies(movies):
    # Devuelve el número de películas de Drama dirigidas por Steven Spielberg
    pass
```

### Iteración 3 — Puntuación media

**JavaScript de referencia:**
```javascript
function scoresAverage(movies) {
  if (movies.length === 0) return 0;
  const total = movies.reduce((acc, movie) => acc + movie.score, 0);
  return Math.round((total / movies.length) * 100) / 100;
}
```

**Tu turno en Python:**
```python
def scores_average(movies):
    # Devuelve la media de scores redondeada a 2 decimales
    # Devuelve 0 si la lista está vacía
    pass
```

### Iteración 4 — Media del Drama

**JavaScript de referencia:**
```javascript
function dramaMoviesScore(movies) {
  const dramas = movies.filter(movie => movie.genre.includes("Drama"));
  if (dramas.length === 0) return 0;
  return scoresAverage(dramas);
}
```

**Tu turno en Python:**
```python
def drama_movies_score(movies):
    # Filtra solo las películas de Drama y devuelve su puntuación media
    pass
```

### Iteración 5 — Ordenar por año

**JavaScript de referencia:**
```javascript
function orderByYear(movies) {
  return [...movies].sort((a, b) => {
    if (a.year !== b.year) return a.year - b.year;
    return a.title.localeCompare(b.title);
  });
}
```

**Tu turno en Python:**
```python
def order_by_year(movies):
    # Devuelve una NUEVA lista ordenada por año (ascendente)
    # Si dos películas tienen el mismo año, ordénalas alfabéticamente por título
    # No modifiques la lista original
    pass
```

### Iteración 6 — Orden alfabético (top 20)

**JavaScript de referencia:**
```javascript
function orderAlphabetically(movies) {
  return [...movies]
    .sort((a, b) => a.title.localeCompare(b.title))
    .slice(0, 20)
    .map(movie => movie.title);
}
```

**Tu turno en Python:**
```python
def order_alphabetically(movies):
    # Devuelve los títulos (solo el string) de las primeras 20 películas en orden alfabético
    # Si hay menos de 20, devuelve todas
    # No modifiques la lista original
    pass
```

### Bonus — Iteración 7: Convertir duración a minutos

**JavaScript de referencia:**
```javascript
function turnHoursToMinutes(movies) {
  return movies.map(movie => {
    const match = movie.duration.match(/(\d+)h\s*(\d*)min?/);
    const hours = parseInt(match[1]) || 0;
    const mins  = parseInt(match[2]) || 0;
    return { ...movie, duration: hours * 60 + mins };
  });
}
```

**Tu turno en Python:**
```python
def turn_hours_to_minutes(movies):
    # Devuelve una NUEVA lista de películas con duration convertida a minutos (int)
    # Formato de entrada: "2h 22min", "1h 58min", "2h 49min"
    # No modifiques la lista original
    pass
```

### Bonus — Iteración 8: El mejor año

**JavaScript de referencia:**
```javascript
function bestYearAvg(movies) {
  if (movies.length === 0) return null;
  const byYear = {};
  movies.forEach(movie => {
    if (!byYear[movie.year]) byYear[movie.year] = [];
    byYear[movie.year].push(movie.score);
  });
  let bestYear, bestAvg = 0;
  for (const [year, scores] of Object.entries(byYear)) {
    const avg = scores.reduce((a, b) => a + b, 0) / scores.length;
    if (avg > bestAvg || (avg === bestAvg && year < bestYear)) {
      bestAvg = avg; bestYear = year;
    }
  }
  return `The best year was ${bestYear} with an average score of ${bestAvg}`;
}
```

**Tu turno en Python:**
```python
def best_year_avg(movies):
    # Devuelve None si la lista está vacía
    # Devuelve el string: "The best year was YEAR with an average score of SCORE"
    # El score debe estar redondeado a 2 decimales
    pass
```

---

## Cómo probar tu código

Crea un archivo `movies.py` con las funciones y pruébalas al final con:

```python
if __name__ == "__main__":
    # Parte 1
    print(max_of_two_numbers(4, 7))           # 7
    print(find_longest_word(words))            # "crocodile"
    print(sum_numbers(numbers))               # 87
    print(average_numbers(numbers2))          # 6.0
    print(does_word_exist(words2, "truth"))   # True
    print(does_word_exist(words2, "coding"))  # False

    # Parte 2
    print(get_all_directors(movies))
    print(how_many_movies(movies))            # 3
    print(scores_average(movies))             # 8.79
    print(drama_movies_score(movies))         # 8.75
    print(order_by_year(movies)[0]["title"])  # "The Godfather" (1972)
    print(order_alphabetically(movies)[:3])   # primeros 3 títulos en orden A-Z
```

---

## Diferencias clave a recordar

| Concepto | JavaScript | Python |
|---------|-----------|--------|
| Spread/copy de objeto | `{ ...obj }` | `{**obj}` o `obj.copy()` |
| Copia de array | `[...arr]` | `arr.copy()` o `arr[:]` |
| Desestructuración | `const [a, b] = arr` | `a, b = arr` |
| Regex | `str.match(/pattern/)` | `re.search(r"pattern", str)` |
| `parseInt` | `parseInt(str)` | `int(str)` |
| `null` condicional | `x ?? default` | `x or default` (ojo con falsy) |
| Nombres de funciones | `camelCase` | `snake_case` |
| Nombres de variables | `camelCase` | `snake_case` |
