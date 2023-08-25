# Créer un Pierre, feuille, ciseaux entre le jeu et le joueur
import random

choixOrdi = (
    "pierre",
    "feuille",
    "ciseaux",
)
user_win = 0
ordi_win = 0

rejouer = ""

while True:
    #Relance le jeu ou non
    if rejouer == "n":
        break

    # Tour de l'ordinateur
    print("*" * 50)
    print("La partie va commencer!")
    valeur_ordi = choixOrdi[random.randint(0, 2)]

    # Tour du joueur
    user_choice = ""
    while user_choice not in ["pierre", "feuille", "ciseaux"]:
        user_choice = input("Choisissez entre pierre, feuille ou ciseaux. Respectez bien l'orthographe")
        user_choice.lower()

    # Résultats
    if valeur_ordi == user_choice:
        print("Egalité! Recommencez la partie...")
        continue

    if valeur_ordi == "pierre":
        if user_choice == "feuille":
            print("Vous avez gagné! La feuille enveloppe la pierre...")
            user_win += 1

        else:
            print("Vous avez perdu... La pierre casse les ciseaux")
            ordi_win += 1


    if valeur_ordi == "feuille":
        if user_choice == "ciseaux":
            print("Vous avez gagné! Les ciseaux coupent la feuille...")
            user_win += 1

        else:
            print("Vous avez perdu... La feuille enveloppe la pierre...")
            ordi_win += 1

    if valeur_ordi == "ciseaux":
        if user_choice == "pierre":
            print("Vous avez gagné! La pierre casse les ciseaux...")
            user_win += 1

        else:
            print("Vous avez perdu... Les ciseaux coupent la feuille")
            ordi_win += 1

    #Indicateur de victoire
    print(f"L'ordianteur à gagné {ordi_win}X...")
    print(f"Vous avez gagné {user_win}X...")

    #Demande si le joueur veut rejouer
    while rejouer not in ["y", "n",]:
        rejouer = input("Voulez-vous rejouez? (y/n)").lower()
        print(rejouer)
        if rejouer == "y":
            continue