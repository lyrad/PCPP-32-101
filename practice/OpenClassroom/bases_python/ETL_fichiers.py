import requests, csv
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.title
print(title.string)

descriptions_bs = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptions = []
titres = []

for desc in descriptions_bs:
    descriptions.append(desc.string)
    titres.append(title.string)

print(descriptions)

## Fichiers
# Modes: r, w (ecraser), a (append), r+ (read and append), et une armée d'autres...
fichier = open("ETL_fichiers.txt", "w")
for desc in descriptions:
    fichier.write(desc)
fichier.close()

# with ferme automatiquement le fichier à la fin du bloc
with open("ETL_fichiers.txt", 'r') as fichier:
    for ligne in fichier:
        print(ligne)

## Package CSV
# Lire
with open('ETL_fichiers.csv') as fichier_csv:
    # Retourne une liste avec toutes les lignes en row
    # reader = csv.reader(fichier_csv, delimiter=',')
    # Lecture 'intelligente': retourne un dictionnaire avec nom de colonnes (1er ligne = indexes), supprimer 1er colonne
    reader = csv.DictReader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne)

# Ecrire
en_tete = ["titre", "description"]
with open('ETL_fichiers.csv', 'w') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=',')
    writer.writerow(en_tete)

    for titre, description in zip(titres, descriptions):
        ligne = [titre, description]
        writer.writerow(ligne)

