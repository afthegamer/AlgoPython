# Délais de livraison
# Faîtes saisir une quantité de produits, type entier.
# Faîtes choisir à l’utilisateur un mode de livraison : rapide ou normal.
# Indiquez le délai de livraison correspondant à vos données selon le tableau ci-dessous.
# Quantité de Produits Livraison rapide Livraison normale
# < 50 2 jours 4 jours
# 50 <= quantité < 100 3 jours 5 jours
# 100 <= quantité 5 jours 7 jours

print("Entrez la quantité de produits :")
quantity = int(input('saissisez la quantité : '))
print("La quantité de produits est : ", quantity)
modeLivraison = input('saissisez le mode de livraison (rapide ou normal) : ')
if quantity < 50:
    if modeLivraison == 'rapide':
        delaiLivraison = 2
    else:
        delaiLivraison = 4
elif quantity < 100:
    if modeLivraison == 'rapide':
        delaiLivraison = 3
    else:
        delaiLivraison = 5
else:
    if modeLivraison == 'rapide':
        delaiLivraison = 5
    else:
        delaiLivraison = 7
print("Le délai de livraison est : ", delaiLivraison)
# Fin