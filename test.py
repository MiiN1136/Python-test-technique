def somme_liste_pair(liste):
    somme = 0
    for nombre in liste:
        if nombre % 2 == 0:
            somme += nombre
    return somme


liste = [5,7,10,99,75,32]
resultat = somme_liste_pair(liste)
print(f"La somme des nombres pairs dans la liste {liste} est : {resultat}")
