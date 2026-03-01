#Dictionary manager
from random import choice
def choix_dico(configue  : object) -> str:
    """
    Fonction pour choisir un mot aléatoirement d'un fichier précis
    Elle prend en paramètre un Objet et return le mot choisi en string
    """
    with open(f"dictionnaire/{configue.langue}/{configue.theme}/{configue.longueur_mot}.txt","r", encoding="utf-8") as fichier:
        mots = fichier.read().splitlines()
        return choice(mots)
