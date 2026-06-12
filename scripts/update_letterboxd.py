import re
import sys
from urllib.request import urlopen, Request

RSS_URL = "https://letterboxd.com/whattheprak/rss/"
README_PATH = "README.md"
NUM_FILMS = 4


def fetch_films():
    req = Request(RSS_URL, headers={"User-Agent": "Mozilla/5.0 (compatible; profile-readme-bot/1.0)"})
    with urlopen(req) as resp:
        xml = resp.read().decode("utf-8")

    items = re.findall(r"<item>(.*?)</item>", xml, re.DOTALL)
    films = []
    for item in items[:NUM_FILMS]:
        title_match = re.search(r"<letterboxd:filmTitle>(.*?)</letterboxd:filmTitle>", item)
        title = title_match.group(1) if title_match else ""

        link_match = re.search(r"<link>(.*?)</link>", item)
        link = link_match.group(1) if link_match else ""

        img_match = re.search(r'<img src="([^"]+)"', item)
        poster = img_match.group(1) if img_match else ""

        if title and link and poster:
            films.append({"title": title, "link": link, "poster": poster})

    return films


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
    films = fetch_films()
    if not films:
        print("No films found in RSS feed.", file=sys.stderr)
        sys.exit(1)
    update_readme(build_card(films))
