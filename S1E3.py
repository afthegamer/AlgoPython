# Faîtes saisir une note sur 20, de type réel.
# Convertissez cette note en lettre selon le tableau ci-dessous et affichez la lettre qui correspond
# à la note.
# Note <= 5 Lettre E
# 5 < Note <= 8 Lettre D
# 8 < Note <= 11 Lettre C
# 11 < Note <= 14 Lettre B
# 14 < Note Lettre A
print('donner une not sur 20')
note=float(input('note sur 20 : '))
print('la note que vous aver mis est de : ',note)
if note<=5:
    print('ça note équivaut a un : D')
elif note<=8:
    print('ça note équivaut a un : C')
elif note<=11:
    print('ça note équivaut a un : B')
elif note<=14:
    print('ça note équivaut a un : A')
else:
    print('ça note équivaut a un : A+')
# Compare this snippet from \\wsl.localhost\Ubuntu\home\Python cours\S1E3.py:
