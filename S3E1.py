# 1 Calculette
# Exercice à réaliser
# Programmez une calculette simple permettant de faire :
#  des additions
#  des soustractions
#  des multiplications
#  et des divisions.
# Permettez à l’utilisateur d’enchaîner les calculs, par exemple :
# Il tape 2 + 5 et on affiche 7
# Il tape ensuite * 3 et on affiche 21
# Il tape – 1 et on affiche 20
# Il tape / 4 et on affiche 5

print("Bienvenue dans la calculette")
print("si vous souhait fair une addition tapez +")
print("si vous souhait fair une soustraction tapez -")
print("si vous souhait fair une multiplication tapez *")
print("si vous souhait fair une division tapez /")
print("si vous souhait quitter tapez q")
choice=input("que voulez vous faire ? ")
while choice !='q' and choice !='Q':
    if choice == '+':
        a = int(input('saisissez le premier nombre : '))
        b = int(input('saisissez le deuxième nombre : '))
        print("le résultat est : ",a+b)
    elif choice == '-':
        a = int(input('saisissez le premier nombre : '))
        b = int(input('saisissez le deuxième nombre : '))
        print("le résultat est : ",a-b)
    elif choice == '*':
        a = int(input('saisissez le premier nombre : '))
        b = int(input('saisissez le deuxième nombre : '))
        print("le résultat est : ",a*b)
    elif choice == '/':
        a = int(input('saisissez le premier nombre : '))
        b = int(input('saisissez le deuxième nombre : '))
        print("le résultat est : ",a/b)
    choice=input("que voulez vous faire ? ")