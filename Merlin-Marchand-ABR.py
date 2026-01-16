import tkinter as tk

class Noeud:
    def __init__(self, valeur, hauteur=0):
        # Initialisation d'un nœud avec une valeur, une hauteur et deux pointeurs vers les sous-arbres gauche et droit
        self.valeur = valeur
        self.sag = None  # Sous-arbre gauche
        self.sad = None  # Sous-arbre droit
        self.hauteur = hauteur  # Stockage de la hauteur du nœud

    def ajouter(self, valeur, hauteur):
        # Ajoute une valeur dans l'arbre en respectant la contrainte de hauteur maximale (4)
        if hauteur > 4:
            print(f"Impossible d'ajouter {valeur}, hauteur maximale atteinte.")
            return

        # Si la valeur est inférieure à la valeur du nœud, elle va dans le sous-arbre gauche
        if valeur < self.valeur:
            if self.sag is None:
                self.sag = Noeud(valeur, hauteur)  # Création d'un nouveau nœud à gauche
                print(f"Ajout de {valeur} à gauche de {self.valeur} (Hauteur {hauteur})")
            else:
                self.sag.ajouter(valeur, hauteur + 1)  # Appel récursif pour ajouter à gauche

        # Si la valeur est supérieure, elle va dans le sous-arbre droit
        elif valeur > self.valeur:
            if self.sad is None:
                self.sad = Noeud(valeur, hauteur)  # Création d'un nouveau nœud à droite
                print(f"Ajout de {valeur} à droite de {self.valeur} (Hauteur {hauteur})")
            else:
                self.sad.ajouter(valeur, hauteur + 1)  # Appel récursif pour ajouter à droite
        else:
            print(f"La valeur {valeur} existe déjà dans l'arbre.")  # La valeur existe déjà dans l'arbre

