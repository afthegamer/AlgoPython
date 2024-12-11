# Comparaison de 2 offres téléphoniques.
# Vous êtes opérateur téléphonique et vous proposez deux offres à vos clients.
# 1
# ère offre : coût fixe de 10 euros + coût variable de 0.05 euros par minute consommée
# 2
# ème offre : coût fixe de 20 euros + coût variable de 0.02 euros par minute consommée
# Demandez à votre client quelle est sa consommation habituelle en minutes et proposez lui
# l’offre la plus avantageuse pour lui.

print("Entrez votre consommation habituelle en minutes :")
consommation = float(input('saissisez la consommation habituelle en minutes : '))
print("La consommation habituelle en minutes est : ", consommation)
offre1 = 10 + 0.05 * consommation
offre2 = 20 + 0.02 * consommation
if offre1 < offre2:
    print("L'offre la plus avantageuse pour vous est l'offre 1 : ", offre1)
else:
    print("L'offre la plus avantageuse pour vous est l'offre 2 : ", offre2)
# Fin