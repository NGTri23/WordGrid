"""
Projet : WORDGRID
Auteurs : Valentin BORNE, Minh Tri NGUYEN
"""

""" Fichier Chronometre.py """
""" Contient la Class Chronometre pour la gestion du chronomètre du mode Chrono"""

import time

class Chronometre:
    """ Class pour chronométrer les parties """
    
    def __init__(self):
        """ Constructeur """
        self.debut = None
        self.fin = None
        self.duree = 0 # en secondes (et non formalisé)

    def start(self):
        """ Méthode pour débuter le chrono """
        self.debut = time.time()
        self.fin = None
        self.duree = 0

    def stop(self) -> float:
        """ Méthode pour arrêter le chrono, et elle retourne le temps """
        if self.debut is None:
            return None
        self.fin = time.time()
        
        self.duree = self.fin - self.debut
        return self.duree

    def get_time(self) -> float:
        """ Méthode qui retourne la durée du chrono """
        if self.debut is None:
            return 0
        if self.fin is None:
            self.duree = time.time() - self.debut
            return self.duree
        
        self.duree = self.fin - self.debut
        return self.duree

    def convertisseur(self) -> tuple:
        """ Méthode pour convertir le format de base (en seconde) en un tuple (heures, minutes, secondes, 100e de sec) """
        duree = self.duree
        
        heures = int(duree // 3600)
        minutes = int((duree % 3600) // 60)
        secondes = round(duree % 60, 2)
        
        return heures, minutes, secondes