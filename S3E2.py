# Tri à bulles
# Exercice à réaliser
#  Soit un tableau de 10 entiers que vous remplissez manuellement avec les valeurs de votre
# choix en évitant que ces valeurs ne soient déjà triées
#  Ecrire l’algorithme qui permet de trier le tableau du plus petit entier au plus grand entier (sans
# utiliser la fonction sort de Python)

table=[5,3,7,1,9,2,4,8,6,0]
print(table)
for i in range(10):
    for j in range(9):
        if table[j]>table[j+1]:
            table[j],table[j+1]=table[j+1],table[j]
print(table)


