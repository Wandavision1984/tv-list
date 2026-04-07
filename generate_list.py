import os
import re

TV_FOLDER = r"F:\Shows"
OUTPUT_FILE = "index.html"

def normalize_season_name(name):
    """Turn folder names like 'S01', 'Season 1', '1' into 'Season 1'"""
    match = re.search(r'(\d+)', name)
    if match:
        return f"Season {int(match.group(1))}"
    return name

def get_shows(folder):
    shows = {}
    for show_name in os.listdir(folder):
        show_path = os.path.join(folder, show_name)
        if os.path.isdir(show_path):
            seasons = []
            for item in os.listdir(show_path):
                item_path = os.path.join(show_path, item)
                if os.path.isdir(item_path):
                    seasons.append(normalize_season_name(item))
            # If no season folders, but episodes exist, call it Season 1
            if not seasons:
                episodes = [f for f in os.listdir(show_path)
                            if f.lower().endswith(('.mkv', '.mp4', '.avi', '.mov'))]
                if episodes:
                    seasons.append("Season 1")
            shows[show_name] = sorted(seasons)
    return dict(sorted(shows.items()))

def generate_html(shows):
    html = """
    <html>
    <head>
        <title>My TV Shows</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: auto; padding: 20px; }
            h1 { text-align: center; }
            ul { list-style-type: none; padding-left: 0; }
            li { padding: 8px 0; border-bottom: 1px solid #ddd; }
            strong { color: #333; }
            @media (max-width: 600px) { body { padding: 10px; } }
        </style>
    </head>
    <body>
        <div style="text-align:center; margin-bottom:15px;">
            <a href="https://wandavision1984.github.io/movie-list/">🎬 Movies</a> |
            <a href="https://wandavision1984.github.io/tv-list/">📺 TV Shows</a>
        </div>
        <h1>📺 My TV Shows</h1>
        <ul>
    """

    for show, seasons in shows.items():
        html += f"<li><strong>{show}</strong>: {', '.join(seasons)}</li>"

    html += "</ul></body></html>"
    return html

shows = get_shows(TV_FOLDER)
html = generate_html(shows)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Done! {len(shows)} shows listed.")
