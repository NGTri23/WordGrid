""" Fichier config.py """
""" Contient la Class GameConfig :
Demander : difficulté, longueur mot, lang, theme, random?
"""
from random import choice, randint

liste_langue = {"fr" : "Français", "en" : "Anglais"}
liste_theme = {"all" : "Tous", "natural" : "Nature"}
liste_difficulte = {10: "Chill", 9: "Très facile", 8: "Facile", 7: "Normal", 6: "Moyen", 5: "Difficile", 4: "Très difficile"}
liste_modeJeu = {"Normal" : "None", "Chronomètre" : "chrono", "Duo (1v1)" : "duo"}

class GameConfig():
    """ Class pour configurer les choix du joueur """

    def __init__(self, lenght = 4, difficulty = 3, lang = "fr", themeJeu = "all", mode = "None"):
        self._longueur_mot = lenght
        self._difficulte = difficulty
        self._langue = lang
        self._theme = themeJeu
        self._modeJeu = mode # 'chrono'
        self._random = False

    def __str__(self):
        """ Méthode str """
        s = f"""
        Votre configuration de la partie est la suivante :
        La longueur du mot est : {self._longueur_mot}
        La difficultée est : {self._difficulte}
        La langue est : {self._langue}
        Le thème est : {self._theme}
        """
        return s

    # Les ACCESSEURS pour longueur_mot ; difficulte ; langue ; theme
    def _choix_longueur_mot(self, num):
        valeur = int(num)
        assert 4 <= valeur <= 8, "La longueur du mot est trop grand ou trop petit"
        self._longueur_mot  = valeur
    def _choix_difficulte(self, num):
        valeur = int(num)
        assert 0 <= valeur <= 6, "La difficulté doit se situer entre 0 et 6, car 10 - 6 = 4"
        self._difficulte = valeur
    def _choix_langue(self, valeur):
        assert valeur in ['fr', 'en'], "La langue choisie n'est pas valide"
        self._langue = valeur
    def _choix_theme(self, valeur):
        assert valeur in ['all', 'natural'], "Le thème choisie n'exite pas"
        self._theme = valeur
    def _choix_modeJeu(self, valeur):
        assert valeur in ["None", "chrono", "duo"], "Le mode de jeu n'existe pas"
        self._modeJeu = valeur

    # Les MUTATEURS pour longueur_mot ; difficulte ; langue ; theme
    def _get_longueur_mot(self):
        return self._longueur_mot
    def _get_difficulte(self):
        return self._difficulte
    def _get_langue(self):
        return self._langue
    def _get_theme(self):
        return self._theme
    def _get_modeJeu(self):
        return self._modeJeu

    #Les property
    longueur_mot = property(_get_longueur_mot, _choix_longueur_mot)
    difficulte = property(_get_difficulte, _choix_difficulte)
    langue = property(_get_langue, _choix_langue)
    theme = property(_get_theme, _choix_theme)
    modeJeu = property(_get_modeJeu, _choix_modeJeu)


    def random_config(self):
        """ Méthode pour définir aléatoirement la configuration """

        self.longueur_mot = randint(4, 8)
        self.difficulte = randint(0, 6)
        self.langue = choice(["fr", "en"])
        self.theme = choice(["all", "natural"])
