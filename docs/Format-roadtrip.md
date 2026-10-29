# Format Roadtrip

Ce document décrit comment le contenu du roadtrip est écrit pour des **adultes francophones**, du niveau débutant (après l'introduction et le kit de survie) jusqu'à un **bon A2, avec des incursions vers le B1**. Il reprend le format de Zajka Friends (`docs/Format-friends.md` dans [Slovingo-sk-fr-friends](https://github.com/lstux/Slovingo-sk-fr-friends)) et indique ce qui change. L'histoire, les personnages et l'itinéraire sont dans `Concept-adulte.md` ; la progression dans `Progression-roadtrip.md`.

La base reste le **SMD (Slovingo Markdown)** : voir `docs/Format-SMD.txt` dans le repo [Slovingo](https://github.com/lstux/Slovingo/tree/main/docs).

## Ce qui change

| | Ancien cours adulte (branche `original`) | Friends | Roadtrip |
|---|---|---|---|
| Public | adultes, débutants | 12–16 ans, Kids supposé acquis | adultes, débutants (intro + kit de survie) |
| Forme | séries thématiques (famille, maison…) | un récit : une série = un chapitre | un récit : **une série = un chapitre = une journée de voyage** |
| Fiches 01 à 04 | phrases isolées | vocabulaire + grammaire + micro-dialogues | idem Friends |
| Fiches 05 et 06 | un dialogue court (~90 mots) | l'épisode, en deux parties | idem Friends |
| Narration | aucune | 💬 le Narrateur | 🧭 **la navigation (le GPS)**, avec repli possible sur 💬 un narrateur neutre |
| Personnages | humains (Eric, Andrea…) | animaux + humains adultes | animaux (Gab, Andrea, Hugo, Lola) + humains par fonction |
| Ton | neutre, scolaire | ado, ironique | **adulte, décalé** : gags de parents en vacances, tendresse, jamais cynique |
| Culture | coin slovaque | coin slovaque | **guide touristique** : chaque chapitre fait visiter de vrais lieux |

## 1. Ton et rédaction

- Phrases courtes, répliques vives. L'humour vient des situations de voyage (la valise, la pause pipi, le ronfleur, « on est arrivés ? »), jamais d'une moquerie sur des personnes réelles.
- Ton d'adulte : second degré, autodérision de Gab, patience d'Andrea, logique implacable des enfants.
- Une idée à la fois, pas de jargon grammatical dans le texte (« génitif », « perfectif »…), comme dans Friends.
- Le guide touristique passe par les personnages : Andrea raconte, les enfants demandent, le GPS annonce. Pas de paragraphe encyclopédique dans les dialogues ; les faits détaillés vont dans le **coin slovaque**.
- Le slovaque est celui qu'un adulte slovaque dirait, à faire relire par un locuteur natif.

## 2. Une série = 6 fiches = un chapitre = une journée

- **Fiches 01 à 04** : apprentissage (vocabulaire, un point de grammaire) avec des **micro-dialogues** qui font avancer la journée : départ, route, visite, repas, arrivée au logement.
- **Fiche 05** : première partie de l'épisode (dialogue).
- **Fiche 06 (« extra »)** : tableau complet du vocabulaire **et** suite de l'épisode, qui se termine en général par **la nuit** (le logement du soir).

Chaque chapitre doit pouvoir se lire d'un trait de la fiche 01 à la fiche 06.

## 3. Personnages, avatars et prénom

Le moteur associe **un nom par emoji** pour tout le cours, et les voix se règlent par emoji. **Chaque personnage a donc un marqueur unique.** Un marqueur peut combiner deux emojis, à condition de ne contenir aucune lettre.

| Avatar | Personnage | Notes |
|---|---|---|
| 🦊 | **Gab** (toi) | homme adulte, Français, oncle de Hugo et Lola ; prénom `[USER_NAME]` (par défaut *Gab*) ; formes **masculines** |
| 🐰 | **Andrea** | hase adulte, née à Prešov, amie de Gab ; formes **féminines** |
| 🦊🧢 | **Hugo** | renardeau, 9 ans, neveu de Gab *(avatar et âge proposés)* |
| 🐇 | **Lola** | petite hase, 6 ans, nièce de Gab *(avatar et âge proposés)* |
| 📱 | **Claire** | la mère des enfants, restée en France, au téléphone |
| 🧭 | **La navigation** (le GPS) | narratrice par défaut, voir §6 |
| 💬 | Le narrateur neutre | repli, voir §6 |
| à définir | La famille d'Andrea (Marta, Ivan, babka Zuzana) | chapitre 11 ; un marqueur unique chacun |
| 🧑‍… | Les humains | désignés par leur **fonction**, vouvoyés ; **un emoji par fonction** (voir ci-dessous) |

**Humains** : comme dans Friends, ils parlent normalement aux animaux et personne ne s'en étonne. Un même emoji ne peut pas servir à deux fonctions (le moteur leur donnerait le même nom). Propositions : 🧑‍💼 la réception (*recepčná*), 🧑‍🍳 le serveur (*čašník*), 🧓 l'hôte de la chata ou de la chambre chez l'habitant (*pán domáci*), 🧑‍🏫 le guide (*sprievodca*), 🧑‍🔧 le gardien du camping (*správca kempu*), 🧑‍🦰 la vendeuse (*predavačka*), 👵 une vieille dame du village (*stará pani*), 👷 le préposé de la remontée (*pracovník lanovky*). Animaux non-personnages : 🐓 le coq (*Kikirikí*), à valider. On complète la liste au fil de l'écriture et on la tient à jour ici.

**Tutoiement et vouvoiement** :
- *ty* entre Gab, Andrea et les enfants, et en famille (y compris chez Andrea) ;
- **exception voulue : le *vy* de Gab envers Andrea**. Il l'a longtemps vouvoyée avant de passer au *ty*, et il y retombe par habitude, surtout au début du voyage ou quand il est fatigué. Andrea le reprend. Chaque réplique où Gab vouvoie Andrea porte une remarque `+` qui le signale, pour que l'apprenant ne prenne pas cette forme pour la bonne (voir `Progression-roadtrip.md`, gags) ;
- *vy* avec tous les adultes inconnus (réception, serveurs, guides) ; les enfants vouvoient aussi les adultes ;
- la navigation vouvoie le conducteur (*Odbočte doprava*), comme une vraie navigation.

**Prénom** :
- `[ASK_USER_NAME]` reste dans l'introduction (`00_Introduction_04_qui-es-tu`). Ensuite, `[USER_NAME]` dans les répliques et la narration.
- Le nom par défaut (`site.user_name_default` dans `lang.json`) passera de *Eric* à *Gab* au moment de la fusion, avec l'adaptation du kit de survie et des deux annexes où « Eric » est écrit en dur.
- Un prénom saisi **ne se décline pas** : on l'emploie comme sujet ou pour appeler (*Ahoj, [USER_NAME]!*), jamais à l'accusatif ni au datif.
- Le marqueur va **après** le `!` : `! 🐰 Ahoj!`.

## 4. Genre

- Gab est un homme : formes masculines (*rád*, *sám*, *bol som*, *unavený*). Andrea et Lola : formes féminines. Hugo : masculines.
- Quand on parle de Gab ou de Hugo **comme animal**, on emploie *líška* (féminin) et on accorde avec le mot, comme dans Kids et Friends. Une remarque `+` le dit quand il le faut.
- La navigation se dit **navigácia** (féminin) : elle parle au féminin (*stratila som signál*). *À vérifier avec un locuteur natif.*
- Le cours reste écrit pour un apprenant au masculin (Gab). Le choix « renard ou hase » viendra plus tard, avec une évolution du moteur.

## 5. Écouter plutôt que lire

Mêmes règles que Friends :
- les consignes importantes en `{{fr:...}}`, une idée par bloc, une à trois phrases ;
- **pas de mot slovaque dans un `{{fr:...}}`** : le mot va à côté, en `{{...}}` ;
- exceptions : les prénoms et les **noms de lieux** du voyage (*Trenčín, Bojnice, Prešov*…) ;
- en français, on écrit les noms usuels (les Tatras, Košice) ; le nom slovaque (`{{Tatry}}`) n'est donné que pour l'apprendre ;
- pas de `**gras**` dans un `{{fr:...}}`.

## 6. La navigation 🧭 et le narrateur neutre 💬

La navigation est la **voix du voyage** : elle situe l'action (où on est, où on va, l'heure), annonce les étapes et donne des directions. Elle est **intégrée au dialogue**, avec son avatar, comme le Narrateur de Friends.

```
! 🧭 O dvesto metrov odbočte doprava.
> Dans deux cents mètres, tournez à droite.
> O dvesto metrov = dans deux cents mètres
> odbočte = tournez (vous)
> doprava = à droite
```

Règles :
- phrases **très courtes**, au **présent** tant que le passé n'est pas introduit ;
- ses formules (*odbočte*, *pokračujte rovno*, *prepočítavam trasu*, *cieľ je vpravo*) s'apprennent d'abord **en bloc**, avant que l'impératif soit expliqué (chapitre 05) ;
- **elle n'est pas toujours là** : sans réseau (camping des Tatras, grotte de glace, gorges du Slovenský raj, chez la famille d'Andrea), elle l'annonce (*Stratila som signál*), se tait ou boude, puis revient avec *Prepočítavam trasu…* ; le gag fait partie du personnage ;
- quand une scène a besoin d'être située sans elle, on prend le **narrateur neutre 💬**, même règles que dans Friends ; on peut aussi basculer toute la série sur lui si la navigation s'essouffle ;
- les deux apparaissent dans `## Les personnages` quand ils parlent dans la fiche ; si le moteur le permet, chacun a sa voix.

## 7. Structure des fichiers

```
md/
├── 00_Introduction_NN_titre.md        (inchangé : 5 fiches)
├── 10_Series_00_KitSurvie_NN_titre.md (à adapter : Gab et Andrea)
├── 10_Series_NN_Etape_YY_titre.md     (roadtrip : séries 01 à 12)
├── 10_Series_15+_Kronika_…            (inchangé)
├── 20_Vocabulary_NN_titre.md          (inchangé)
└── 90_Annex_NN_titre.md               (inchangé, sauf « Eric » à remplacer)
exercises/   un fichier .exercises.json par fiche
img/         photos et img/credits.md
```

Exemple : `10_Series_02_Trencin_01_na-ceste.md`.

- **Titres** : `# Série Trenčín (1/5) — Na ceste` ; extra : `# Trenčín (extra) — Penzión`.
- Le **thème** du nom de fichier donne la clé de `lang.json` → `subgroups`, `subgroup_themes` et `map.icons`, en minuscules et **sans diacritiques** (`Trenčín` → `trencin`). Les clés et noms affichés sont listés dans `Progression-roadtrip.md`.
- Les numéros 01 à 12 ne gênent pas les Kronika, qui commencent à 15.
- Noms de fichiers sans accent ; titres avec.

## 8. Vocabulaire

- **Fiche d'apprentissage** : **7 à 8 mots** essentiels dans les chapitres 1 à 3 (on part de zéro), puis **9 à 10** ; plus 3 mots complémentaires. Un mot déjà vu (intro, kit, chapitre précédent) est marqué « (rappel) ».
- **Fiche 05** : au plus **5 mots nouveaux**, toujours signalés : `+ Mot nouveau signalé : {{…}} = …`.
- **Fiche 06** : au plus **3 mots nouveaux**, signalés et ajoutés au tableau récapitulatif.
- Au plus **une** forme « à écouter » (pas encore apprise) par fiche de dialogue, signalée par `+ À écouter : …`. Les formules de la navigation comptent comme des blocs à retenir, pas comme des formes « à écouter ».
- Aucun mot inconnu non signalé, navigation et narrateur compris.
- Les noms de lieux ne comptent pas comme mots nouveaux, mais leurs formes déclinées (*v Trenčíne*, *do Bojníc*) sont données en morceaux, avec la décomposition.
- Les cas ne sont pas expliqués comme tels : on donne des morceaux à retenir (*na hrade*, *do mesta*, *u Andrey*).

## 9. Fiche d'apprentissage (01 à 04)

Même squelette que Friends :

```markdown
# Série Trenčín (1/5) — Na ceste

@ TODO_img/nom.jpg | TODO : choisir une photo (…) sur Wikimedia Commons

(fiche 01 seulement : la carte du jour, voir ci-dessous)

{{fr:Courte intro (1 à 2 phrases) qui situe la journée.}}

---

## Les nouveaux mots
| Slovenčina | Français |
|------------|----------|
| … | … |

---

## Aujourd'hui on apprend…
### Un point de grammaire
Explication en quelques phrases, tableau d'exemples.

---

## Le dialogue
(micro-dialogue de 3 à 6 cartes avec avatars, navigation comprise)

---

## 🇸🇰 Coin slovaque
2 courts paragraphes sur le lieu du jour, mots-clés en {{…}}

---

## Vocabulaire complémentaire
(3 mots)

---

## Encore quelques répliques
(2 cartes qui réutilisent les mots complémentaires)
```

**La carte du jour** : la fiche 01 de chaque série commence, juste après le titre et l'image, par une **carte Leaflet du trajet de la journée** (bloc `%~`, points numérotés dans l'ordre) ; les fiches suivantes peuvent ajouter une carte d'épingles (`%:`) pour les lieux visités en ville. Coordonnées à régler avec `tools/geomap-editor.html` du moteur ; syntaxe dans `docs/Format-SMD.txt`, §5.

```
%~ Deň 2 : z Bratislavy do Trenčína
% 48.1439, 17.1097 | {{Bratislava}}
% 48.5944, 17.8275 | {{Piešťany}}
% 48.8945, 18.0444 | {{Trenčiansky hrad}}
```

*(Coordonnées de l'exemple approximatives.)*

Les micro-dialogues font **3 à 5 répliques au début du voyage, jusqu'à 8 vers la fin**. La section `## Le dialogue` ne contient que des cartes avec avatar : le moteur la reconnaît comme dialogue.

## 10. Fiches 05 et 06 : l'épisode

**Fiche 05** :
- `## Vocabulaire du dialogue` (au plus 5 mots nouveaux) ;
- `## Les personnages` : avatar + nom (`- 🧭 Navigácia`, `- 🦊🧢 Hugo`…) ;
- `## Le dialogue` : l'épisode, **12 à 15 répliques** au chapitre 1, **15 à 20** jusqu'au chapitre 4, puis jusqu'à **30–40** vers la fin ;
- Coin slovaque.

**Fiche 06 (extra)** :
- `## Tout le vocabulaire de la série` : le tableau complet ;
- `## Les personnages` ;
- `## La suite de l'épisode` : la suite et la fin de la journée, souvent **la nuit au logement** ; même longueur que la 05 ; **3 mots nouveaux au maximum**, signalés ; les exercices ne portent que sur les répliques sans mot nouveau ;
- Coin slovaque.

## 11. Cartes audio

Comme Friends :

```
! Koľko to stojí?
> Combien ça coûte ?
> Koľko = combien
> to = ça
> stojí = coûte
+ Remarque utile.
```

- Première ligne `>` : traduction naturelle ; lignes suivantes : décomposition **une ligne par élément**.
- Lignes `+` : remarque, mot nouveau, astuce.
- Dialogues : `! 🐰 Ahoj!` (avatar après le `!`).

## 12. Photos

```
@ img/nom.jpg | Légende : sujet. Source : Wikimedia Commons
```

- **Photos réelles** des lieux du voyage (paysages, monuments, rues), une par fiche, choisies une à une sur Wikimedia Commons, avec auteur et licence dans `img/credits.md`. ~600-800 px de large.
- Tant que la photo n'est pas choisie : `@ TODO_img/choisir-image.jpg | TODO : choisir une photo (…)`.
- Les photos de l'ancien cours restées dans `img/` (Tatras, Štrbské pleso, Lomnický štít, halušky, Kofola, trams de Košice…) peuvent être réutilisées.
- Pas d'illustrations de personnages pour l'instant.
- Le téléchargement depuis Commons se fait **lentement** (une requête à la fois, avec des pauses) pour éviter les erreurs 429.

## 13. Coin slovaque

Court, **vérifiable** (pas de chiffre approximatif), relié au **lieu du jour** : une date, une légende, une spécialité, un usage, un mot. C'est la partie « guide » du cours. Les faits sont vérifiés sur des sources sérieuses (sites officiels, UNESCO, offices de tourisme). Les **lieux touristiques réels** (Tatralandia, l'Hôtel des Monnaies de Kremnica…) sont nommés ; pas de marque de produit ni de personnalité réelle dans les dialogues.

## 14. Qualité de langue

- **Français** : naturel, adulte.
- **Slovaque** : celui qu'un adulte slovaque dirait. À faire relire.
- **Pièges** : ceux de Kids et Friends restent valables. En plus, pour le roadtrip :

| ❌ | ✅ |
|----|----|
| Sme arrivés? (calque du français) | Už sme tam? |
| Idem do Trenčín | Ideme do Trenčína. (*do* + génitif, en morceau) |
| Som v Trenčín | Som v Trenčíne. (*v* + locatif, en morceau) |
| Chcem jeden pivo | Dám si jedno pivo. (*pivo* est neutre ; *dám si* au restaurant) |
| GPS hovorí (si on veut un personnage féminin) | Navigácia hovorí. |

## 15. Exercices faits main

Comme Friends : écrits à la main dans `exercises/<nom de la fiche>.exercises.json`, avec `"mode": "replace"` et `"sync": "full"` ; que du déjà vu ; une seule bonne réponse ; distracteurs qui ciblent les vraies confusions d'un francophone (*v / na*, *rád / rada*, *euro / eurá / eur*) ; les 5 types quand la fiche s'y prête ; `[USER_NAME]` n'est jamais un trou ni une réponse. Les répliques de la navigation et du narrateur peuvent servir à l'écoute, mais ni de trou ni de réponse piège.

## 16. Vérifier avant de publier

- [ ] Photo choisie (ou TODO explicite), crédits dans `img/credits.md`
- [ ] Fiche 01 : carte du trajet du jour
- [ ] 7-8 (ch. 1-3) ou 9-10 nouveaux mots + 3 complémentaires ; 5 au plus en 05, 3 au plus en 06
- [ ] Cartes décomposées une ligne par élément
- [ ] Aucun mot inconnu non signalé (navigation et narrateur compris)
- [ ] Un marqueur unique par personnage, `! 🐰 …` après le `!`
- [ ] Formes masculines pour Gab et Hugo, féminines pour Andrea, Lola et la navigation
- [ ] *ty / vy* respectés (inconnus vouvoyés, navigation au *vy*) ; tout *vy* de Gab envers Andrea est signalé par un `+`
- [ ] Coin slovaque : faits vérifiés sur le lieu du jour
- [ ] Fiche extra : tableau complet, suite de l'épisode, 3 mots nouveaux au plus
- [ ] Nom de fichier et titre selon le schéma, sous-groupe déclaré dans `lang.json`
- [ ] Slovaque relu par un locuteur natif
- [ ] Ton : décalé, tendre, jamais cynique

Build local (depuis le repo [Slovingo](https://github.com/lstux/Slovingo)) :

```
python3 src/build.py --lang-dir ../slovingo-sk-fr --static-dir static
```

Après une modification de fiche, relancer `python3 src/sync_exercises.py --lang-dir ../slovingo-sk-fr`.
