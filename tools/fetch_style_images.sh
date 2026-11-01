#!/usr/bin/env bash
# fetch_style_images.sh
# ---------------------
# Télécharge les photos des bandeaux de style (thèmes CSS) depuis Wikimedia
# Commons, les nomme `img/style_<clé>.jpg` et les réduit à 1200 px de large
# au maximum (jamais agrandies).
#
# Il faut : curl et ImageMagick (`convert`, ou `magick` pour la version 7).
#
# Usage (depuis la racine du dépôt) :
#   ./tools/fetch_style_images.sh              # télécharge et réduit les images manquantes
#   ./tools/fetch_style_images.sh family city  # seulement certaines clés
#   ./tools/fetch_style_images.sh --force      # refait aussi celles qui existent déjà
#   ./tools/fetch_style_images.sh --credits    # affiche auteur et licence de chaque image
#                                              # (lignes prêtes à coller dans img/credits.md)
#
# Variables facultatives :
#   WIDTH=1200     largeur maximale en pixels
#   QUALITY=82     qualité JPEG
#
# Les noms de fichiers Commons sont écrits tels qu'ils apparaissent dans
# l'adresse de la page (avec le codage %xx), pour être recopiés sans erreur.

set -euo pipefail

WIDTH="${WIDTH:-1200}"
QUALITY="${QUALITY:-82}"
UA="Slovingo-style-images/1.0 (https://github.com/lstux/Slovingo-sk-fr)"
COMMONS="https://commons.wikimedia.org"

# clé de thème | nom du fichier Commons (codé comme dans l'adresse de la page)
IMAGES=(
  "mountains|Vysok%C3%A9_Tatry_panorama.jpg"
  "city|Bratislava_Panorama_R01.jpg"
  "default|Kremnicke_vrchy_from_Kremnica.jpg"
  "basics|Flowers_%C5%A0trbsk%C3%A9_Pleso_25_Slovakia_4.jpg"
  "shopping|Bojnice_Castle_Slovakia.jpg"
  "food|Bansk%C3%A1_%C5%A0tiavnica_from_Nov%C3%BD_z%C3%A1mok_2007.jpg"
  "time|Slovakia-01893_-_Orava_Castle_(31909660610).jpg"
  "family|Hlavn%C3%A1_ulica._Pre%C5%A1ov_20_Slovakia.jpg"
  "games|Devin_Hrad_Panorama.jpg"
)

# --- Arguments ---------------------------------------------------------
FORCE=0
CREDITS=0
KEYS=()
for arg in "$@"; do
  case "$arg" in
    --force)   FORCE=1 ;;
    --credits) CREDITS=1 ;;
    -h|--help) sed -n '2,24p' "$0"; exit 0 ;;
    *)         KEYS+=("$arg") ;;
  esac
done

wanted() {  # la clé $1 est-elle demandée ? (toutes si aucune n'est précisée)
  [ "${#KEYS[@]}" -eq 0 ] && return 0
  local k
  for k in "${KEYS[@]}"; do [ "$k" = "$1" ] && return 0; done
  return 1
}

# --- Outils ------------------------------------------------------------
command -v curl >/dev/null || { echo "Erreur : curl est introuvable." >&2; exit 1; }

if command -v magick >/dev/null; then
  IM=(magick)
elif command -v convert >/dev/null; then
  IM=(convert)
else
  echo "Erreur : ImageMagick (convert ou magick) est introuvable." >&2
  exit 1
fi

# Va à la racine du dépôt (le dossier qui contient tools/)
cd "$(dirname "$0")/.."
mkdir -p img

# --- Mode crédits ------------------------------------------------------
if [ "$CREDITS" -eq 1 ]; then
  command -v python3 >/dev/null || { echo "Erreur : python3 est nécessaire pour --credits." >&2; exit 1; }
  for entry in "${IMAGES[@]}"; do
    key="${entry%%|*}"; name="${entry#*|}"
    wanted "$key" || continue
    python3 - "$key" "$name" "$COMMONS" "$UA" <<'PY'
import json, re, sys, urllib.parse, urllib.request

key, name, commons, ua = sys.argv[1:5]
title = "File:" + urllib.parse.unquote(name).replace("_", " ")
url = (commons + "/w/api.php?action=query&format=json&prop=imageinfo"
       "&iiprop=extmetadata&titles=" + urllib.parse.quote(title))
try:
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    data = json.load(urllib.request.urlopen(req, timeout=30))
    page = next(iter(data["query"]["pages"].values()))
    meta = page["imageinfo"][0]["extmetadata"]
except Exception as exc:
    print(f"| style_{key}.jpg | {title} | ERREUR : {exc} | |")
    sys.exit(0)

def clean(field):
    value = meta.get(field, {}).get("value", "")
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", value)).strip()

page_url = commons + "/wiki/" + urllib.parse.quote(title.replace(" ", "_"), safe="(),:_-")
print(f"| style_{key}.jpg | [{title[5:]}]({page_url}) | {clean('Artist') or 'inconnu'} | {clean('LicenseShortName') or 'inconnue'} |")
PY
  done
  exit 0
fi

# --- Téléchargement et réduction -----------------------------------------
fail=0
for entry in "${IMAGES[@]}"; do
  key="${entry%%|*}"; name="${entry#*|}"
  wanted "$key" || continue

  out="img/style_${key}.jpg"
  if [ -f "$out" ] && [ "$FORCE" -eq 0 ]; then
    echo "= $out existe déjà (--force pour le refaire)"
    continue
  fi

  tmp="$(mktemp "${TMPDIR:-/tmp}/slovingo-style-${key}.XXXXXX")"
  echo "↓ $key : $name"
  if ! curl -fsSL --retry 3 -A "$UA" -o "$tmp" "$COMMONS/wiki/Special:FilePath/$name"; then
    echo "  ✗ téléchargement impossible pour « $key »" >&2
    rm -f "$tmp"; fail=1; continue
  fi

  # [0] = première image ; -auto-orient : respecte l'orientation EXIF ;
  # WIDTHx> : réduit seulement si l'image est plus large que WIDTH.
  if "${IM[@]}" "${tmp}[0]" -auto-orient -resize "${WIDTH}x>" \
        -colorspace sRGB -strip -interlace Plane -quality "$QUALITY" "$out"; then
    size="$(du -k "$out" | cut -f1)"
    dims="$(identify -format '%wx%h' "$out" 2>/dev/null || echo '?')"
    echo "  ✓ $out (${dims}, ${size} Ko)"
  else
    echo "  ✗ réduction impossible pour « $key »" >&2
    fail=1
  fi
  rm -f "$tmp"
done

[ "$fail" -eq 0 ] || { echo "Certaines images ont échoué." >&2; exit 1; }
echo "Terminé. Pense à compléter img/credits.md (./tools/fetch_style_images.sh --credits)."
