import re
import sys
import xml.etree.ElementTree as ET
from urllib.request import urlopen

RSS_URL = "https://letterboxd.com/whattheprak/rss/"
README_PATH = "README.md"
LB_NS = "https://letterboxd.com"
NUM_FILMS = 4


def fetch_films():
    with urlopen(RSS_URL) as resp:
        root = ET.fromstring(resp.read())

    films = []
    for item in root.findall(".//item")[:NUM_FILMS]:
        title_elem = item.find(f"{{{LB_NS}}}filmTitle")
        title = title_elem.text if title_elem is not None else item.findtext("title", "")

        link = item.findtext("link", "")
        desc = item.findtext("description", "")

        img_match = re.search(r'<img src="([^"]+)"', desc)
        poster = img_match.group(1) if img_match else ""

        films.append({"title": title, "link": link, "poster": poster})

    return films


def build_card(films):
    cells = " | ".join(
        f'<a href="{f["link"]}"><img src="{f["poster"]}" width="110" title="{f["title"]}"/></a>'
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
