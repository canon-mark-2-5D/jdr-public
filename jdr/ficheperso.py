import json
def fichepeso():
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

def aficherfiche():
   print(nom)
   print(age)
   print(taille)
   print(sexe)
   print(classs)
   print('point de vie de basse' ,pvbasse)
   print('point de vie restant' ,pvréele)

def inputdegat():
 fichepeso()
 print('dégat prie')
 s = int(input(()))
 
 pvnow = (int(pvréele) - s)

 with open("./persos/ficheperso.json", "r") as ff:
   ata = json.load(ff)
   ata["pvreele"] = pvnow  # Modifie une valeur existante
   with open('./persos/ficheperso.json', 'w') as fw:
    json.dump(ata, fw, indent=4)  # Indentation de 4 pour une meilleure lisibilité

    

