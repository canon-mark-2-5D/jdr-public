import random
import json

def lacarta():
 with open("./AD&D-Json/caerz.json", "r") as f:
   data = json.load(f)
   global ville1
   ville1 = (data["ville1"])
   global ville2
   ville2 =(data["ville2"])
   global ville3
   ville3 =(data["ville3"])
   global ville4
   ville4 =(data["ville4"])
   global ville5
   ville5 =(data["ville5"])
   global ville6
   ville6 =(data["ville6"])







def distance():
 with open("./persos/ficheperso.json", "r") as fr:
   aa = json.load(fr)
 filurl = (aa["posistion"])
 txt = "./AD&D-Json/place-{}.json"

 filurl2 = (txt.format(filurl))
 with open(filurl2, "r") as f:
   data = json.load(f)
   global nomposition
   nomposition = (data["name"])
   global place1
   place1 =(data["place1"])
   global distance1
   distance1 =(data["distance1"])
   global place2
   place2 =(data["place2"])
   global distance2
   distance2 =(data["distance2"])
   global place3
   place3 =(data["place3"])
   global distance3
   distance3 =(data["distance3"])
distance()


def roll(): # lancer de dé
   global dé       # global c'est pour faire une variable dans un function que lon peut utilisé globalement 
   dé = random.randint(1,12)
   print(dé)
   if dé == 5:
    global embuscade
    embuscade = (1)
distance()

def deplacementt():
 print('destination:')
 h = input() 
 if h == place1:
   distancekm = distance1
 elif h == place2:
   distancekm = distance2
 elif h == place3:
   distancekm = distance3
 else:
   print('destination non atégnable ou non existante')
   return

 print('trage de',nomposition ,'a',h,'distence',distancekm,"km")
 rest = int(distancekm )
 rast = 0
 embuscade = (0)
 while rest > rast:
  rast =(rast +1)
  roll()
  if dé == 5:
   embuscade = (embuscade + 1)
 print(embuscade)
 if embuscade > 1:
  print('rencontre hostille')
 embuscade = 0
 with open("./persos/ficheperso.json", "r") as ff:
  ata = json.load(ff)
  ata["posistion"] = h  # Modifie une valeur existante
  with open('./persos/ficheperso.json', 'w') as fw:
   json.dump(ata, fw, indent=4)  # Indentation de 4 pour une meilleure lisibilité
