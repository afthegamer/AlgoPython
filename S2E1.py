# Algo – Exercices Séquence 2
#
# 1 Ecrire un algorithme qui permet d’afficher le contenu d’un tableau déjà rempli de 5 entiers, du dernier au premier.


table=[]
for i in range(5):
    table.append(int(input('saisissez un entier : ')))
table.reverse()
print(table)
