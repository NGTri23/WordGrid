from flask import Flask, render_template, request, session, redirect
from config import GameConfig, liste_langue, liste_theme, liste_difficulte, liste_modeJeu
from Dictionary_manager import choix_dico
from TRIE import utiliser_trie
from Chronometre import Chronometre
from random import randint
import time #à sup
import os
import datetime
LEADERBOARD_FILE = "leaderboard.txt"
DIFFICULTES_LABEL = {
    0: "Chill",
    1: "Très facile",
    2: "Facile",
    3: "Normal",
    4: "Moyen",
    5: "Difficile",
    6: "Très difficile"
}

def save_best_score_txt(mot: str, difficulte: int, tentatives_utilisees: int, temps_sec: float):

    mot = (mot or "").strip().lower().replace(";", " ")

    try:
        new_time = float(temps_sec)
    except:
        new_time = float("inf")

    date_iso = datetime.datetime.utcnow().isoformat()
    new_line = f"{mot};{int(difficulte)};{int(tentatives_utilisees)};{new_time};{date_iso}\n"

    # Si le fichier n'existe pas : on crée
    if not os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
            f.write(new_line)
        return

    out_lines = []
    found = False

    with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) != 5:
                out_lines.append(line)
                continue

            w, d, old_attempts, old_time, old_date = parts

            # Même mot + difficulté => comparer temps
            if w == mot and int(d) == int(difficulte):
                found = True
                try:
                    old_time_val = float(old_time)
                except:
                    old_time_val = float("inf")

                # Remplace seulement si meilleur temps
                if new_time < old_time_val:
                    out_lines.append(new_line)
                else:
                    out_lines.append(line)
                continue

            out_lines.append(line)

    # Si pas trouvé : on ajoute
    if not found:
        out_lines.append(new_line)

    with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
        f.writelines(out_lines)

def load_scores_txt(limit: int = 20):
    if not os.path.exists(LEADERBOARD_FILE):
        return []

    scores = []

    with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            if len(parts) != 5:
                continue

            mot, difficulte, tentatives, temps_sec, date_iso = parts

            try:
                temps_val = float(temps_sec)
            except:
                temps_val = float("inf")

            c = Chronometre()
            c.duree = temps_val
            h, m, s = c.convertisseur()
            temps_affiche = f"{h:02d}:{m:02d}:{s:05.2f}"

            scores.append({
                "mot": mot,
                "difficulte": DIFFICULTES_LABEL.get(int(difficulte), "Inconnue"),
                "tentatives": int(tentatives),
                "temps_sec": temps_val,
                "temps_affiche": temps_affiche,
                "date": date_iso
            })

    scores.sort(key=lambda s: (s["temps_sec"], s["tentatives"], s["date"]))
    return scores[:limit]

#il faudra peut-etre plus tard à mettre les fct dans le meme fichier
def img_background() -> str:
    """Fonction pour retourner un path (en str) de l'image du background
    Cette image est tirée aléatoirement"""

    return f"images/{randint(1,20)}.jpg"

def comparer_mots(mot_secret : str, mot_proposé : str) -> str:
    """Fonction pour comparer le mot_secret à deviner et le mot_proposé par le joueur
    Elle retourne un str qui contient les couleurs (V, J, G) correspondant à chaque lettre du mot_proposé
    """
    assert len(mot_proposé) == len(mot_secret), "la longueur de 'mot_proposé' et 'mot_secret' ne sont pas pareil"

    resultat = []
    mot2_utilise = list(mot_secret)  # Pour éviter de compter une lettre deux fois

    # Première passage : vérifier les lettres bien placées (V)
    for i in range(len(mot_secret)):
        if mot_secret[i] == mot_proposé[i]:
            resultat.append("V")
            mot2_utilise[i] = None
        else:
            resultat.append(None)

    # Deuxième passage : vérifier lettres présentes mais mal placées (J) ou absentes (G)
    for i in range(len(mot_secret)):
        if resultat[i] is None:
            if mot_proposé[i] in mot2_utilise:
                resultat[i] = "J"
                mot2_utilise[mot2_utilise.index(mot_proposé[i])] = None 
            else:
                resultat[i] = "G"

    return "".join(resultat)

app = Flask(__name__)
app.secret_key = "dev-key" # je sais pas à quoi ça sert mais c'est obligatoire

