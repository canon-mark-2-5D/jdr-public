import json
import logging 
import random
def roll(): # lancer de dé ps penssé a metre une sécurité  pour les génie comme nicola qui mette des nombre negatif  bref les petit flan portugay c'est bon ^_~
 try :  
   print("entré  quel type de dé a émuler ex: dé 20")
   nombre = int(input(()))
   global dé        
   dé = random.randint(1,nombre)
   print(dé)
 except:
  logging.exception('')

def ficheenemi():
  with open("./persos/enemi/tep.json", "r") as ff:
   ata = json.load(ff)
   global type1
   type1 = (ata["nom"])
   global classs1
   classs1 =(ata["classs"])
   global pvbasse1
   pvbasse1 =(ata["pvbasse"])
   global pvréele1
   pvréele1 =(ata["pvreele"])
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
ficheenemi()
fichepeso()
def combat():   

  pvnow = pvréele
  pvnow1 = pvréele1
  while pvnow and pvnow1 > 0:
    a =str(pvnow)
    b =str(pvnow1)
    print("pv ", a)
    print('pv adverse ', b)
    print('list attaque')
    print("1 -> balle normal")
    print("2 -> balle expencive")
    print("3 -> sabre")

    s = int(input('> entré le numéro de votre attaque'))
    try:
      if s == 1:
        attaqueper = random.randint(1,10)
      elif s == 2:
        attaqueper = random.randint(5,9)
      elif s == 3:
        h = random.randint(1,20)
        attaqueper = (h - 5)
    except:
      logging.exception('')
    pvnow1 =(pvnow1 - attaqueper)
    print('dégat fait ')
    print(attaqueper)
    dé1 = random.randint(1,10)
    pvnow = (pvnow - dé1)
    print('dégat prie')
    print(dé1)
  print('win')
combat()