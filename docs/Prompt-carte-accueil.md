# Fond de la carte d'accueil

Image : `img/map_background.jpg`, 768 × 1376 (portrait 9:16), générée avec Gemini le 30 octobre 2026 à partir du prompt ci-dessous.

Le parcours va de haut en bas : l'ouest (Bratislava) en haut, l'est (Košice) en bas, une route qui serpente et les monuments du voyage le long, dans l'ordre des chapitres. Pas de texte sur l'image : les libellés viennent de l'application.

Les positions des étapes sont réglées dans `lang.json` (`map.positions`, en % de l'image), sur le monument de chaque chapitre. Pour les ajuster : `python3 ../Slovingo/tools/map_editor.py .`

Les séries Kronika ne sont pas sur la carte (`map.exclude`), elles restent dans la liste des fiches. La dernière étape est la fiche `99_Credits_01_merci.md`, « Šťastnú cestu! » 🏁.

## Prompt

```
Vertical illustrated travel map of Slovakia, 9:16 portrait (1080×1920), seen from a high bird's-eye angle. Detailed, warm digital painting, golden-hour light, soft and slightly muted colours so that small round markers placed on top stay readable. Same spirit as a vintage tourist poster map, but painterly and realistic, no cartoon.

A single winding road crosses the whole image from the top edge to the bottom edge, in a gentle zigzag (left, right, left…). The journey goes from west (top) to east (bottom). Along the road, from top to bottom, small vignette-sized landmarks, each in its own area, alternating left and right of the road:

1. Top: the road enters from the top edge, coming from far away.
2. A cosy café terrace on the bank of the Danube.
3. Bratislava Castle (white, square, four corner towers, red roofs) on its hill above the Danube, with the modern bridge topped by a round "UFO" restaurant.
4. Trenčín Castle on a rock above the Váh river, with its tall square tower; a small spa colonnade bridge nearby.
5. Bojnice Castle, a fairytale castle with many pointed spires, among trees; a brown bear in a park.
6. Banská Štiavnica: an old mining town on steep hillsides, a white baroque Calvary with chapels on a hill, small blue mountain lakes in the forest.
7. Orava Castle perched high on a vertical rocky cliff above a river; a small dark wooden church; a tiny forest steam train.
8. Vlkolínec: a hamlet of log houses with a wooden bell tower; further on, an outdoor aquapark with pools and slides near a lake.
9. The High Tatras: jagged granite peaks, a mountain lake with rowing boats, a few tents in a campsite, a marmot.
10. Slovak Paradise: a narrow forest gorge with metal ladders beside waterfalls, an ice-cave entrance.
11. Spiš Castle: huge white castle ruins spread over a hilltop, a walled town with a Gothic church nearby.
12. Bardejov: a long square of colourful gabled houses around a Gothic church and a small town hall.
13. Prešov: a long, spindle-shaped main street with a Gothic church, a little house with a garden, old wooden salt-works buildings.
14. Košice: the Gothic St Elisabeth Cathedral with a colourful glazed-tile roof, a fountain in front.
15. Bottom: the road leaves through the bottom edge towards a warm sunset, like the way home.

Rolling green hills, forests, fields and rivers fill the space between landmarks; mountains are bigger towards the middle (Tatras). Keep the road and the areas right next to each landmark uncluttered.

No text, no letters, no labels, no signs, no flags, no logos, no map legend, no compass, no frame or border, no people in the foreground, no animal characters in clothes.
```
