import os

MOVIE_FOLDER = r"F:\Movies"

OUTPUT_FILE = "index.html"

def get_movies(folder):
    movies = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith((".mp4", ".mkv", ".avi", ".mov")):
                movies.append(file)
    return sorted(movies)

def generate_html(movies):
    html = "<html><head><title>My Movie List</title></head><body>"
    html += "<h1>My Movies</h1><ul>"

    for movie in movies:
        html += f"<li>{movie}</li>"

    html += "</ul></body></html>"
    return html

movies = get_movies(MOVIE_FOLDER)
html = generate_html(movies)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Done! {len(movies)} movies listed.")