configuration = GameConfig() # INSTANCIATION pour régler par défaut la config
chrono = Chronometre() # INSTANCIATION un chronomètre pour mesurer le temps d'une partie


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html",
                           image_fond=img_background())

@app.route("/configuration", methods=["POST", "GET"])
def menu_config():
    donnee_config = dict(request.form)
    print(donnee_config) # à sup

    session.clear() # supprimer tout le cache et session
    
    if "random" in request.form: #le bouton random est cliqué
        configuration.random_config()

    return render_template("configuration.html",
                           liste_langue=liste_langue,
                           liste_theme=liste_theme,
                           liste_difficulte=liste_difficulte,
                           liste_modeJeu=liste_modeJeu,
                           configuration=configuration,
                           image_fond=img_background())

@app.route("/play", methods=["POST", "GET"])
def game():
    fin_partie = False
    session["score_saved"] = False

    donnee_config = dict(request.form)
    print(donnee_config) # à sup
    bool_mot_présent = True
    
    trie = utiliser_trie(configuration) #faire entrer tous les mots dans l'arbre Trie
    for cle, valeur in donnee_config.items():
        if cle == "mot_tentative" :
            bool_mot_présent = trie.mot_present(valeur)
        if cle in ["langue", "theme", "longueur_mot", "difficulte", "modeJeu"] :
            setattr(configuration, cle, valeur)

        elif cle == "mot_tentative" and  trie.mot_present(valeur):
            resultat_VJG = comparer_mots(session["mot_secret"], valeur.lower())
            session["liste_mot_proposé"] += [(valeur, resultat_VJG)] #privilégier l'utilisation de la concaténation que 'append'

            if resultat_VJG.count("V") == configuration.longueur_mot:
                session["victoire"] = True # le joueur a trouvé le mot

            session["essais_restant"] -= 1 # décomptes à -1 aux essais

        elif cle == "abandonne_partie" :
            fin_partie = True
            session["victoire"] = False  # abandon = défaite

        elif cle == "btn_revenir" :
            return redirect("/configuration")


        if cle == "modeJeu" and valeur == "duo" :
            return redirect("/play_duo")


    if "mot_secret" not in session : # session : c'est presque comme des Cookies
        session["mot_secret"] = choix_dico(configuration) # choisir le mot au hasard et le stocker jusqu'à la fin de la partie
    print(session["mot_secret"]) # à sup

    if "liste_mot_proposé" not in session:
        session["liste_mot_proposé"] = []
    print("liste_mot :", session["liste_mot_proposé"]) # à sup

    if "victoire" not in session :
        session["victoire"] = False
    elif "victoire" in session and session["victoire"]:
        session["temps_chrono"] = chrono.stop()
        session["temps_sec"] = chrono.duree
        print(session["temps_chrono"]) # à sup
        fin_partie = True

    if "essais_restant" not in session : # création session "essais_restant"
        session["essais_restant"] = 10 - configuration.difficulte
    elif session["essais_restant"] < 1: # vérification fin décompte essais
        session["temps_chrono"] = chrono.stop()
        session["temps_sec"] = chrono.duree
        print(session["temps_chrono"]) # à sup
        fin_partie = True

    if "temps_chrono" not in session :
        session["temps_chrono"] = 0
        chrono.start()
        print(time.time()) # à sup
    if fin_partie and not session.get("score_saved", False):

        tentatives_max = 10 - int(configuration.difficulte)
        tentatives_utilisees = tentatives_max - int(session.get("essais_restant", 0))

        if session.get("victoire", False) and configuration.modeJeu == "chrono":
            save_best_score_txt(
                mot=session.get("mot_secret", ""),
                difficulte=int(configuration.difficulte),
                tentatives_utilisees=tentatives_utilisees,
                temps_sec=float(session.get("temps_sec", 0))
            )

    session["score_saved"] = True
    return render_template("play.html", mot=session["mot_secret"],
                                       liste_langue=liste_langue,
                                       liste_theme=liste_theme,
                                       configuration=configuration,
                                       essais_restant=session["essais_restant"],
                                       liste_mot=session["liste_mot_proposé"],
                                       image_fond=img_background(),
                                       start_time=chrono.debut,
                                       temps=chrono.convertisseur(),
                                       bool_mot_présent=bool_mot_présent,
                                       fin_partie=fin_partie,
                                       victoire=session["victoire"])

