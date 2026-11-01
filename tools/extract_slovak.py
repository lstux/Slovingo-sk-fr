#!/usr/bin/env python3
"""Rassemble tout le slovaque des fiches dans un seul fichier, pour la relecture.

Pour chaque fiche (introduction, kit, chapitres, Kronika), on garde :
  - chaque réplique `!` (avec l'emoji du personnage) et sa traduction `>` ;
  - les tableaux de vocabulaire (slovaque | français).

Le résultat, docs/Texte-slovaque.md, se lit d'un bout à l'autre sans ouvrir
l'appli. Chaque bloc porte le nom de sa fiche, pour retrouver la phrase.

Usage, depuis la racine du cours :
    python3 tools/extract_slovak.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD = ROOT / "md"
OUT = ROOT / "docs" / "Texte-slovaque.md"

NAMES = {
    "🦊": "Gab", "🐰": "Andrea", "🧢": "Hugo", "🐇": "Lola", "📱": "Claire",
    "🧭": "GPS", "💬": "narrateur",
}


def clean(s: str) -> str:
    s = re.sub(r"\{\{fr:([^}]*)\}\}", r"\1", s)
    s = re.sub(r"\{\{([^}]*)\}\}", r"\1", s)
    return s.replace("[USER_NAME]", "Gab").replace("[ASK_USER_NAME]", "Gab").strip()


SK = re.compile(r"[ľščťžýáíúäôňďŕĺČŠŽŤĽÁÍÚÝĎŇ]")


def extract(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    out, title = [], path.stem
    table: list[list[str]] = []

    def flush() -> None:
        # a table is kept only if it holds Slovak (the header line is dropped)
        if len(table) > 1 and any(SK.search(" ".join(r)) for r in table[1:]):
            out.append("")
            for row in table[1:]:
                cells = [clean(c) for c in row]
                out.append(f"- {cells[0]} = *{' · '.join(c for c in cells[1:] if c)}*")
            out.append("")
        table.clear()

    for i, line in enumerate(lines):
        if line.startswith("# ") and title == path.stem:
            title = line[2:].strip()
        if line.startswith("|"):
            if not re.match(r"^\|[-:\s|]+\|$", line):
                table.append([c.strip() for c in line.strip().strip("|").split("|")])
            continue
        if table:
            flush()
        if line.startswith("! "):
            body = line[2:].strip()
            m = re.match(r"^(\S+)\s+(.*)$", body)
            who, text = (m.group(1), m.group(2)) if m and not m.group(1)[0].isalnum() else ("", body)
            fr = lines[i + 1][2:].strip() if i + 1 < len(lines) and lines[i + 1].startswith("> ") else ""
            name = NAMES.get(who, who)
            out.append(f"- {who} **{name}** : {clean(text)}" if who else f"- {clean(text)}")
            if fr:
                out.append(f"  *{clean(fr)}*")
    if table:
        flush()
    return [f"### {title}", f"`md/{path.name}`", ""] + out if out else []


def main() -> None:
    files = sorted(p for p in MD.glob("*.md")
                   if p.name.startswith(("00_", "10_")))
    parts = [
        "# Tout le slovaque du cours",
        "",
        "Généré par `tools/extract_slovak.py` à partir des fiches : ne pas corriger ici, "
        "mais dans la fiche indiquée sous chaque titre (ou signaler la phrase, tout simplement).",
        "",
        "Gab est le prénom par défaut de l'apprenant ; dans l'appli, c'est le prénom choisi.",
        "",
    ]
    for p in files:
        block = extract(p)
        if block:
            parts += block + [""]
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)} : {len(files)} fiches")


if __name__ == "__main__":
    main()
