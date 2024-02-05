## Structures conditionelles
# Id & cie
soleil = False
neige = True
en_semaine = False

if soleil and not en_semaine:
    print("on va à la plage !")
elif neige and en_semaine:
    print("on fait un bonhomme de neige")
else:
    print("on reste à la maison !")

# Match
fruit = "pomme"
match fruit:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print("Je ne connais pas ce fruit.")

## Structures itératives
# For
races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
couleur_de_chien = ['bleu', 'noir', 'blanc', 'rouge']
for chien in races_de_chien:
    print(chien)

for race, couleur in zip(races_de_chien, couleur_de_chien):
    # On peut parcourir deux listes à la fois
    print(f'race: {race}, couleur: {couleur}')

# range(): Boucle 0-99
for x in range(100):
    # print(f"{x} bouteilles de bières au mur !")
    pass

# While: Break et continue marchent aussi pour la boucle for
capacite_maximale = 10
capacite_actuelle = 3
while capacite_actuelle < capacite_maximale:
    if capacite_actuelle == 8:
        break

    if capacite_actuelle == 12:
        continue

    capacite_actuelle += 1


