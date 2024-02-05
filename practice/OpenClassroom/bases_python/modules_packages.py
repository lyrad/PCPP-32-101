import structures_fonctions_exceptions
from structures_fonctions_exceptions import retour_multiple

import mon_package.module
from mon_package.module import ma_fonction_1

print("MODULES: ")
results = structures_fonctions_exceptions.retour_multiple()
print(results)
results = retour_multiple()
print(results)

print("PACKAGES: ")
results = mon_package.module.ma_fonction()
print(results)

results = mon_package.module.ma_fonction_1()
print(results)
