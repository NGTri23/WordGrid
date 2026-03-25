<div align="center">

<img src="static/images/logo_vert.png" alt="logo" width="500"/>

### Jeu de devinette de mots — enrichissez votre vocabulaire en jouant, en français, anglais ou espagnol.

</div>

---

## À propos

**WordGrid** est un projet développé dans le cadre des **Trophées NSI 2026** par deux élèves de Terminale NSI du **Lycée Polyvalent Clos Maire**, sous la direction des professeurs **Chaddai FOUCHÉ** & **Christophe GUENEAU**.

L'idée est née de l'envie de proposer un jeu simple permettant d'améliorer son vocabulaire, y compris dans différentes langues.

---

## Problématique

> **Comment apprendre et enrichir son vocabulaire de manière accessible et non scolaire ?**

---

## Objectif

Créer un jeu de devinette de mots, facile à prendre en main, qui permet d'apprendre en jouant — seul ou avec des amis — tout en développant la réflexion et les connaissances linguistiques.

---

## Fonctionnalités

### Gameplay
- WordGrid est un jeu de devinette de mots en un nombre limité d'essais
- Affichage coloré des lettres du mot après chaque tentative : lettre bien placée, mal placée ou absente
- **3 langues disponibles** : Français, Anglais, Espagnol
- **Thèmes** : Tous les thèmes, Nature

### Configuration de la partie
Avant chaque partie, le joueur peut personnaliser entièrement sa partie :
- **Taille du mot** : de 4 à 8 lettres
- **Nombre de tentatives** : de 4 à 10 essais
- **Langue** et **thème** au choix

### Modes de jeu
- **Mode Normal** : jeu classique
- **Mode Chrono** : course contre la montre, le temps de résolution est enregistré comme score
- **Mode Duo (1v1)** : affrontez un ami sur le même écran


---

## Comment jouer

### Prérequis

- Python 3.8 ou supérieur
- Flask

### Installation

**1. Cloner le projet**
```bash
git clone https://github.com/NGTri23/WordGrid.git
cd WordGrid
```

**2. Installer les dépendances**
```bash
pip install -r requirements.txt
```

**3. Lancer le serveur**
```bash
python main.py
```

**4. Ouvrir le jeu**

Une fois le serveur lancé, un lien apparaît dans la console (ex : `http://127.0.0.1:5000`). Ouvrez-le dans votre navigateur.

### Règles

- Devinez le mot secret dans le nombre de tentatives configuré
- Après chaque essai, les cases changent de couleur :
  - **Vert** : lettre bien placée
  - **Jaune** : lettre présente mais mal placée
  - **Gris** : lettre absente du mot

---

## Structure du projet

```
WordGrid/
│
├── dictionnaire/            # Fichiers contenant tous les dictionnaires de mots (par langue/thème)
│
├── templates/               # Fichiers HTML (interface web)
│   ├── base.html
│   ├── configuration.html
│   ├── index.html
│   ├── leaderboard.html
│   ├── play.html
│   └── play_duo.html
│
├── static/                  # Ressources liées à l'interface
│   ├── images/              # Images de fond du site et logo
│   └── style.css            # Feuille de style CSS
│
├── TRIE.py                  # Système d'arbre Trie pour la vérification des mots
├── Dictionary_manager.py    # Gestion des dictionnaires et sélection des mots
├── Chronometre.py           # Gestion du chronomètre (mode chrono)
├── config.py                # Paramètres de configuration du jeu
└── main.py                  # Point d'entrée — serveur Flask (Python ↔ HTML)
```

---

## Technologies utilisées

| Technologie | Usage |
|---|---|
| **Python 3.8+** | Langage principal, logique du jeu |
| **Flask** | Serveur web local, liaison Python ↔ HTML |
| **HTML / CSS** | Interface utilisateur |
| **Arbre TRIE** | Vérification rapide des mots proposés |
| **POO** | Architecture modulaire du projet |

---

## Équipe

| Membre | Rôle |
|---|---|
| **Valentin BORNE** | Logique interne — gestion des dictionnaires, algorithmes, structure du jeu |
| **Minh Tri NGUYEN** | Interface utilisateur — HTML/CSS, liaison Flask/Python, intégration visuelle |
