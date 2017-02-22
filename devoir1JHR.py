# coding: utf-8 # N'oublie pas cette première ligne; pour imprimer uniquement des nombres, on n'en pas pas formellement besoin, mais elle devient nécessaire dès qu'on manipule du texte accentué, ce qui nous arrive souvent en français :)

b = list(range(30000,100000))
print(["{:05d}".format(item) for item in b])
# Wow! Tu as trouvé comment imprimer une liste formée avec une boucle en une seule ligne.
# En s'inspirant de cette syntaxe, il aurait même été possible de joindre tes deux lignes en une seule ainsi:
# print(["{:05d}".format(b) for b in list(range(30000,100000))])

a = list(range(00000,18000))
print(["{:05d}".format(item) for item in a])

##########

# Solution astucieuse!
# Afin d'utiliser chaque numéro de permis pour vérifier s'il correspond à un médecin qui est ou a déjà été membre du Collège des médecins, il est plus intéressant de les utiliser un après l'autre.
# Pour faire ça avec ta solution, voici ce que j'aurais fait:

# D'abord créer une liste à partir des deux que tu as créées:

c = b + a

# Ensuite, on peut imprimer chaque élément de cette liste en utilisant le même formatage que celui que tu as utilisé:

for noPermis in c:
	print("{:05d}".format(noPermis))