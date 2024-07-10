import json
from ficheperso import fichepeso
from ficheperso import inputdegat
fichepeso()
inputdegat()
with open("./persos/ficheperso.json", "r") as f:
 data = json.load(f)
 global nom
 nom = (data["nom"])
 global age
 age =(data["age"])
 global taille
 taille =(data["taille"])
 global sexe
 sexe =(data["sexe"])
 global classs
 classs =(data["classs"])
 global pvbasse
 pvbasse =(data["pvbasse"])
 global pvréele
 pvréele =(data["pvreele"])

