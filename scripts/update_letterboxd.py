import re
import sys
from urllib.request import urlopen, Request

PROFILE_URL = "https://letterboxd.com/whattheprak/"
FILM_BASE = "https://letterboxd.com/film"
README_PATH = "README.md"
NUM_FILMS = 4
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}


def fetch(url):
    with urlopen(Request(url, headers=HEADERS)) as resp:
        return resp.read().decode("utf-8")


def fetch_favorites():
    html = fetch(PROFILE_URL)

    # Isolate the favourites section to avoid picking up recent-activity entries
    fav_section = re.search(r'id="favourites"(.*?)(?=<section |$)', html, re.DOTALL)
    if not fav_section:
        return []
    section_html = fav_section.group(1)

    # Attribute order in HTML: data-item-name → data-item-slug → data-item-link
    entries = re.findall(
        r'data-item-name="([^"]+)"[^>]*data-item-slug="([^"]+)"[^>]*data-item-link="([^"]+)"',
        section_html,
    )

    films = []
    for name, slug, link in entries[:NUM_FILMS]:
        films.append({"slug": slug, "title": name, "link": f"https://letterboxd.com{link}"})

    return films


def resolve_poster(slug):
    html = fetch(f"{FILM_BASE}/{slug}/")
    match = re.search(r'"image":"(https://a\.ltrbxd\.com/[^"]+)"', html)
    return match.group(1) if match else ""


def build_card(films):
    cells = " | ".join(
        f'<a href="{f["link"]}"><img src="{f["poster"]}" width="120" title="{f["title"]}"/></a>'
        for f in films
    )
    sep = " | ".join(":---:" for _ in films)
    names = " | ".join(f'[{f["title"]}]({f["link"]})' for f in films)
    return f"| {cells} |\n| {sep} |\n| {names} |"


def update_readme(card):
    with open(README_PATH, "r") as f:
        content = f.read()

    updated = re.sub(
        r"<!-- LETTERBOXD-START -->.*?<!-- LETTERBOXD-END -->",
        f"<!-- LETTERBOXD-START -->\n{card}\n<!-- LETTERBOXD-END -->",
        content,
        flags=re.DOTALL,
    )

    if updated == content:
        print("No changes to README.")
        return

    with open(README_PATH, "w") as f:
        f.write(updated)
    print(f"README updated with {len(films)} films.")


if __name__ == "__main__":
    films = fetch_favorites()
    if not films:
        print("No favorite films found.", file=sys.stderr)
        sys.exit(1)

    for film in films:
        film["poster"] = resolve_poster(film["slug"])

    films = [f for f in films if f["poster"]]
    if not films:
        print("Could not resolve any poster images.", file=sys.stderr)
        sys.exit(1)

    update_readme(build_card(films))
