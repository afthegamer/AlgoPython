# Calculs HT et remises
# Faîtes saisir une quantité de produits de type réel, et affichez la.
# Faîtes saisir un prix unitaire hors-taxes de type réel, et affichez le.
# Calculez le montant total hors-taxes de type réel, et affichez-le.
# Appliquez une remise selon le tableau ci-dessous et affichez le prix remisé de type réel.
# Montant total hors-taxes < 200 Taux de remise : 2,5 %
# 200 <= Montant total hors-taxes < 400 Taux de remise : 5 %
# 400 <= Montant total hors-taxes < 700 Taux de remise : 7,5 %
# 700 <= Montant total hors-taxes Taux de remise : 10 %
# Calculez le montant de la TVA en appliquant un taux de TVA de 20%, et affichez ce montant de
# TVA.
# Calculez le montant TTC de type réel et affichez-le.

print("Entrez la quantité de produits :")
quantity = float(input('saissisez la quantité : '))
print("La quantité de produits est : ", quantity)
prixUnitaire = float(input('saissisez le prix unitaire HT : '))
print("Le prix unitaire hors-taxes est : ", prixUnitaire)
montantHT = quantity * prixUnitaire
print("Le montant total hors-taxes est : ", montantHT)
if montantHT < 200:
    tauxRemise = 2.5
elif montantHT < 400:
    tauxRemise = 5
elif montantHT < 700:
    tauxRemise = 7.5
else:
    tauxRemise = 10
montantRemise = montantHT * (tauxRemise / 100)
print("Le montant de la remise est : ", montantRemise)
montantTTC = montantHT - montantRemise
print("Le montant TTC est : ", montantTTC)
montantTVA = montantTTC * 0.2
print("Le montant de la TVA est : ", montantTVA)
# Fin