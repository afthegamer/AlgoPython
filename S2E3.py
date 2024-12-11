# 3 Ecrire l’algorithme qui permet de constituer une table de multiplication de 9 par 9.
table=[]
for i in range(9):
    table.append([])
    for j in range(9):
        table[i].append((i+1)*(j+1))
print(table)
