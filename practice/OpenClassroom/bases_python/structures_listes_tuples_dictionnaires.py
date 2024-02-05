## Les listes (PHP: arrays)

plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter", "TikTok"]
plateformes_sociales[2] = 'SnapChat'

print(plateformes_sociales)
print(plateformes_sociales[2])
print(len(plateformes_sociales))

plateformes_sociales.append("Slack")
plateformes_sociales.extend(["Github", "Youtube"])
plateformes_sociales.sort()
plateformes_sociales.insert(2, "Slack")

print(plateformes_sociales)
print(plateformes_sociales.count('Slack'))

plateformes_sociales.reverse()
plateformes_sociales.pop()
plateformes_sociales.remove('TikTok')
print(plateformes_sociales)
plateformes_sociales.clear()

## Les tuples (qui sont listes immuables)
plateformes_sociales_tuple = ("Facebook", "Instagram", "TikTok", "Twitter")

# In: fonctionne sur les listes, les tuples et les dictionnaires (clé)
print('Twitter' in plateformes_sociales_tuple)

## Les dictionnaires (PHP: associative arrays)
dictionnaire = dict()
dictionnaire1 = {}

nouvelle_campagne = {
    "responsable_de_campagne": "Jeanne d'Arc",
    "nom_de_campagne": "Campagne nous aimons les chiens",
    "date_de_début": "01/01/2020",
    "influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"],
    "key_does_not_exist": "None",
}

nouvelle_campagne['date_de_fin'] = '31/01/2020'
del nouvelle_campagne['influenceurs_importants']

print(nouvelle_campagne)
print(nouvelle_campagne['nom_de_campagne'])
print(nouvelle_campagne.keys())
print(nouvelle_campagne.values())
print(nouvelle_campagne.items())
print(nouvelle_campagne.get('nom_de_campagne'))

# Fonctions à la con qui retournent None quand index pas trouvé.
print(nouvelle_campagne.get('key_does_not_exist'))
print(nouvelle_campagne.pop('key_does_not_exist'))
# print(nouvelle_campagne.pop('key_does_not_exist')) Exception (et non None retourné)
print(nouvelle_campagne.get('key_does_not_exist'))




