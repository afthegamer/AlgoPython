# Début
#     Écrire "Entrez la première variable (v1) :"
#     Lire v1
#     Écrire "La valeur de v1 est : ", v1
#
#     Écrire "Entrez la deuxième variable (v2) :"
#     Lire v2
#     Écrire "La valeur de v2 est : ", v2
#
#     Temp <- v1
#     v1 <- v2
#     v2 <- Temp
#
#     Écrire "Après inversion, la valeur de v1 est : ", v1
#     Écrire "Après inversion, la valeur de v2 est : ", v2
# Fin
#
# Inversion du contenu de deux variables
# Faîtes saisir une première variable nommée v1, de type entier, et affichez-la.
# Faîtes saisir une deuxième variable nommée v2, de type entier, et affichez-la.
# Inversez le contenu des deux variables et affichez les deux variables une fois qu’elles sont
# inversées.

print("Entrez la première variable (v1) :")
v1 = int(input('saissisez la valeur de v1 : '))
print("La valeur de v1 est : ", v1)
v2= int(input('saissisez la valeur de v2 : '))
print("La valeur de v2 est : ", v2)
v3 = v1
v1 = v2
v2 = v3
print("Après inversion, la valeur de v1 est : ", v1)
print("Après inversion, la valeur de v2 est : ", v2)