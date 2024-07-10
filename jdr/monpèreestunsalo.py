import json
import logging 
import csv
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
def fichepeso():
  with open("./persos/fzendesk.json", "r") as f:
   data = json.load(f)
   global nom
   nom = (data["author_name"])
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

fichepeso()


with open('./persos/mon_fichier.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["nom", "age"])
    writer.writerows([[nom, age], ["nom", age]])