@app.route("/play_duo", methods=["POST", "GET"])
def play_duo():

    donnee_config = dict(request.form)
    print(donnee_config) # à sup
    
    fin_partie = False
    trie = utiliser_trie(configuration)

    bool_mot_présent = True
    for cle, valeur in donnee_config.items():
        if cle == "mot_tentative" :
            bool_mot_présent = trie.mot_present(valeur)
        if cle in ["langue", "theme", "longueur_mot", "difficulte", "modeJeu"] :
            setattr(configuration, cle, valeur)

    # Initialisation tous les sessions
    if "joueur_actif" not in session:
        session["joueur_actif"] = 1

    if "mot_secret_j1" not in session:
        session["mot_secret_j1"] = choix_dico(configuration)
        print(session["mot_secret_j1"]) # à sup

    if "mot_secret_j2" not in session:
        session["mot_secret_j2"] = choix_dico(configuration)
        print(session["mot_secret_j2"]) # à sup

    if "liste_mot_j1" not in session:
        session["liste_mot_j1"] = []

    if "liste_mot_j2" not in session:
        session["liste_mot_j2"] = []

    if "essais_j1" not in session:
        session["essais_j1"] = 10 - int(configuration.difficulte)

    if "essais_j2" not in session:
        session["essais_j2"] = 10 - int(configuration.difficulte)

    if "tour_transition" not in session:
        session["tour_transition"] = False
    
    if "transition_valide" not in session:
        session["transition_valide"] = True

    if "victoire_j1" not in session:
        session["victoire_j1"] = False

    if "victoire_j2" not in session:
        session["victoire_j2"] = False

    if request.method == "POST":
        if "btn_revenir" in request.form:
            return redirect("/configuration")

        if "continuer_duo" in request.form:
            session["tour_transition"] = False

        elif "abandonne_partie" in request.form:
            fin_partie = True

        elif "mot_tentative" in request.form:
            valeur = request.form["mot_tentative"].lower()

            if trie.mot_present(valeur):
                session["transition_valide"] = True
                if session["joueur_actif"] == 1:
                    resultat = comparer_mots(session["mot_secret_j1"], valeur)
                    session["liste_mot_j1"] += [(valeur, resultat)]
                    print(1, session["liste_mot_j1"]) # à sup
                    session["essais_j1"] -= 1

                    if resultat.count("V") == configuration.longueur_mot:
                        session["victoire_j1"] = True
                        fin_partie = True
                        session["tour_transition"] = False
                    elif session["essais_j1"] <= 0:
                        fin_partie = True
                    else:
                        session["joueur_actif"] = 2
                        session["tour_transition"] = True

                else:
                    resultat = comparer_mots(session["mot_secret_j2"], valeur)
                    session["liste_mot_j2"] += [(valeur, resultat)]
                    print(2, session["liste_mot_j2"]) # à sup
                    session["essais_j2"] -= 1

                    if resultat.count("V") == configuration.longueur_mot:
                        session["victoire_j2"] = True
                        fin_partie = True
                        session["tour_transition"] = False
                    elif session["essais_j2"] <= 0:
                        fin_partie = True
                    else:
                        session["joueur_actif"] = 1
                        session["tour_transition"] = True
            else :
                session["transition_valide"] = False

    return render_template(
        "play_duo.html",
        configuration=configuration,
        joueur_actif=session["joueur_actif"],
        mot_j1=session["mot_secret_j1"],
        mot_j2=session["mot_secret_j2"],
        liste_mot_j1=session["liste_mot_j1"],
        liste_mot_j2=session["liste_mot_j2"],
        essais_j1=session["essais_j1"],
        essais_j2=session["essais_j2"],
        tour_transition=session["tour_transition"],
        transition_valide=session["transition_valide"],
        image_fond=img_background(),
        fin_partie=fin_partie,
        victoire_j1=session["victoire_j1"],
        victoire_j2=session["victoire_j2"],
        bool_mot_présent=bool_mot_présent
    )

@app.route("/leaderboard")
def leaderboard():
    scores = load_scores_txt(limit=20)
    return render_template("leaderboard.html",
                           scores=scores,
                           image_fond=img_background())

@app.route("/aide")
def need_help():
    return render_template("aide.html",
                           image_fond=img_background())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

