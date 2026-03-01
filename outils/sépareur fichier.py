def séparer(fichier, taille):
    with open(f"c:/Users/ELEVE/Sac à dos 5eme1/3°/OneDrive/Sac à dos/Term/trophé/data/{fichier}.txt", "r") as fichier, \
         open(f"c:/Users/ELEVE/Sac à dos 5eme1/3°/OneDrive/Sac à dos/Term/trophé/data/all/{taille}.txt", "w") as sortie:
        
        for ligne in fichier:
            mot = ligne.strip()
            if len(mot) == taille:
                sortie.write(mot + "\n")
   
for i in range(4, 31):   
    séparer("en_all", i)