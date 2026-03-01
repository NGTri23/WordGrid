class TrieNoeud:
    """Class pour instancier un Noeud d'un arbre
    qui a pour attributs :
        - fils
        - fin_mot"""
    
    def __init__(self):
        """Constructeur"""
        self.fils = {}
        self.fin_mot = False

class Trie:
    """Class pour faire un arbre Trie"""

    def __init__(self):
        """Constructeur"""
        self.racine = TrieNoeud()
    
    def inserer(self, mot):
        """Méthode pour insérer les nouveaux mots à l'arbre"""
        noeud = self.racine
        for charactere in mot:
            if charactere not in noeud.fils:
                noeud.fils[charactere] = TrieNoeud()
            noeud = noeud.fils[charactere]
        noeud.fin_mot = True
    
    def mot_present(self, mot):
        """Méthode pour vérifier si le mot est présent dans l'arbre"""
        noeud = self.racine
        for charactere in mot.lower():
            if charactere not in noeud.fils:
                return False
            noeud = noeud.fils[charactere]
        return noeud.fin_mot
  

def utiliser_trie(configue : object) -> Trie:
    """
    Fonction pour insérer tous les mots du fichier des mots dans l'arbre TRIE
    Elle prend en paramètre un Object et retourne l'arbre
    """
    trie = Trie()
    with open(f"dictionnaire/{configue.langue}/{configue.theme}/{configue.longueur_mot}.txt","r", encoding="utf-8") as fichier:
        for mot in fichier :
            trie.inserer(mot[:-1])
    return trie