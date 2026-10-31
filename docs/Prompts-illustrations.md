# Illustrations IA du roadtrip — prompts Gemini

Une illustration par chapitre, pour la **fiche 05** (l'épisode), plus une pour le kit (la première rencontre). La fiche 06 viendra peut-être ensuite. Les autres fiches gardent leur photo Wikimedia Commons.

**Style** : dessin animé 2D classique (pas de 3D), personnages animaux, décors peints réalistes pour que les lieux soient reconnaissables.

## Méthode

1. **Planche de personnages** : dans Gemini, joindre `docs/illustrations/ref_gab_pixel.jpg` puis `docs/illustrations/ref_andrea_pixel.jpg`, coller le prompt « Planche ». Garder la meilleure : `docs/illustrations/planche-personnages.jpg` (faite le 31 octobre).
2. **Chaque scène** : joindre **la planche** + **la photo de référence** du lieu (lien Commons donné), coller le prompt de la scène. Chaque prompt est complet : rien d'autre à ajouter.
3. Si un personnage dérive (couleurs, vêtements, oreille d'Andrea), le redemander en citant la planche : « keep the characters exactly as in the model sheet ».
4. Déposer l'image dans `img/illus_<NN>_<lieu>.jpg` (1920×1080 ou réduite à 1280 px de large). Je l'intègre ensuite dans la fiche 05, avec le crédit.

**Crédits** : « Illustration générée avec Google Gemini, d'après une photo de <auteur> (Wikimedia Commons, <licence>) ». Une image faite d'après une photo CC BY-SA en est une œuvre dérivée : elle reste sous CC BY-SA, avec le nom du photographe (voir `img/credits.md`).

## Les personnages

| | Personnage | Description à garder |
|---|---|---|
| 🦊 | Gab | renard roux, la quarantaine, pointes d'oreilles gris foncé, quelques poils gris aux joues ; sweat zippé bleu, T-shirt blanc, sac à dos aux bretelles jaunes |
| 🐰 | Andrea | hase grise, la quarantaine, bande blanche du front au museau, oreille gauche tombante (à droite sur l’image de référence) ; haut vert menthe |
| 🦊🧢 | Hugo | renardeau, 9 ans ; casquette rouge, T-shirt rayé |
| 🐇 | Lola | petite hase, 6 ans, fourrure sable clair (pas grise, pas de bande blanche) ; robe jaune |
| 🧑 | Les humains | adultes ordinaires, même style 2D, désignés par leur fonction (hôte, guide…) |

---

## Planche de personnages

```
Character model sheet for an animated film, on a plain light background, four characters standing side by side at the same scale, each shown front view and three-quarter view, full body, with a few facial expressions (smiling, surprised, annoyed):

1. Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps). Use the first attached image (pixel-art fox in a blue hoodie) as the design reference, but make him older and draw him in the style below.
2. Andrea, an adult female grey hare in her forties (grey fur, a white blaze from forehead to muzzle, long ears with pink insides, her left ear folded down, calm amused look), wearing a mint-green top. Use the second attached image (pixel-art grey hare in a mint top) as the design reference, older, in the style below.
3. Hugo, a 9-year-old fox cub (same orange fur and grey ear tips as Gab, lively and mischievous), wearing a red baseball cap and a striped T-shirt. He is Gab's nephew: same species and colours as Gab, smaller and rounder.
4. Lola, a 6-year-old little hare (light sandy-brown fur, white tummy, big ears, cheeky smile), wearing a yellow summer dress. She is Hugo's little sister; their mother is a hare. Clearly different from Andrea: smaller, sandy-brown, no white blaze.

Height: Gab and Andrea about the same height; Hugo reaches Gab's chest; Lola reaches Hugo's shoulder.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Warm, gentle summer light. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---

## Couverture — l'image d'intro

Pour l'introduction (`md/00_Introduction_01_slovaquie.md`) → image `img/illus_cover.jpg`

**À joindre** : la planche seulement.

```
Use the attached model sheet for the characters (keep them exactly as designed).

Scene: Opening image of an animated road movie across Slovakia. A small, slightly dusty light-blue family car with a roof box drives along a winding country road through green summer hills, seen from slightly above and in front. Gab is driving, smiling but already a little tired; Andrea sits next to him holding an unfolded paper road map, amused; in the back, Hugo leans out of the open window with his cap almost flying off, and Lola presses her face against the other window, wide-eyed. Behind them, far away, Bratislava Castle (white, square, four corner towers, red roofs) on its hill above the Danube; ahead of them, on the horizon, the jagged peaks of the High Tatras. Fields, forests, a village with a church spire, a few castle ruins on hilltops along the way. Leave the upper third of the image fairly calm (sky with a few summer clouds), as a title may be added later.

Characters: Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps); Andrea, an adult female grey hare in her forties (grey fur, a white blaze from forehead to muzzle, long ears with pink insides, her left ear folded down, calm amused look), wearing a mint-green top; Hugo, a 9-year-old fox cub (same orange fur and grey ear tips as Gab, lively and mischievous), wearing a red baseball cap and a striped T-shirt; Lola, a 6-year-old little hare (light sandy-brown fur, white tummy, big ears, cheeky smile), wearing a yellow summer dress.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Backgrounds are detailed, realistic painted backdrops, true to Slovakia's real landscapes and landmarks. Warm, gentle summer light. 16:9 landscape, 1920×1080. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---

## 00. Kit — la première rencontre

Fiche : `md/10_Series_00_KitSurvie_03_dialogue.md` → image `img/illus_00.jpg`

**Photo à joindre** : [Hviezdoslavovo_námestie_(10266936594).jpg](https://commons.wikimedia.org/wiki/File:Hviezdoslavovo_námestie_(10266936594).jpg)

```
Use the attached model sheet for the characters (keep them exactly as designed) and the attached photo as the reference for the place: Hviezdoslavovo námestie in Bratislava (long tree-lined square, the Slovak National Theatre at the end).

Scene: Many years ago, the very first meeting. On the square, Gab, holding a small French–Slovak phrasebook, greets Andrea very politely, a little stiff and formal; she answers with an amused, kind smile. Both look about ten years younger than in the rest of the story. Passers-by in the background.

Characters: Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps); Andrea, an adult female grey hare in her forties (grey fur, a white blaze from forehead to muzzle, long ears with pink insides, her left ear folded down, calm amused look), wearing a mint-green top.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Backgrounds are detailed, realistic painted backdrops, so that the real place is instantly recognisable: keep its architecture, proportions, colours and surroundings faithful to the reference photo. Warm, gentle summer light. 16:9 landscape, 1920×1080. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---

## 01. Bratislava — le soir à la cave

Fiche : `md/10_Series_01_Bratislava_05_vecer-v-pivnici.md` → image `img/illus_01.jpg`

**Photo à joindre** : aucune (intérieur), seulement la planche.

```
Use the attached model sheet for the characters (keep them exactly as designed). Place: an old vaulted wine cellar in the Small Carpathians, stone vault, big oak barrels, a long wooden table, warm candle light.

Scene: Evening toast. Andrea and Gab raise wine glasses; Hugo and Lola have small chunky tumblers (not wine glasses) of pale golden white-grape juice, clearly a children's drink with straws; the adults' wine is in stemmed glasses. Lola lifts her tumbler very, very high and spills the golden juice all over Hugo, who is soaked and outraged. Gab's backpack hangs on his chair and his phone is ringing on the table.

Characters: Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps); Andrea, an adult female grey hare in her forties (grey fur, a white blaze from forehead to muzzle, long ears with pink insides, her left ear folded down, calm amused look), wearing a mint-green top; Hugo, a 9-year-old fox cub (same orange fur and grey ear tips as Gab, lively and mischievous), wearing a red baseball cap and a striped T-shirt; Lola, a 6-year-old little hare (light sandy-brown fur, white tummy, big ears, cheeky smile), wearing a yellow summer dress.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Backgrounds are detailed, realistic painted backdrops, believable and true to Slovakia. Warm, gentle summer light. 16:9 landscape, 1920×1080. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---

## 02. Trenčín — la pension

Fiche : `md/10_Series_02_Trencin_05_penzion.md` → image `img/illus_02.jpg`

**Photo à joindre** : [Trenciansky_hrad_(2007).jpg](https://commons.wikimedia.org/wiki/File:Trenciansky_hrad_(2007).jpg)

```
Use the attached model sheet for the characters (keep them exactly as designed) and the attached photo as the reference for the place: Trenčín Castle on its rock with the tall square Matúš tower, seen at dusk through the small window of the room.

Scene: A small, simple guesthouse room with three beds: two small ones and one big one. Hugo and Lola both stand on the same small bed, fighting over it; Gab, arms spread, assigns the beds like a referee. Through the window, the castle lit up at dusk.

Characters: Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps); Hugo, a 9-year-old fox cub (same orange fur and grey ear tips as Gab, lively and mischievous), wearing a red baseball cap and a striped T-shirt; Lola, a 6-year-old little hare (light sandy-brown fur, white tummy, big ears, cheeky smile), wearing a yellow summer dress.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Backgrounds are detailed, realistic painted backdrops, so that the real place is instantly recognisable: keep its architecture, proportions, colours and surroundings faithful to the reference photo. Warm, gentle summer light. 16:9 landscape, 1920×1080. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---

## 03. Kremnica — les pièces

Fiche : `md/10_Series_03_Bojnice_05_kremnica.md` → image `img/illus_03.jpg`

**Photo à joindre** : [Kremnica,_mincovňa.jpg](https://commons.wikimedia.org/wiki/File:Kremnica,_mincovňa.jpg)

```
Use the attached model sheet for the characters (keep them exactly as designed) and the attached photo as the reference for the place: the old Mint of Kremnica (historic building on the sloping town square of a small mining town in the mountains).

Scene: In front of the old mint, Hugo proudly holds up a shiny golden collector's coin; Lola, jealous, shows the single euro coin in her paw; Gab counts his change; Andrea explains, pointing at the building.

Characters: Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps); Andrea, an adult female grey hare in her forties (grey fur, a white blaze from forehead to muzzle, long ears with pink insides, her left ear folded down, calm amused look), wearing a mint-green top; Hugo, a 9-year-old fox cub (same orange fur and grey ear tips as Gab, lively and mischievous), wearing a red baseball cap and a striped T-shirt; Lola, a 6-year-old little hare (light sandy-brown fur, white tummy, big ears, cheeky smile), wearing a yellow summer dress.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Backgrounds are detailed, realistic painted backdrops, so that the real place is instantly recognisable: keep its architecture, proportions, colours and surroundings faithful to the reference photo. Warm, gentle summer light. 16:9 landscape, 1920×1080. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---

## 04. Banská Štiavnica — le tajch

Fiche : `md/10_Series_04_Stiavnica_05_tajch.md` → image `img/illus_04.jpg`

**Photo à joindre** : [Počúvadlianske_jazero_01.jpg](https://commons.wikimedia.org/wiki/File:Počúvadlianske_jazero_01.jpg)

```
Use the attached model sheet for the characters (keep them exactly as designed) and the attached photo as the reference for the place: Počúvadlo, a dark, calm mountain lake surrounded by forest.

Scene: Late afternoon at the lake. Hugo and Lola stand in the cold water splashing Gab, who is still on the shore, fully dressed and already dripping wet, about to give up and jump. Andrea, sitting on the jetty, laughs.

Characters: Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps); Andrea, an adult female grey hare in her forties (grey fur, a white blaze from forehead to muzzle, long ears with pink insides, her left ear folded down, calm amused look), wearing a mint-green top; Hugo, a 9-year-old fox cub (same orange fur and grey ear tips as Gab, lively and mischievous), wearing a red baseball cap and a striped T-shirt; Lola, a 6-year-old little hare (light sandy-brown fur, white tummy, big ears, cheeky smile), wearing a yellow summer dress.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Backgrounds are detailed, realistic painted backdrops, so that the real place is instantly recognisable: keep its architecture, proportions, colours and surroundings faithful to the reference photo. Warm, gentle summer light. 16:9 landscape, 1920×1080. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---

## 05. Orava — le train de quinze heures

Fiche : `md/10_Series_05_Orava_05_vlak-o-tretej.md` → image `img/illus_05.jpg`

**Photo à joindre** : [Tanečník_-_railway_carriage.JPG](https://commons.wikimedia.org/wiki/File:Tanečník_-_railway_carriage.JPG)

```
Use the attached model sheet for the characters (keep them exactly as designed) and the attached photo as the reference for the place: the small Orava forest railway: a tiny narrow-gauge train with open wooden carriages at a little station in a pine forest.

Scene: The little train is about to leave. Andrea, Hugo and Lola run along the platform; Gab runs last, out of breath, one arm up: "wait for me!". A station clock shows almost three o'clock.

Characters: Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps); Andrea, an adult female grey hare in her forties (grey fur, a white blaze from forehead to muzzle, long ears with pink insides, her left ear folded down, calm amused look), wearing a mint-green top; Hugo, a 9-year-old fox cub (same orange fur and grey ear tips as Gab, lively and mischievous), wearing a red baseball cap and a striped T-shirt; Lola, a 6-year-old little hare (light sandy-brown fur, white tummy, big ears, cheeky smile), wearing a yellow summer dress.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Backgrounds are detailed, realistic painted backdrops, so that the real place is instantly recognisable: keep its architecture, proportions, colours and surroundings faithful to the reference photo. Warm, gentle summer light. 16:9 landscape, 1920×1080. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---

## 06. Liptov — Tatralandia

Fiche : `md/10_Series_06_Liptov_05_tatralandia.md` → image `img/illus_06.jpg`

**Photo à joindre** : [Aquapark_Tatralandia_(16).jpg](https://commons.wikimedia.org/wiki/File:Aquapark_Tatralandia_(16).jpg)

```
Use the attached model sheet for the characters (keep them exactly as designed) and the attached photo as the reference for the place: the Tatralandia aquapark: outdoor thermal pools, colourful water slides, mountains behind.

Scene: On the right of the pool, three open water slides come down a grassy slope side by side, straight into the pool; the middle one is bright yellow. Gab, in blue swim shorts, is sliding down the yellow one, near the bottom, feet first towards the pool, lying on his back with his arms raised, delighted, his tail flying behind him; a big splash where the slide meets the water. In the pool, Hugo, wearing a red long-sleeved swim shirt and his red cap, cheers with both arms up; Lola, wearing a yellow long-sleeved swim shirt and orange armbands, floats in an inflatable ring. Andrea, in a mint-green T-shirt, sits at the pool edge with her feet in the water, amused. Other families in the background.

Characters: Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps); Andrea, an adult female grey hare in her forties (grey fur, a white blaze from forehead to muzzle, long ears with pink insides, her left ear folded down, calm amused look), wearing a mint-green top; Hugo, a 9-year-old fox cub (same orange fur and grey ear tips as Gab, lively and mischievous), wearing a red baseball cap and a striped T-shirt; Lola, a 6-year-old little hare (light sandy-brown fur, white tummy, big ears, cheeky smile), wearing a yellow summer dress.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Backgrounds are detailed, realistic painted backdrops, so that the real place is instantly recognisable: keep its architecture, proportions, colours and surroundings faithful to the reference photo. Warm, gentle summer light. 16:9 landscape, 1920×1080. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---

## 07. Tatras — le camping

Fiche : `md/10_Series_07_Tatry_05_kemp.md` → image `img/illus_07.jpg`

**Photo à joindre** : [Panorama_High_Tatras_from_Poprad.jpg](https://commons.wikimedia.org/wiki/File:Panorama_High_Tatras_from_Poprad.jpg)

```
Use the attached model sheet for the characters (keep them exactly as designed) and the attached photo as the reference for the place: the jagged High Tatras peaks behind a campsite at the edge of a forest.

Scene: Evening at the campsite, other tents and cars further away. In the foreground, a small beige dome tent that Gab has pitched wrongly: it lies tipped over on its side like a fallen barrel, its dark grey floor standing up as a vertical wall, and its zipped door on the very top, facing the sky. Gab stands proudly next to it, hands on his hips, as if it were perfect. Hugo points up at the door on top of the tent, laughing; Lola giggles behind her paws; Andrea, arms crossed, raises an eyebrow. The instruction sheet lies forgotten on the grass. Dark storm clouds gather over the peaks.

Characters: Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps); Andrea, an adult female grey hare in her forties (grey fur, a white blaze from forehead to muzzle, long ears with pink insides, her left ear folded down, calm amused look), wearing a mint-green top; Hugo, a 9-year-old fox cub (same orange fur and grey ear tips as Gab, lively and mischievous), wearing a red baseball cap and a striped T-shirt; Lola, a 6-year-old little hare (light sandy-brown fur, white tummy, big ears, cheeky smile), wearing a yellow summer dress.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Backgrounds are detailed, realistic painted backdrops, so that the real place is instantly recognisable: keep its architecture, proportions, colours and surroundings faithful to the reference photo. Warm, gentle summer light. 16:9 landscape, 1920×1080. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---

## 08. Slovenský raj — le jardin

Fiche : `md/10_Series_08_Raj_05_co-by-si-chcel.md` → image `img/illus_08.jpg`

**Photo à joindre** : [Hrabušice,_obec_a_Vysoké_Tatry.JPG](https://commons.wikimedia.org/wiki/File:Hrabušice,_obec_a_Vysoké_Tatry.JPG)

```
Use the attached model sheet for the characters (keep them exactly as designed) and the attached photo as the reference for the place: a village at the edge of the Slovak Paradise, with the High Tatras on the horizon.

Scene: Evening in the garden of a guesthouse: a wooden table with tea and homemade cakes. Gab yawns, Hugo and Lola talk with their mouths full. Andrea, a cup in her paws, looks dreamily at the distant mountains, thinking of her home town.

Characters: Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps); Andrea, an adult female grey hare in her forties (grey fur, a white blaze from forehead to muzzle, long ears with pink insides, her left ear folded down, calm amused look), wearing a mint-green top; Hugo, a 9-year-old fox cub (same orange fur and grey ear tips as Gab, lively and mischievous), wearing a red baseball cap and a striped T-shirt; Lola, a 6-year-old little hare (light sandy-brown fur, white tummy, big ears, cheeky smile), wearing a yellow summer dress.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Backgrounds are detailed, realistic painted backdrops, so that the real place is instantly recognisable: keep its architecture, proportions, colours and surroundings faithful to the reference photo. Warm, gentle summer light. 16:9 landscape, 1920×1080. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---

## 09. Spiš — « ujo zajačica »

Fiche : `md/10_Series_09_Spis_05_co-sme-robili.md` → image `img/illus_09.jpg`

**Photo à joindre** : [Spis_Castle_-_Slovakia.jpg](https://commons.wikimedia.org/wiki/File:Spis_Castle_-_Slovakia.jpg)

```
Use the attached model sheet for the characters (keep them exactly as designed) and the attached photo as the reference for the place: the huge white ruins of Spiš Castle on its hill, seen at dusk through the window of a village house.

Scene: Dinner at a host's house in Spišské Podhradie: soup and bread on the table. An elderly human host listens, amused. Hugo and Lola point at Gab, laughing; Gab, embarrassed, covers his face with a paw; Andrea smiles behind her spoon. The castle is visible through the window.

Characters: Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps); Andrea, an adult female grey hare in her forties (grey fur, a white blaze from forehead to muzzle, long ears with pink insides, her left ear folded down, calm amused look), wearing a mint-green top; Hugo, a 9-year-old fox cub (same orange fur and grey ear tips as Gab, lively and mischievous), wearing a red baseball cap and a striped T-shirt; Lola, a 6-year-old little hare (light sandy-brown fur, white tummy, big ears, cheeky smile), wearing a yellow summer dress.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Backgrounds are detailed, realistic painted backdrops, so that the real place is instantly recognisable: keep its architecture, proportions, colours and surroundings faithful to the reference photo. Warm, gentle summer light. 16:9 landscape, 1920×1080. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---

## 10. Bardejov — le skanzen

Fiche : `md/10_Series_10_Bardejov_05_kupele-a-skanzen.md` → image `img/illus_10.jpg`

**Photo à joindre** : [Bardejovské_Kúpele_skanzen_10_01.jpg](https://commons.wikimedia.org/wiki/File:Bardejovské_Kúpele_skanzen_10_01.jpg)

```
Use the attached model sheet for the characters (keep them exactly as designed) and the attached photo as the reference for the place: the open-air museum of Bardejovské Kúpele: old log houses and a dark wooden church among trees.

Scene: In the open-air museum, near the wooden church, Lola has found a cat sitting on an old cartwheel and shows it like a treasure ("almost a dragon!"); Hugo looks around for dragons; Gab and Andrea follow, Gab grimacing at a cup of mineral water.

Characters: Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps); Andrea, an adult female grey hare in her forties (grey fur, a white blaze from forehead to muzzle, long ears with pink insides, her left ear folded down, calm amused look), wearing a mint-green top; Hugo, a 9-year-old fox cub (same orange fur and grey ear tips as Gab, lively and mischievous), wearing a red baseball cap and a striped T-shirt; Lola, a 6-year-old little hare (light sandy-brown fur, white tummy, big ears, cheeky smile), wearing a yellow summer dress.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Backgrounds are detailed, realistic painted backdrops, so that the real place is instantly recognisable: keep its architecture, proportions, colours and surroundings faithful to the reference photo. Warm, gentle summer light. 16:9 landscape, 1920×1080. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---

## 11. Prešov — le sel

Fiche : `md/10_Series_11_Presov_05_sol.md` → image `img/illus_11.jpg`

**Photo à joindre** : [Sklad_soli,_Solivar,_Prešov.jpg](https://commons.wikimedia.org/wiki/File:Sklad_soli,_Solivar,_Prešov.jpg)

```
Use the attached model sheet for the characters (keep them exactly as designed) and the attached photo as the reference for the place: the old wooden salt-works buildings of Solivar in Prešov, with steep shingled roofs.

Scene: Inside a tall wooden building of the old salt works, a huge wooden horse-driven wheel under the roof beams. Andrea explains, pointing at the wheel; Hugo looks up, impressed; Lola pats the wooden frame ("poor horses"); Gab rubs his sore legs.

Characters: Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps); Andrea, an adult female grey hare in her forties (grey fur, a white blaze from forehead to muzzle, long ears with pink insides, her left ear folded down, calm amused look), wearing a mint-green top; Hugo, a 9-year-old fox cub (same orange fur and grey ear tips as Gab, lively and mischievous), wearing a red baseball cap and a striped T-shirt; Lola, a 6-year-old little hare (light sandy-brown fur, white tummy, big ears, cheeky smile), wearing a yellow summer dress.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Backgrounds are detailed, realistic painted backdrops, so that the real place is instantly recognisable: keep its architecture, proportions, colours and surroundings faithful to the reference photo. Warm, gentle summer light. 16:9 landscape, 1920×1080. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---

## 12. Košice — le dernier soir

Fiche : `md/10_Series_12_Kosice_05_buduce-leto.md` → image `img/illus_12.jpg`

**Photo à joindre** : [St_Elisabeth_Cathedral_Kosice.jpeg](https://commons.wikimedia.org/wiki/File:St_Elisabeth_Cathedral_Kosice.jpeg)

```
Use the attached model sheet for the characters (keep them exactly as designed) and the attached photo as the reference for the place: the Gothic St Elisabeth Cathedral of Košice with its colourful glazed-tile roof, seen at dusk from a terrace.

Scene: The last evening, on a terrace in the old town. Gab, tired but happy, holds his phone on speaker (a video call with the children's mother); Hugo leans in to shout into the phone; Lola, sleepy, leans against Andrea; Andrea smiles. The cathedral glows at dusk.

Characters: Gab, an adult male red fox in his forties (bright orange fur, grey-black ear tips, cream muzzle and chest, a few grey hairs on the cheeks, friendly slightly tired eyes), wearing a blue zip hoodie over a white T-shirt (his backpack has yellow straps); Andrea, an adult female grey hare in her forties (grey fur, a white blaze from forehead to muzzle, long ears with pink insides, her left ear folded down, calm amused look), wearing a mint-green top; Hugo, a 9-year-old fox cub (same orange fur and grey ear tips as Gab, lively and mischievous), wearing a red baseball cap and a striped T-shirt; Lola, a 6-year-old little hare (light sandy-brown fur, white tummy, big ears, cheeky smile), wearing a yellow summer dress.

Style: Classic 2D hand-drawn animated-film style (not 3D, not pixel art): clean ink outlines, flat colours with soft cel shading, expressive faces. Backgrounds are detailed, realistic painted backdrops, so that the real place is instantly recognisable: keep its architecture, proportions, colours and surroundings faithful to the reference photo. Warm, gentle summer light. 16:9 landscape, 1920×1080. Anthropomorphic animals walk upright, wear clothes and live among ordinary humans, who are drawn in the same 2D style and find this normal. No text, no letters, no speech bubbles, no logos, no watermark.
```

---
