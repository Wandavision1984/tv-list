import os
import re

MOVIE_FOLDER = r"F:\Shows"
OUTPUT_FILE = "index.html"

def get_movies(folder):
    movies = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith((".mp4", ".mkv", ".avi", ".mov")):
                movies.append(file)
    return sorted(movies)

def extract_year(name):
    match = re.search(r"(19|20)\d{2}", name)
    return match.group(0) if match else "Unknown"

def guess_genre(name):
    name = name.lower()
    if "action" in name: return "Action"
    if "comedy" in name: return "Comedy"
    if "horror" in name: return "Horror"
    if "sci" in name or "space" in name: return "Sci-Fi"
    if "romance" in name: return "Romance"
    return "Other"

def generate_html(movies):
    movie_items = ""

    for movie in movies:
        clean_name = os.path.splitext(movie)[0].replace(".", " ")
        year = extract_year(clean_name)
        genre = guess_genre(clean_name)
        rating = "⭐⭐⭐☆☆"  # placeholder

        movie_items += f"""
        <div class="movie-row" data-title="{clean_name.lower()}" data-genre="{genre}">
            <div class="title">{clean_name}</div>
            <div class="meta">{year} • {genre}</div>
            <div class="rating">{rating}</div>
        </div>
        """

    return f"""
<!DOCTYPE html>
<html>
<head>
<title>My Movie Collection</title>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body {{
    font-family: Arial, sans-serif;
    background: #121212;
    color: white;
    margin: 0;
    padding: 15px;
}}

h1 {{
    text-align: center;
}}

.controls {{
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 20px;
}}

input, select {{
    padding: 10px;
    border-radius: 8px;
    border: none;
    font-size: 14px;
}}

.movie-row {{
    background: #1e1e1e;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
    transition: 0.2s;
}}

.movie-row:hover {{
    background: #2a2a2a;
}}

.title {{
    font-size: 16px;
    font-weight: bold;
}}

.meta {{
    font-size: 13px;
    color: #aaa;
}}

.rating {{
    margin-top: 5px;
}}

@media (min-width: 600px) {{
    .controls {{
        flex-direction: row;
    }}
}}
</style>
</head>

<body>

<h1>🎬 My Movie Collection</h1>

<div class="controls">
    <input type="text" id="search" placeholder="Search movies...">
    
    <select id="genreFilter">
        <option value="All">All Genres</option>
        <option>Action</option>
        <option>Comedy</option>
        <option>Horror</option>
        <option>Sci-Fi</option>
        <option>Romance</option>
        <option>Other</option>
    </select>
</div>

<div id="movieList">
{movie_items}
</div>

<script>
const searchInput = document.getElementById("search");
const genreFilter = document.getElementById("genreFilter");
const movies = document.querySelectorAll(".movie-row");

function filterMovies() {{
    const search = searchInput.value.toLowerCase();
    const genre = genreFilter.value;

    movies.forEach(movie => {{
        const title = movie.getAttribute("data-title");
        const movieGenre = movie.getAttribute("data-genre");

        const matchesSearch = title.includes(search);
        const matchesGenre = genre === "All" || movieGenre === genre;

        movie.style.display = (matchesSearch && matchesGenre) ? "block" : "none";
    }});
}}

searchInput.addEventListener("input", filterMovies);
genreFilter.addEventListener("change", filterMovies);
</script>

</body>
</html>
"""

movies = get_movies(MOVIE_FOLDER)
html = generate_html(movies)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Done! {len(movies)} movies listed.")