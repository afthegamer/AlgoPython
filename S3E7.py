# 7 Recherche dichotomique
# La recherche dichotomique, ou recherche par dichotomie (en anglais : binary search), est un
# algorithme de recherche pour trouver la position d'un élément dans un tableau trié.
#
# Page 4 sur 4
# Le principe est le suivant : comparer l'élément recherché avec la valeur de la case au milieu du
# tableau. Si les valeurs sont égales, la tâche est accomplie.
# Sinon on recommence dans la moitié du tableau pertinente jusqu’à trouver la valeur recherchée
# (ou constater qu’elle n’est pas dans le tableau). Source Wikipédia.
# Exercice à réaliser
#  Soit le tableau suivant : [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  Faites saisir un entier et dites s’il est présent dans le tableau ci-dessus, et si oui à quelle
# position, en utilisant la méthode de la recherche dichotomique.

tableau = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(tableau)
n = int(input("Entrez un entier : "))
debut = 0
fin = len(tableau) - 1
trouve = False
while debut <= fin and not trouve:
    milieu = (debut + fin) // 2
    if tableau[milieu] == n:
        trouve = True
    elif tableau[milieu] < n:
        debut = milieu + 1
    else:
        fin = milieu - 1
if trouve:
    print("L'entier est présent à la position", milieu)
else:

    print("L'entier n'est pas présent dans le tableau")
