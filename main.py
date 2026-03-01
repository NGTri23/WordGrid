""" Main"""
""" POUR LANCER LE JEU, TAPER : "play()" dans la console"""
from TRIE import*
from config import GameConfig
from Dictionary_manager import*
from Chronometre import*
def play():
  """démarrer le jeu"""

  while True:
    print("""
  --- Vous êtes sur le jeu, que voulez-vous faire ? ---
    Taper :
    - 'exit' : pour quitter le jeu
    - 'config' : pour effectuer des configurations avant jouer
    """)

    rép = input("Votre choix --> ")
    assert rép in ["exit", "config"], "la rép est mauvaise"

    if rép == "exit" : return
    elif rép == "config":
      menu()
    
configue = GameConfig() #instantiation
def menu():
  """définir la configuration"""

  rép = ""
  while rép != "exit":
    print("""
  --- Vous êtes sur le menu de la configuration de la partie ---
    Taper :
    - 'random' : pour paramétrer aléatoirement les config
    - 'choisir' : pour choisir personellement chaque config
    - 'voir' : pour voir les choix de config que vous avez faites
    - 'jouer' : pour lancer le jeu
    - 'exit' : pour quitter le menu config
    """)
    rép = input("Votre choix --> ")

    if rép == "random" :
      configue.random_config()
      a = configue
      print(configue)
    elif rép == "choisir" :
      configue.choix_longueur_mot()
      configue.choix_difficulte()
      configue.choix_langue()
      configue.choix_theme()
    elif rép == 'voir' :
      print(configue)
    elif rép == 'jouer':
        jouer()
        exit()

def comparer_mots(mot1, mot2):
    if len(mot1) != len(mot2):
        return "Les mots doivent avoir la même taille."

    resultat = []
    mot2_utilise = list(mot2)  # Pour éviter de compter une lettre deux fois

    # Première passe : vérifier les lettres bien placées (V)
    for i in range(len(mot1)):
        if mot1[i] == mot2[i]:
            resultat.append("V")
            mot2_utilise[i] = None  # Marquer comme utilisée
        else:
            resultat.append(None)

    # Deuxième passe : vérifier lettres présentes mais mal placées (J) ou absentes (G)
    for i in range(len(mot1)):
        if resultat[i] is None:
            if mot1[i] in mot2_utilise:
                resultat[i] = "J"
                mot2_utilise[mot2_utilise.index(mot1[i])] = None
            else:
                resultat[i] = "G"

    return "".join(resultat)


def jouer():
    mot = choix_dico(configue)
    trie = utiliser_trie(configue)
    configue.difficulte = 4
    print(mot)
    print(f"Vous avez {configue._difficulte} essais :")
    essais = 0
    dico_couleur = {}
    chrono = Chronometre()
    chrono.start()
    while essais+1 <= configue._difficulte:
        tentative = ''
        while len(tentative) != configue._longueur_mot or trie.mot_present(mot) == False:
            tentative = input()
        print(tentative)
        print(comparer_mots(tentative, mot))
        if comparer_mots(tentative, mot).count("V") == len(mot):
            temps = chrono.stop()
            return True, temps
            break
        essais +=1
        print(essais)
    temps = chrono.stop()
    return False, temps
a = jouer()        
print(a)