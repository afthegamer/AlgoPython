# 3 Exercice récursivité : la fonction factorielle
# La factorielle d'un nombre entier positif, notée avec un point d'exclamation (!), est le produit de
# tous les entiers positifs inférieurs ou égaux à ce nombre.
# Par exemple, la factorielle de 5 (notée 5!) est égale à 5 × 4 × 3 × 2 × 1, ce qui donne 120.
# En termes mathématiques, la factorielle d'un nombre n’est définie comme ceci :
# n! = n * (n – 1) * (n – 2) * ... * 2 * 1
# Exercice à réaliser
# Faire saisir un entier.
# Calculer la factorielle de cet entier avec deux méthodes différentes :
#  en utilisant une boucle
#  en utilisant la récursivité

# Méthode 1 : en utilisant une boucle
n=int(input("Entrez un entier : "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

# Méthode 2 : en utilisant la récursivité
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Entrez un entier : "))
print(fact(n))
