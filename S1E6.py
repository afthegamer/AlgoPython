# Calcul d’une facture selon le nombre de photocopies effectuées (calculs par paliers).
# Voici comment sont facturées les photocopies dans un service de reproduction.
# Les 10 premières photocopies sont facturées au prix de 0.1 euro par photocopie.
# Entre 11 et 20 photocopies : les 10 premières sont au prix de 0.1 euros par photocopie, les
# suivantes sont au prix de 0.08 euro par photocopie.
# Entre 21 et 50 photocopies : les 10 premières sont au prix de 0.1 euros par photocopie, les 10
# suivantes sont au prix de 0.08 euro par photocopie, et les suivantes sont au prix de 0.06 euro
# par photocopie.
# A partir de 51 photocopies : les 10 premières sont au prix de 0.1 euros par photocopie, les 10
# suivantes sont au prix de 0.08 euro par photocopie, les 30 suivantes sont au prix de 0.06 euro
# par photocopie, et ensuite chaque photocopie coûte 0.03 euro.
# Faites saisir un nombre de photocopies et affichez-le.
# Calculez le montant de la facture correspondante et affichez-le.

print("Entrez le nombre de photocopies :")
nbCopies = int(input('saissisez le nombre de photocopies : '))
print("Le nombre de photocopies est : ", nbCopies)
if nbCopies <= 10:
    prixCopie = 0.1
elif nbCopies <= 20:
    prixCopie = 0.08
elif nbCopies <= 50:
    prixCopie = 0.06
else:
    prixCopie = 0.03
montantFacture = 0
for i in range(nbCopies):
    montantFacture += prixCopie
print("Le montant de la facture est : ", montantFacture)
# Fin