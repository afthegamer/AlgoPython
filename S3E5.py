# 5 Algorithme de Luhn
# Hans Peter Luhn est un informaticien et ingénieur germano-américain qui a développé cet
# algorithme lors de son passage chez IBM dans les années 1950.
# L'algorithme de Luhn est utilisé pour vérifier divers numéros d'identification, par exemple les
# numéros des cartes de crédits, les codes-barres (exemple ISBN) ou encore les numéros de
# sécurité sociale. Voici comment il fonctionne :
# On démarre avec le dernier chiffre (à droite) et on se déplace vers la gauche, en doublant la valeur
# de tous les chiffres de rang pair : le dernier (c'est-à-dire la clef) est traité en 1er, il n'est pas doublé,
# l'avant-dernier (2e
#
# ) sera doublé. Si le double d'un chiffre dépasse 9, on le remplace par la somme
#
# de ses chiffres.
# Ainsi, sur les positions paires, les chiffres (0;1;2;3;4;5;6;7;8;9) deviennent (0;2;4;6;8;1;3;5;7;9)
# Par exemple, 1 111 devient 2 121, tandis que 8 763 devient 7 733 (car 2×6=12, et 1+2=3 ; 2×8=16, et
# 1+6=7) ;
# On additionne ensemble tous les chiffres du nombre ainsi obtenu. Par exemple, 1111 devient 2121
# dont la somme donne 6 (2+1+2+1) ; tandis que 8763 devient 7733 et 7+7+3+3 donne alors 20 ;
# Si le total est un multiple de 10 (le chiffre des unités est un zéro), alors le nombre est valide, en
# accord avec la formule de Luhn. Sinon il est invalide. Ainsi, 1 111 n'est pas valide (comme montré
# ci-dessus, il aboutit à 6), tandis que 8 763 est valide (comme montré ci-dessus, il aboutit à 20).
# Pour déterminer le chiffre de contrôle ajouté à la fin du numéro, calculer la somme comme décrit
# ci-dessus, deux cas de figure se présentent alors :
#  Si la somme est un multiple de 10, le chiffre de contrôle final est égal à 0 ;
#  Si la somme n'est pas un multiple de 10, modifier le dernier chiffre pour obtenir un multiple de
# 10, soit 10 - (somme % 10) où somme % 10 désigne le reste de la division entière de la somme
# calculée par 10 (ce qui revient à ne garder que le chiffre des unités).
# (Source Wikipedia)
# Exercice à réaliser
# L’exercice à réaliser consiste à demander la saisie d’un numéro de carte bancaire (16 positions
# sans espaces) et ensuite vérifier si le numéro saisi est valide ou non.

# Demander la saisie d’un numéro de carte bancaire (16 positions sans espaces)

def luhn(card_number):
    card_number = [int(i) for i in card_number]
    for i in range(0, 16, 2):
        card_number[i] *= 2
        if card_number[i] > 9:
            card_number[i] -= 9
    return sum(card_number) % 10 == 0

card_number = input("Entrez un numéro de carte bancaire (16 chiffres sans espaces) : ")
if luhn(card_number):
    print("Le numéro de carte bancaire est valide.")
else:
    print("Le numéro de carte bancaire n'est pas valide !")
