# Test de dates
# Faîtes saisir deux dates.
# Chaque date doit être saisie en remplissant d’abord le jour, puis le mois et enfin l’année.
# A l’aide d’un algorithme, déterminez quelle est la date la plus récente des deux.

print("Entrez la première date :")
jour1 = int(input('saissisez le jour : '))
mois1 = int(input('saissisez le mois : '))
annee1 = int(input('saissisez l\'année : '))
print("La première date est : ", jour1, "/", mois1, "/", annee1)
print("Entrez la deuxième date :")
jour2 = int(input('saissisez le jour : '))
mois2 = int(input('saissisez le mois : '))
annee2 = int(input('saissisez l\'année : '))
print("La deuxième date est : ", jour2, "/", mois2, "/", annee2)
if annee1 < annee2:
    print("La date la plus récente est : ", jour2, "/", mois2, "/", annee2)
elif annee1 > annee2:
    print("La date la plus récente est : ", jour1, "/", mois1, "/", annee1)
else:
    if mois1 < mois2:
        print("La date la plus récente est : ", jour2, "/", mois2, "/", annee2)
    elif mois1 > mois2:
        print("La date la plus récente est : ", jour1, "/", mois1, "/", annee1)
    else:
        if jour1 < jour2:
            print("La date la plus récente est : ", jour2, "/", mois2, "/", annee2)
        elif jour1 > jour2:
            print("La date la plus récente est : ", jour1, "/", mois1, "/", annee1)
        else:
            print("Les deux dates sont identiques.")
# Fin