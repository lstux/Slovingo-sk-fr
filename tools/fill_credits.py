#!/usr/bin/env python3
"""Complète les crédits des photos Wikimedia Commons.

Pour chaque ligne de img/credits.md dont l'auteur ou la licence vaut « à compléter » (ou « à vérifier »),
le script interroge l'API Commons (auteur, licence), puis :
  - remplit la ligne dans img/credits.md ;
  - remplace « crédit à compléter » dans la légende `@` de la fiche correspondante.

Les fichiers introuvables sur Commons sont signalés : il faut alors choisir une autre photo.

Usage, depuis la racine du cours :
    python3 tools/fill_credits.py            # complète et écrit
    python3 tools/fill_credits.py --dry-run  # affiche seulement ce qui serait fait

À lancer AVANT src/fetch_images.py (qui remplace les adresses Commons par des chemins locaux).
Doucement : une requête toutes les 2 secondes, avec reprise en cas de 429.
"""
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CREDITS = ROOT / "img" / "credits.md"
MD = ROOT / "md"
API = "https://commons.wikimedia.org/w/api.php"
UA = "SlovingoCredits/1.0 (cours Slovingo-sk-fr; contact via GitHub lstux)"
TODO_MARKS = ("à compléter", "à vérifier", "non précisée")
PAUSE = 2.0

ROW = re.compile(r"^\| (?P<fiche>[^|]+?) \| \[(?P<name>[^\]]+)\]\((?P<url>[^)]+)\) \| (?P<author>[^|]+?) \| (?P<lic>[^|]+?) \|\s*$")


def strip_html(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s or "")
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def query(name: str) -> dict | None:
    params = {
        "action": "query", "format": "json", "prop": "imageinfo",
        "iiprop": "extmetadata", "redirects": "1",
        "titles": "File:" + name,
    }
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(5):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.load(r)
            break
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 10 * (attempt + 1)
                print(f"   429, pause {wait} s…")
                time.sleep(wait)
                continue
            raise
    else:
        return None
    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        if "missing" in page or "imageinfo" not in page:
            return {}
        meta = page["imageinfo"][0].get("extmetadata", {})
        author = strip_html(meta.get("Artist", {}).get("value", ""))
        lic = strip_html(meta.get("LicenseShortName", {}).get("value", ""))
        return {"author": author or "auteur non indiqué", "licence": lic or "licence non indiquée"}
    return {}


def main() -> None:
    dry = "--dry-run" in sys.argv
    lines = CREDITS.read_text(encoding="utf-8").splitlines(keepends=True)
    missing = []
    done = 0
    for i, line in enumerate(lines):
        m = ROW.match(line)
        if not m or not any(t in m["author"] + m["lic"] for t in TODO_MARKS):
            continue
        name = m["name"]
        print(f"→ {m['fiche']} : {name}")
        if dry:
            continue
        info = query(name)
        time.sleep(PAUSE)
        if info is None:
            print("   pas de réponse, on passe")
            continue
        if not info:
            print("   INTROUVABLE sur Commons : choisir une autre photo")
            missing.append((m["fiche"], name))
            continue
        a, l = info["author"], info["licence"]
        print(f"   {a} — {l}")
        lines[i] = f"| {m['fiche']} | [{name}]({m['url']}) | {a} | {l} |\n"
        fiche = MD / f"10_Series_{m['fiche']}.md"
        if fiche.exists():
            text = fiche.read_text(encoding="utf-8")
            # la ligne @ de la fiche : on remplace le crédit entre le dernier « — » et « , Wikimedia Commons »
            new = re.sub(r"^(@ [^\n]* — )[^\n—]*(, Wikimedia Commons)$",
                         lambda mm: f"{mm.group(1)}{a}, {l}{mm.group(2)}", text, count=1, flags=re.M)
            fiche.write_text(new, encoding="utf-8")
        done += 1
    if not dry:
        CREDITS.write_text("".join(lines), encoding="utf-8")
    print(f"\n{done} crédit(s) complété(s).")
    if missing:
        print("Introuvables :")
        for f, n in missing:
            print(f"  - {f} : {n}")


if __name__ == "__main__":
    main()
