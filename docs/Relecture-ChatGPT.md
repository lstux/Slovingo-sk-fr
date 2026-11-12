# Relecture éditoriale de Slovingo-sk-fr

**Document de travail — première passe ChatGPT**  
**Dépôt :** \`lstux/Slovingo-sk-fr\`  
**Cours :** Ahoj Slovenčina! Zo západu na východ — cours de slovaque pour francophones, sous forme de roadtrip  
**Périmètre :** introduction, kit de survie, douze séries du roadtrip, documents de concept / format / progression, histoire complète, configuration, crédits et inventaire des exercices. Les fiches Kronika et le vocabulaire complémentaire ont aussi été parcourus par sondage, mais ne font pas ici l'objet d'une correction exhaustive ligne par ligne.

> Cette relecture est une passe éditoriale et pédagogique, pas une validation linguistique native. Je peux repérer des erreurs manifestes, des incohérences et des traductions suspectes ; les nuances de slovaque naturel, en particulier le šariš de babka Zuzana, restent à confirmer par une locutrice ou un locuteur natif.

## 1. Bilan général

Le roadtrip est une très bonne évolution du cours adulte initial. Il a une identité claire : on apprend le slovaque parce qu'on en a besoin au fil d'un vrai voyage, et chaque étape apporte un décor, du vocabulaire et une petite situation mémorable.

Ce qui fonctionne particulièrement bien :

- **Le fil narratif est simple et efficace.** Douze jours, de Bratislava à Košice, avec une progression géographique facile à suivre.
- **Les personnages ont une vraie dynamique.** Gab est autodérisoire, Andrea connaît le pays et le taquine, les enfants posent les questions que se poserait un apprenant.
- **Les gags reviennent sans lasser.** « Už sme tam? », le ronfleur, les pauses pipi, le GPS qui recalcule et le vouvoiement accidentel de Gab forment une vraie continuité.
- **Les lieux sont concrets.** Le cours fait découvrir la Slovaquie en même temps qu'il enseigne la langue ; les Coins slovaques apportent une vraie valeur touristique et culturelle.
- **La progression grammaticale est réfléchie.** Les cas sont abordés par blocs utiles, les temps arrivent progressivement, et les explications évitent autant que possible le jargon.
- **Le cours assume son public adulte.** L'humour est tendre et décalé, sans prendre l'apprenant pour un enfant.

Je ne recommande donc pas de refonte. Les priorités sont plutôt :
1. corriger quelques erreurs de traduction ou d'explication ;
2. sécuriser les affirmations grammaticales et phonétiques ;
3. faire valider les expressions signalées dans le document de relecture native ;
4. harmoniser les documents qui décrivent encore une version antérieure du cours ;
5. clarifier le statut des exercices et des séries Kronika.

## 2. Corrections prioritaires

| Priorité | Fichier / emplacement | Observation | Proposition |
|---|---|---|---|
| Haute | \`md/10_Series_07_Tatry_01_predpoved-pocasia.md\` — « Ak… » | L'explication traduit \`ak bude\` par « s'il y aura ». C'est faux en français : après le « si » conditionnel, on emploie le présent. | Écrire : « En slovaque, on emploie ici le futur après \`ak\` : \`Ak bude búrka\` = « s'il y a un orage ». En français, on dit bien « s'il y a », pas « s'il y aura ». » |
| Haute | \`md/10_Series_08_Raj_03_sysle.md\` — décomposition | \`Z dier vykúkajú malé zvieratká\` est traduit par « Des trous pointent la tête des trous » dans la décomposition actuelle. Ce sont les petites bêtes qui sortent la tête des trous. | Traduire : « De petits animaux pointent le bout de leur nez hors des trous » ; décomposer \`z dier\` = hors des trous, \`vykúkajú\` = passent la tête / regardent dehors. |
| Haute | \`md/00_Introduction_04_prononciation.md\` — lettre H | « h aspiré léger » est une comparaison trompeuse pour un francophone : le h aspiré français est muet, alors que le \`h\` slovaque se prononce. | Dire « un h audible, produit avec un souffle » et préciser qu'il n'a pas d'équivalent exact en français. Faire valider la description phonétique par un natif. |
| Haute | \`md/10_Series_10_Bardejov_02_namestie.md\` — UNESCO | \`Celé námestie je v UNESCO\` (« toute la place est à l'UNESCO ») est imprécis : c'est le centre historique de Bardejov, avec le faubourg juif, qui est inscrit au patrimoine mondial. | Préférer \`Historické centrum Bardejova je zapísané v zozname svetového dedičstva UNESCO.\` (« Le centre historique de Bardejov est inscrit au patrimoine mondial de l'UNESCO. ») |
| Haute | \`lang.json\` — \`story.user_name\` | Le prénom de l'histoire complète est encore \`Eric\`, alors que le personnage du cours est Gab et que \`site.user_name_default\` vaut \`Gab\`. | Harmoniser avec Gab, ou vérifier si cette valeur sert à un usage spécifique de l'ancienne histoire. |
| Moyenne | \`md/10_Series_06_Liptov_04_v-obchode.md\` | \`plavky\` est pluriel en slovaque, alors que plusieurs traductions françaises sont au singulier (« ce maillot », « il ne me plaît pas »). Le français naturel au singulier est compréhensible, mais l'apprenant risque de ne pas comprendre l'accord pluriel en slovaque. | Ajouter une remarque pédagogique : \`plavky\` s'emploie au pluriel en slovaque, même si l'on traduit naturellement par « un maillot de bain » en français. |
| Moyenne | \`md/10_Series_04_Stiavnica_03_v-restauracii.md\` et \`docs/Format-roadtrip.md\` §13 | Le dialogue contient \`Dám si kofolu\`, alors que la règle éditoriale indique qu'on ne nomme pas de marque de produit dans les dialogues. Kofola est une marque, même si le nom est souvent employé pour désigner la boisson. | Décider explicitement si Kofola est une exception culturelle autorisée. Sinon, remplacer par \`kolu\` ou \`limonádu\`. |
| Moyenne | \`lang.json\` — \`subgroups\` | Le dépôt contient plusieurs séries Kronika (15, 17, 19, 21 à 27 et 29), mais la liste \`subgroups\` visible ne déclare que \`kronika_vstupdoeu\`. Les thèmes correspondants sont en revanche présents dans \`subgroup_themes\`. | Vérifier le comportement du build et déclarer les libellés manquants si ces séries doivent toutes être visibles dans la navigation. |
| Moyenne | \`exercises/\` | Le dossier ne contient que deux fichiers d'exercices JSON, alors que le README annonce des exercices pour chaque fiche et que le format décrit des exercices faits à la main. | Clarifier si les autres exercices sont générés automatiquement. Si oui, corriger la documentation ; sinon, il manque encore la majorité des fichiers annoncés. |
| Moyenne | \`docs/Concept-adulte.md\`, \`docs/Progression-roadtrip.md\`, \`docs/Histoire.md\` | Plusieurs « prochaines étapes » décrivent encore l'écriture de l'histoire et le découpage en fiches, alors que les douze séries existent déjà. | Actualiser les étapes et le statut du projet après la première passe de relecture. |
| Basse | \`md/00_Introduction_03_langue.md\` — tableau des communautés | Les entrées « Auvergne-Rhône-Alpes : une centaine (à vérifier) » et « Lyon : au moins une perle » mélangent information non vérifiée et clin d'œil personnel dans un tableau factuel. | Déplacer la plaisanterie dans une note clairement humoristique, ou retirer ces deux lignes du tableau. |
| Basse | \`img/credits.md\` | Plusieurs crédits des images de style sont encore « à compléter ». Le README le signale déjà. | Terminer les auteurs et licences manquants avant de considérer les crédits comme finalisés. |

## 3. Relecture de langue et de pédagogie

### 3.1. Introduction et prononciation

**Lettre H**

C'est le point phonétique le plus important à corriger dans la fiche. En français, « h aspiré » désigne une lettre non prononcée qui empêche certaines liaisons. Le \`h\` slovaque, lui, est audible. La comparaison peut donc induire l'apprenant en erreur.

Proposition :
« Le \`h\` se prononce : on entend un souffle dans la gorge. Il ne faut pas le confondre avec le h muet ou le h aspiré du français. »

La description exacte du son (consonne fricative voisée) peut rester hors du cours débutant ; l'essentiel est de ne pas faire croire que la lettre est silencieuse.

**Assourdissement final**

La fiche donne les exemples \`chlieb\` → « chliep » et \`hrad\` → « hrat », puis liste \`b, d, z, ž, h, v\`. La règle est utile, mais la liste paraît présentée comme exhaustive alors qu'elle ne l'est probablement pas.

Proposition éditoriale : introduire la liste par « notamment » ou « par exemple », puis faire vérifier par un natif si l'on souhaite présenter l'inventaire complet des consonnes concernées.

**Autres choix**

- « Le slovaque se lit presque comme il s'écrit » est une bonne phrase d'accroche, à condition de conserver les explications sur les consonnes molles, les voyelles longues et l'assourdissement.
- Les approximations françaises des sons sont adaptées à une première approche. Elles ne remplacent pas l'écoute, ce que la fiche rappelle déjà.
- La phrase « les syllabes gardent une longueur et une netteté assez régulières » est utile, mais ne doit pas laisser croire que toutes les voyelles ont la même durée : les voyelles longues restent distinctives.

### 3.2. Explications grammaticales

**Le futur après \`ak\` — correction à faire**

Dans Tatry 01, l'explication dit :
« Après \`ak\`, le futur, comme en français après “quand” : on dit \`ak bude\`, “s'il y aura”. »

Le slovaque \`Ak bude búrka\` est correct, mais la traduction française ne l'est pas. En français, dans une condition réelle, on dit « s'il y a un orage » et non « s'il y aura un orage ».

Formulation conseillée :
« En slovaque, on emploie le futur après \`ak\` : \`Ak bude búrka\` = « s'il y a un orage ». En français, on emploie le présent après « si » dans une condition. »

C'est une correction importante, car l'explication actuelle enseigne involontairement une faute de français.

**Les comparatifs**

Les fiches font bien de donner des séries comme \`malý → menší\`, \`veľký → väčší\`, puis \`krásny → krajší\`. Les formes irrégulières sont utiles à mémoriser en contexte. Je garderais toutefois la formulation « quelques comparatifs changent de forme » plutôt que de laisser croire que tous suivent un seul modèle.

**L'aspect verbal**

Le contraste entre \`robiť\` et \`urobiť\`, ou \`ísť hore\` et \`vyjsť\`, est une bonne porte d'entrée vers l'aspect. La métaphore « le chemin / le résultat » est pédagogique et accessible. Il faudra simplement éviter de la présenter comme une règle universelle couvrant tous les verbes perfectifs et imperfectifs.

**Les cas**

Le choix de ne pas présenter immédiatement les noms des cas, et de faire apprendre des blocs comme \`do Trenčína\`, \`v Trenčíne\`, \`na hrade\`, est cohérent avec l'objectif A2. C'est l'un des points forts du cours.

### 3.3. Traductions et naturel

**Raj 03 — \`Z dier vykúkajú malé zvieratká\`**

La décomposition française actuelle attribue l'action aux trous. Or le sujet grammatical est \`malé zvieratká\` : ce sont les petits animaux qui passent la tête hors des trous.

Proposition :
- \`Z dier\` = hors des trous ;
- \`vykúkajú\` = pointent le bout de leur nez / regardent dehors ;
- \`malé zvieratká\` = de petits animaux.

La traduction naturelle peut être : « De petites bêtes pointent le bout de leur nez hors des trous. »

**Liptov 04 — \`plavky\`**

Le choix du singulier en français est naturel, mais il masque le pluriel slovaque. C'est justement une occasion pédagogique utile : le mot \`plavky\` se comporte comme un pluriel, même quand on parle d'un seul maillot.

À ajouter dans la fiche :
« Attention : en slovaque, \`plavky\` est toujours au pluriel. On dit donc \`Páčia sa ti tieto plavky?\`, littéralement « ces maillots te plaisent-ils ? », même si le français dit naturellement « ce maillot te plaît ? ». »

**Bardejov 02 — \`Je ticho\`**

La traduction « C'est le silence » est compréhensible, mais peu naturelle en français dans la scène. Préférer « Tout est calme » ou « Il règne un silence ».

**Traductions à conserver comme traductions naturelles**

Le cours a raison de ne pas traduire systématiquement mot à mot. Par exemple, \`Už sme tam?\` peut devenir « On est arrivés ? », et \`Je to v poriadku\` « tout va bien ». Il faut seulement que les décompositions restent fidèles à la structure slovaque, sans attribuer une action au mauvais mot.

## 4. Points à confirmer avec une personne native

Le dépôt contient déjà un document très utile, \`docs/Relecture-locutrice.md\`, qui regroupe les questions les plus difficiles. Je recommande de le conserver comme référence et de ne pas remplacer cette validation par la présente relecture.

### 4.1. Le šariš de babka Zuzana

C'est le point le plus fragile du cours, et le document de relecture a raison de le placer en premier.

À faire confirmer :
- \`Ta co, deci?\`
- \`Hladne sce?\`
- \`Vidziš?\`
- \`Dzivče hutori jak ja!\`
- \`Ešče jeden!\`
- \`Ta co? Medvedz v obývačke?\`
- \`Ta jak medvedz.\`

Il faut vérifier non seulement que ces formes existent, mais qu'elles correspondent bien au parler de Prešov / du Šariš et qu'une grand-mère les emploierait naturellement. Il faut également faire confirmer l'affirmation sur l'accent tonique à l'avant-dernière syllabe : elle ne devrait pas être généralisée à tous les parlers de l'est sans nuance.

### 4.2. Expressions du quotidien et voix du GPS

Les formulations suivantes méritent une écoute native, comme le propose déjà \`Relecture-locutrice.md\` :

- \`Môžeme si potykať?\` et l'usage du toast pour proposer le tutoiement ;
- \`Tykáme si, Gab! Už roky!\` ;
- \`Už sme tam?\` dans la bouche d'enfants en voiture ;
- \`O dvesto metrov odbočte doprava\`, \`Prepočítavam trasu\`, \`Stratila som signál\`, \`Na kruhovom objazde choďte druhým výjazdom\` ;
- \`čerpacia stanica\` par rapport à \`benzínka\` ;
- \`ubytovanie v súkromí\`.

La voix du GPS est une excellente idée narrative ; elle mérite une validation spécifique, parce que ses formulations sont répétées dans plusieurs chapitres et risquent de devenir des modèles pour l'apprenant.

### 4.3. Phrases déjà signalées dans le document de relecture

Je garderais la liste existante, sans trancher à la place d'un natif :

| Fiche | Phrase | Question |
|---|---|---|
| Štiavnica 03 | \`Lola ochutná a prestane.\` | Est-ce naturel sans complément, ou faut-il préciser \`prestane jesť\` ? |
| Štiavnica 04 | \`Tak sa pozeráme zdola.\` | Le présent voulu est-il naturel dans ce contexte ? |
| Raj 06 | \`Dnes som spal výborne.\` | Faut-il préciser \`Dnes v noci\` ? |
| Spiš 03 | \`Bol som na veľa hradoch.\` | Naturel à l'oral ou préférer \`na mnohých hradoch\` ? |
| Bardejov 02 | \`Žltý, zelený, modrý, ružový!\` | L'ellipse au singulier est-elle naturelle quand Lola désigne les maisons une par une ? |
| Bardejov 03 | \`Predvčerom sme vyšli na rebríky.\` | \`Vyjsť na rebríky\` est-il idiomatique ici ? |
| Prešov 03 | \`Ďakujem babke. Ďakujem mame.\` | Est-ce naturel de remercier à la troisième personne dans cette scène ? |
| Prešov 05 | \`Chudáky kone.\` | Faut-il préférer \`Chudáci kone\` ? |
| Košice 01 | \`Cieľ je o tridsaťpäť minút.\` | Est-ce une vraie formulation de navigation ? |

## 5. Cohérence narrative et culturelle

### 5.1. Très bons éléments à préserver

- Le vouvoiement de Gab envers Andrea est un excellent fil rouge, parce qu'il sert à la fois le récit et l'apprentissage de \`ty / vy\`.
- Les enfants qui commencent à corriger Gab créent une progression amusante et visible.
- Le GPS qui parle au vouvoiement est un moyen naturel de répéter l'impératif poli.
- Les rappels entre étapes (Čumil, le tilleul, les échelles, le toboggan, le ronflement) donnent une impression de voyage vécu.
- Le choix de lieux réels et de spécialités locales distingue ce cours d'une suite de dialogues génériques.

### 5.2. Personnages à harmoniser

Le père d'Andrea, Ivan, est mentionné dans le concept et dans le format comme personnage du chapitre 11, avec un avatar et un trait de caractère lié à la pêche. Dans les fiches Prešov parcourues, Marta et babka Zuzana apparaissent, mais Ivan ne semble pas avoir de scène.

Deux solutions :
- lui donner une courte apparition, même une seule réplique sur la pêche ;
- ou le retirer des tableaux de personnages et du casting prévu si son absence est volontaire.

Cela évitera qu'un personnage annoncé dans la documentation semble avoir été oublié.

### 5.3. Simplifications culturelles à nuancer

- La distinction \`hrad\` / \`zámok\` (« château fort » / « château de résidence ») est une bonne première approximation, mais pas une règle absolue pour classer tous les châteaux slovaques.
- Les affirmations de type « le premier bâtiment Renaissance du pays », « le plus ancien skanzen » ou « l'un des plus anciens du monde » doivent être reliées à une source précise et formulées avec prudence si les classements varient selon les critères.
- Les Coins slovaques sont une vraie valeur ajoutée ; mieux vaut une formulation légèrement prudente qu'un superlatif difficile à défendre.

### 5.4. Bardejov et l'UNESCO

La formulation actuelle \`Celé námestie je v UNESCO\` est à corriger, à la fois pour la précision et pour le français. Le bien inscrit concerne le centre historique de Bardejov et le faubourg juif. Il ne s'agit pas de dire que la place elle-même est un bien autonome.

### 5.5. Le rôle de Kofola

La présence de Kofola dans le dialogue est culturellement intéressante : c'est une boisson familière en Slovaquie et dans l'ancien espace tchécoslovaque. Le seul problème est la règle éditoriale du cours qui exclut les marques des dialogues. Il faut décider si Kofola fait exception, plutôt que laisser une contradiction entre la règle et la fiche.

## 6. Progression et niveau

La progression A0 vers A2 est lisible et motivante. Les premiers chapitres restent courts ; les chapitres suivants introduisent progressivement le passé, l'aspect, le conditionnel et les subordonnées.

Deux réserves :

1. **Les chapitres 5 à 12 sont encore sous la cible de longueur**, comme le reconnaît \`docs/Histoire.md\`. Ce n'est pas gênant pour une bêta, mais il faut éviter de présenter le récit comme entièrement étoffé tant que cette seconde passe n'a pas été faite.
2. **Les Kronika sont d'un niveau sensiblement supérieur** aux dialogues du roadtrip : vocabulaire historique et politique, phrases complexes, abstractions et subordonnées. C'est très bien comme contenu bonus, mais je les présenterais explicitement comme lecture complémentaire avancée (B1 ou plus), et non comme une étape obligatoire pour atteindre A2.

La progression gagnerait aussi à préciser clairement ce qui est attendu en production et ce qui est seulement à reconnaître. Plusieurs formes sont données « en bloc » avant d'être expliquées ; c'est une méthode valide, mais les exercices ne devraient pas exiger leur production libre trop tôt.

## 7. Documentation et configuration

### 7.1. Documents à actualiser

Les documents suivants contiennent encore des étapes de travail qui ne correspondent plus à l'état actuel du dépôt :
- \`docs/Concept-adulte.md\` : la rédaction de \`Histoire.md\` et le découpage en fiches apparaissent encore comme étapes futures ;
- \`docs/Progression-roadtrip.md\` : les mêmes étapes sont encore listées ;
- \`docs/Histoire.md\` : le document indique bien que les chapitres 5 à 12 restent à allonger, ce qui semble toujours être le chantier principal ;
- \`README.md\` : il annonce encore que les chapitres 5 à 12 seront étoffés.

Je recommande une petite mise à jour commune : « Les douze étapes sont rédigées et intégrées au cours. Une seconde passe doit encore étoffer les chapitres 5 à 12 et intégrer la relecture native. »

### 7.2. Prénom de l'histoire complète

Dans \`lang.json\` :
- \`site.user_name_default\` vaut \`Gab\` ;
- \`story.user_name\` vaut encore \`Eric\`.

La documentation du format précise que le personnage du cours s'appelle Gab et que le prénom de l'apprenant est paramétrable. Il faut vérifier si \`story.user_name\` est un ancien réglage volontaire ou un oubli de la migration.

### 7.3. Séries Kronika

Les fichiers de plusieurs séries Kronika sont présents dans \`md/\`, et leurs thèmes sont présents dans \`subgroup_themes\`. En revanche, la liste \`subgroups\` de \`lang.json\` ne semble déclarer que \`kronika_vstupdoeu\`.

À vérifier avec le build et la navigation :
- toutes les séries Kronika sont-elles encore accessibles ?
- les titres de groupes affichés sont-ils corrects ?
- faut-il ajouter les libellés manquants dans \`subgroups\` ?

Je ne conclus pas à un bug sans vérifier le comportement réel du moteur ; c'est une incohérence de configuration à contrôler.

### 7.4. Exercices

Le dossier \`exercises/\` ne contient actuellement que deux fichiers JSON. Le README annonce pourtant des exercices pour chaque fiche, et le format décrit des exercices faits à la main.

Il faut préciser l'organisation réelle :
- si les exercices sont générés automatiquement à partir des fiches, le dire dans le format ;
- si les exercices doivent être faits à la main, compléter le dossier ;
- dans tous les cas, vérifier qu'une modification de traduction ou de phrase ne laisse pas un exercice obsolète.

### 7.5. Crédits des images

Le README annonce déjà que certains crédits restent à compléter. Le fichier \`img/credits.md\` confirme que plusieurs bandeaux de style n'ont pas encore leur auteur ou leur licence.

C'est un point administratif plutôt que linguistique, mais à régler avant une publication présentée comme définitive.

## 8. Ordre de correction recommandé

1. Corriger immédiatement l'explication française de \`ak bude\`.
2. Corriger la décomposition de \`Z dier vykúkajú malé zvieratká\`.
3. Reformuler l'explication du \`h\` dans la fiche de prononciation.
4. Corriger la formulation UNESCO de Bardejov.
5. Ajouter la remarque pédagogique sur le pluriel de \`plavky\`.
6. Décider du statut de Kofola dans les dialogues.
7. Faire valider les questions de \`docs/Relecture-locutrice.md\`, en commençant par le šariš et la voix du GPS.
8. Décider si Ivan apparaît dans le chapitre Prešov.
9. Harmoniser \`story.user_name\`, les sous-groupes Kronika, les exercices et les crédits.
10. Actualiser les documents de progression et de statut.
11. Faire une dernière lecture à voix haute des dialogues, puis tester les exercices après build.

## 9. Conclusion

Le roadtrip a une vraie personnalité. C'est un cours qui donne envie de continuer parce qu'on veut savoir ce qui arrive à Gab, Andrea et aux enfants, et parce que chaque journée apporte quelque chose de concret sur la Slovaquie. Le dispositif du GPS et le gag du vouvoiement sont particulièrement réussis : ils font travailler la langue sans donner l'impression d'une leçon.

Les corrections relevées ne remettent pas en cause la structure. Les plus importantes sont localisées et faciles à traiter. Le plus gros travail restant est la validation par un locuteur natif, surtout pour le šariš, les expressions de navigation et quelques tournures de dialogue déjà recensées dans \`Relecture-locutrice.md\`.

**Mon avis :** c'est une très bonne base de cours adulte, probablement la plus aboutie des trois en matière de cohérence entre histoire, lieux visités et apprentissage. Je garderais son ton et son architecture ; je concentrerais les efforts sur la validation linguistique, la mise à jour documentaire et l'étoffement prévu des derniers chapitres.
