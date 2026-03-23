# WORDGRID

## 1. Présentation du projet

### Présentation du projet
L’idée du projet est née de l’envie de proposer un jeu simple permettant d’améliorer son vocabulaire, y compris dans différentes langues. Nous avons voulu répondre à la problématique suivante : comment apprendre et enrichir son vocabulaire de manière accessible et non scolaire.
L’objectif est donc de créer un jeu de devinette de mots, facile à prendre en main, qui permet d’apprendre en jouant, seul ou avec des amis, tout en développant la réflexion et les connaissances linguistiques.

---

## 2. Organisation du travail

### Équipe et Rôles
- Valentiv BORNE : s'occupe principalement la partie logique et interne du programme.
- Minh Tri NGUYEN : s'occupe principalement la partie interface du projet.

### Temps passé
Nous avons consacré au moins  40 heures à ce projet.

---

## 3. Étapes du projet

Nous avons d’abord commencé par développer la version console du jeu, en mettant en place toute la logique : gestion des dictionnaires, sélection aléatoire du mot, vérification des propositions du joueur et mise en place du système de couleurs.

Ensuite, nous avons conçu l’interface afin de rendre le jeu plus interactif et accessible.

Puis, nous avons relié la logique du jeu avec l’interface pour obtenir une application fonctionnelle.

Enfin, nous avons ajouté des fonctionnalités supplémentaires, comme le mode duo et le mode chronométré.

---

## 4. Validation et fonctionnement

### Difficultés rencontrées et solutions
- Gestion des lettres doublées : au début, le programme marquait parfois une lettre comme "J" plusieurs fois alors qu’elle n’apparaissait qu’une seule fois dans le mot secret.  
  **Solution** : nous avons créé une copie du mot secret (`mot2_utilise`) et chaque fois qu’une lettre était utilisée pour un "V" ou un "J", elle était remplacée par `None`. Cela permet d’éviter de compter deux fois la même lettre et de gérer correctement les doublons.
- Vérification des mots proposés : au début, la vérification de la validité d’un mot se faisait en parcourant toute la liste des mots, ce qui était lent et peu efficace, surtout avec des dictionnaires volumineux.  
  **Solution** : nous avons utilisé un arbre **TRIE** pour stocker tous les mots de la longueur choisie dans la configuration. Ainsi, la vérification d’un mot proposé par le joueur se fait très rapidement en cherchant simplement dans l’arbre.
- Choix de l’interface : au départ, nous hésitions entre Pygame et une interface web (HTML/CSS).  
  **Solution** : nous avons choisi HTML/CSS pour bénéficier d’une plus grande liberté graphique, notamment pour créer un fond attrayant et une interface plus esthétique, tout en facilitant l’adaptation aux différentes tailles d’écran et aux animations.

---

## 5. Ouverture

### Idées d'amélioration
- Ajouter davantage de thèmes et de langues pour diversifier le jeu.
- Développer un mode multijoueur en ligne pour jouer avec des amis à distance.  

### Compétences développées
Nous avons renforcé nos compétences en programmation Python, en structuration de projet, en gestion de fichiers et en logique de jeu. Nous avons aussi appris à travailler en équipe et à résoudre des problèmes techniques de manière collaborative.  

### Démarche d'inclusion
Le jeu a été conçu pour être accessible à tous : interface simple, choix de langue, et règles claires. L’idée est de permettre à tous les joueurs, quel que soit leur âge ou leur niveau, de profiter de l’apprentissage du vocabulaire.