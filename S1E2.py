# Calculs HT, TVA et TTC
# Faîtes saisir un montant hors-taxes de type réel, et affichez-le.
# Faîtes saisir un taux de TVA de type réel, et affichez-le.
# Calculez le montant de la TVA de type réel, et affichez-le.
# Calculez le montant TTC de type réel, et affichez-le.

print("Entrez le montant hors-taxes :")
montantHT = float(input('saissisez le montant HT : '))
print("Le montant hors-taxes est : ", montantHT)
tauxTVA = float(input('saissisez le taux de TVA : '))
print("Le taux de TVA est : ", tauxTVA, "%")
montantTVA = montantHT * (tauxTVA / 100)
print("Le montant de la TVA est : ", montantTVA)
montantTTC = montantHT + montantTVA
print("Le montant TTC est : ", montantTTC)
# Fin