# Faites saisir un prix unitaire de produit, type réel.
# Calculez le nouveau prix unitaire selon le tableau ci-dessous.
# Prix unitaire Pourcentage d’augmentation
# <20 10 %
# 20 <= prix <50 7,5 %
# 50<= prix <100 5 %
# 100 <= prix 2,5 %

print("Entrez le prix unitaire du produit :")
prixUnitaire = float(input('saissisez le prix unitaire : '))
print("Le prix unitaire est : ", prixUnitaire)
if prixUnitaire < 20:
    pourcentageAugmentation = 10
elif prixUnitaire < 50:
    pourcentageAugmentation = 7.5
elif prixUnitaire < 100:
    pourcentageAugmentation = 5
else:
    pourcentageAugmentation = 2.5
nouveauPrixUnitaire = prixUnitaire + (prixUnitaire * (pourcentageAugmentation / 100))
print("Le nouveau prix unitaire est : ", nouveauPrixUnitaire)
# Fin