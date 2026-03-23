"""
Projet : WORDGRID
Auteurs : Valentin BORNE, Minh Tri NGUYEN
"""

""" Fichier Dictionary_manager.py """
""" Contient la fonction choix_dico pour choisir aléatoirement le mot selon la configuration choisi par le joueur """

from random import choice

def choix_dico(configue : object) -> str:
    """
    Fonction pour choisir un mot aléatoirement d'un fichier précis
    Elle prend en paramètre un Objet et return le mot choisi en string
    """
    with open(f"dictionnaire/{configue.langue}/{configue.theme}/{configue.longueur_mot}.txt","r", encoding="utf-8") as fichier:
        mots = fichier.read().splitlines()
        return choice(mots)
