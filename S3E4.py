# 4 Exercice récursivité : la suite de Fibonacci
# Leonardo Fibonacci est un mathématicien italien du XIIIe siècle, célèbre pour avoir introduit en
# Europe le système de numération indo-arabe, incluant le chiffre zéro. Il a joué un rôle majeur dans
# le développement des mathématiques occidentales.
# Également célèbre pour la suite de nombres qui porte son nom, appelée la "suite de Fibonacci".
# Cette suite est définie en commençant par les nombres 0 et 1, et chaque nombre suivant est la
# somme des deux nombres précédents. Ainsi, la suite commence par : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
# et ainsi de suite.
# Cette suite apparaît dans de nombreux phénomènes naturels et a de nombreuses applications en
# mathématiques, en sciences et en informatique.
# Exercice à réaliser
# Faire saisir un entier.
# Calculer la valeur de la suite de Fibonacci au rang de cet entier avec deux méthodes différentes :
#  en utilisant une boucle
#  en utilisant la récursivité

# Méthode 1 : en utilisant une boucle
n=int(input("Entrez un entier : "))
a,b=0,1
for i in range(n-1):
    a,b=b,a+b
print(a)

# Méthode 2 : en utilisant la récursivité
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("Entrez un entier : "))
print(fibo(n))