class ArbreBinaire:
    def __init__(self):
        # Initialisation d'un arbre binaire avec une racine vide
        self.racine = None

    def ajouter(self, valeur):
        # Ajoute une valeur à l'arbre binaire
        if self.racine is None:
            self.racine = Noeud(valeur, hauteur=0)  # Création de la racine si l'arbre est vide
            print(f"Racine ajoutée : {valeur}")
        else:
            self.racine.ajouter(valeur, 1)  # On commence à la hauteur 1 si la racine existe déjà

    def afficher(self, canvas, x, y, profondeur=0, espacement=140):
        # Affiche l'arbre sur une toile graphique
        self._afficher_noeud(canvas, self.racine, x, y, profondeur, espacement)

    def _afficher_noeud(self, canvas, noeud, x, y, profondeur, espacement):
        # Affiche récursivement un nœud et ses sous-arbres sur le canevas
        if noeud is None:
            return

        rayon = 15  # Rayon du cercle représentant un nœud
        hauteur_ecart = 70  # Écart vertical entre les nœuds

        # Si le nœud a un sous-arbre gauche, on dessine une ligne et on affiche récursivement ce sous-arbre
        if noeud.sag:
            x_sag, y_sag = x - espacement, y + hauteur_ecart
            canvas.create_line(x, y + rayon, x_sag, y_sag - rayon, arrow=tk.LAST)  # Dessiner la ligne de connexion
            self._afficher_noeud(canvas, noeud.sag, x_sag, y_sag, profondeur + 1, espacement // 2)  # Appel récursif pour le sous-arbre gauche

        # Si le nœud a un sous-arbre droit, on dessine une ligne et on affiche récursivement ce sous-arbre
        if noeud.sad:
            x_sad, y_sad = x + espacement, y + hauteur_ecart
            canvas.create_line(x, y + rayon, x_sad, y_sad - rayon, arrow=tk.LAST)  # Dessiner la ligne de connexion
            self._afficher_noeud(canvas, noeud.sad, x_sad, y_sad, profondeur + 1, espacement // 2)  # Appel récursif pour le sous-arbre droit

        # Dessiner le cercle représentant le nœud
        canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, outline="black", width=2, fill="white")
        # Afficher la valeur du nœud dans le cercle
        canvas.create_text(x, y, text=str(noeud.valeur), font=("Arial", 12, "bold"))

class Application:
    def __init__(self, root):
        self._fenetre = root
        self._fenetre.geometry("1024x600")
        self._fenetre.title("Arbre Binaire de Recherche")
        self._fenetre.config(bg="#f0f0f0")
        self._arbre = ArbreBinaire()

        # Canevas pour afficher l'arbre
        canevas = tk.Canvas(self._fenetre, width=1604, height=130, highlightthickness=5)
        canevas.pack(pady=20)
        self.create_rectangle(canevas, 40, 0, 980, 80, fill="#1F2937")

        # Titre de l'application
        titre = tk.Label(self._fenetre, text="Arbre Binaire de Recherche", bg="#1F2937", fg="#FFFFFF",font=("Arial", 15, "bold"))
        titre.place(x=400, y=45)

        # Canevas pour afficher l'arbre binaire
        self._canvas = tk.Canvas(self._fenetre, width=560, height=430, bg="#FFFFFF")
        self._canvas.place(x=70, y=130)

        # Champ de texte pour saisir les valeurs
        self._entry = tk.Entry(self._fenetre, bd=2, width=40, relief="solid")
        self._entry.place(x=690, y=300)

        # Boutons
        bouton_ajouter = tk.Button(self._fenetre, text="Dessiner", font=("Arial", 12, "bold"), width=10, height=2, command=self.ajouter_valeurs)
        bouton_ajouter.place(x=760, y=400)

        bouton_reset = tk.Button(self._fenetre, text="Réinitialiser", font=("Arial", 12, "bold"), width=10, height=2, command=self.reinitialiser)
        bouton_reset.place(x=900, y=45)

        bouton_Apropos = tk.Button(self._fenetre, text="À propos", font=("Arial", 12, "bold"), width=10, height=2, command=self.FenetreAPropos)
        bouton_Apropos.place(x=100, y=45)

        bouton_quitter = tk.Button(self._fenetre, text="Quitter", font=("Arial", 12, "bold"), width=10, height=2, fg='red', command=self._fenetre.destroy)
        bouton_quitter.place(x=840, y=530)

        canevas.create_window(900, 45, window=bouton_reset)
        canevas.create_window(120, 45, window=bouton_Apropos)

    def ajouter_valeurs(self):
        try:
            # Récupération et conversion des entrées en une liste d'entiers
            valeurs = list(map(int, self._entry.get().split()))
            # Filtrage des valeurs pour qu'elles soient comprises entre 1 et 99
            valeurs = [val for val in valeurs if 1 <= val <= 99]
            # Vérification si au moins une valeur valide a été saisie
            if not valeurs:
                print("Aucune valeur valide saisie.")
                return
            # Ajout des valeurs à l'arbre binaire
            for valeur in valeurs:
                self._arbre.ajouter(valeur)
            # Effacement du canvas avant de redessiner l'arbre
            self._canvas.delete("all")
            self._arbre.afficher(self._canvas, 280, 80)
        except ValueError:
            # Gestion des erreurs si la conversion en entier échoue
            print("Veuillez entrer des nombres valides.")


    def reinitialiser(self):
        # Réinitialise l'arbre et efface le canevas et le champ de texte
        self._arbre = ArbreBinaire()
        self._canvas.delete("all")
        self._entry.delete(0, tk.END)

    def create_rectangle(self, canvas, x1, y1, x2, y2, **kwargs):
        # Crée un rectangle sur le canevas avec les coordonnées et options spécifiées
        return canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

    def FenetreAPropos(self):
        # Crée une fenêtre "À propos" avec des informations sur l'application
        fenetreAP = tk.Toplevel(self._fenetre)
        fenetreAP.geometry("800x480")
        fenetreAP.title("À propos")
        fenetreAP.configure(bg="#f0f0f0")

        canevas = tk.Canvas(fenetreAP, width=800, height=50, highlightthickness=5)
        canevas.pack(pady=20)
        self.create_rectangle(canevas, 45, 0, 800, 50, fill="#1F2937")

        titre = tk.Label(fenetreAP, text="À propos", bg="#1F2937", fg="#FFFFFF",font=("Arial", 15, "bold"))
        titre.place(x=400, y=35)

        textes = [
            "Comment utiliser notre application ?",
            "- Saisissez des nombres entre 1 et 99.",
            "- Cliquez sur 'Dessiner' pour afficher l'arbre.",
            "- L'arbre est limité à une hauteur de 4.",
            "- Utilisez 'Réinitialiser' pour recommencer.",
            "- Cliquez sur 'Quitter' pour fermer l'application."
        ]

        y_position = 120
        for texte in textes:
            tk.Label(fenetreAP, text=texte, font=("Arial", 12, "bold")).place(x=100, y=y_position)
            y_position += 40

        createur = tk.Label(fenetreAP, text="Merlin Kylian | Marchand Baptiste", font=("Arial", 10))
        createur.place(x=100, y=420)

        boutonQ = tk.Button(fenetreAP, text="Quitter", font=("Arial", 12, "bold"), width=10, height=2, fg='red', command=fenetreAP.destroy)
        boutonQ.place(x=600, y=400)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
