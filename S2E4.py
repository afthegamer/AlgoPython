
# 4 Ecrire l’algorithme qui permet d’inverser les valeurs contenues dans un tableau de 10 entiers
# (la valeur contenue dans la première case du tableau passe dans la dernière case alors que
# celle contenue dans la dernière passe dans la première, la seconde passe dans l’avant
# dernière etc ...)

table=[]
for i in range(10):
    table.append(int(input('saisissez un entier : '))
)
print(table)
for i in range(5):
    table[i],table[9-i]=table[9-i],table[i]
print(table)