print(" ▄▄▄       ██▓███   ▒█████   ▄████▄   ▄▄▄       ██▓   ▓██   ██▓ ██▓███    ██████ ▓█████   █████▒██▀███   ▄▄▄       ███▄    █  ▄████▄  ")
print("▒████▄    ▓██░  ██▒▒██▒  ██▒▒██▀ ▀█  ▒████▄    ▓██▒    ▒██  ██▒▓██░  ██▒▒██    ▒ ▓█   ▀ ▓██   ▒▓██ ▒ ██▒▒████▄     ██ ▀█   █ ▒██▀ ▀█  ")
print("▒██  ▀█▄  ▓██░ ██▓▒▒██░  ██▒▒▓█    ▄ ▒██  ▀█▄  ▒██░     ▒██ ██░▓██░ ██▓▒░ ▓██▄   ▒███   ▒████ ░▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒▒▓█    ▄ ")
print("░██▄▄▄▄██ ▒██▄█▓▒ ▒▒██   ██░▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░     ░ ▐██▓░▒██▄█▓▒ ▒  ▒   ██▒▒▓█  ▄ ░▓█▒  ░▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒")
print(" ▓█   ▓██▒▒██▒ ░  ░░ ████▓▒░▒ ▓███▀ ░ ▓█   ▓██▒░██████▒ ░ ██▒▓░▒██▒ ░  ░▒██████▒▒░▒████▒░▒█░   ░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░▒ ▓███▀ ░")
print(" ▒▒   ▓▒█░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░  ██▒▒▒ ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒ ░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░")
print("  ▒   ▒▒ ░░▒ ░       ░ ▒ ▒░   ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░▓██ ░▒░ ░▒ ░     ░ ░▒  ░ ░ ░ ░  ░ ░       ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░  ▒   ")
print("  ░   ▒   ░░       ░ ░ ░ ▒  ░          ░   ▒     ░ ░   ▒ ▒ ░░  ░░       ░  ░  ░     ░    ░ ░     ░░   ░   ░   ▒      ░   ░ ░ ░        ")
print("      ░  ░             ░ ░  ░ ░            ░  ░    ░  ░░ ░                    ░     ░  ░          ░           ░  ░         ░ ░ ░      ")
print("                            ░                          ░ ░                                                                   ░        ")
print('pour afficher les commendes  tapées commende-help')
import random
import logging 
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
etat = 0
def roll(): # lancer de dé ps penssé a metre une sécurité  pour les génie comme nicola qui mette des nombre negatif  bref les petit flan portugay c'est bon ^_~
 try :  
   print("entré  quel type de dé a émuler ex: dé 20")
   nombre = int(input(()))
   global dé        
   dé = random.randint(1,nombre)
   print(dé)
 except:
  logging.exception('')
  pass



def nanjur():
 s = input(()) 
 

     
 if s == 'fiche-perso//vide//':
   print(' nom []')
   print(' age []')
   print(' taille []')
   print(' taille sexe []')
   print(' class []')
 
 elif s == 'dé-roll':
  roll()

 elif s == 'fiche-perso':
  from ficheperso import fichepeso
  from ficheperso import aficherfiche
  fichepeso()
  aficherfiche()

 # pas mit dans la liste des commende mais c'est des sovage du coup 
 elif s == 'quitter':
   global etat 
   etat = 1

 elif s == 'trajet':
  from cartav2 import deplacementt
  deplacementt()

 elif s == 'degat':
  from ficheperso import fichepeso
  from ficheperso import inputdegat
  fichepeso()
  inputdegat()
 # le truc endesous est sencer marcher mais sa marche pas du coup flemme  est puis les print sa marche bien  est  puis quit lit les commentaire de codes il est 3h 41  est je suis en insomenie bref 
 # elif s == "commende-help": 
  #hel = open('./persos/help.txt', 'r')
  #hels = hel.read()
  #print(hels)
  #hel.close

 elif s == "commende-help":
  print(' liste des commendes ')
  print(' ortographe corect non fournie ')
  print(' ')
  print(' dé-roll ')
  print(' -> fait un lancer de dé  avec un nombre  entré  ')
  print(' ')
  print(' ')
  print(' fiche-perso')
  print(' -> afiche la fiche perso ')  
  print(' ')
  print(' l avent dernier nombres est le nombre de pv de basse est le dernier est selui actuel')
  print(' ')
  print(' ')
  print(' trajet') 
  print(' -> permet de se déplacer  de ville en ville ')
  print(' ')
  print(' pour se déplacer vérifier que les 2 ville soit bien  relier sur la carte  si non relier ')
  print(' passé par une ville qui est entre votre destination ')
  print(' ')
  print(' ps( bug non fixé  donc si un 5 est présent dans la liste de nombres qui est afichier ')
  print(' sé le signe d une embuscade) ')
  print(' ')
  print(' ')
  print(' ')
  print(' degat ')
  print(' ->    pour se retier des pv ex si vous vous prenez  4 dégat écrivé 4 ')
  print('')
  print(' carte-afiche')
  print('commende pour ouvrir une feneitre avec la carte aficher')
  print('')
  print(' lien-github')
  print('dit dans le nom')
  print("host")
  print('ouvre un serveur commme maitre du jeux')
 elif s == 'lien-github':
  from testweb import weblien
  weblien()
 elif s == "host":
  from host import host
  host()
  


 elif s == "carte-afiche":
  from afichecart import afiche
  afiche()
while  etat  == 0:
 nanjur()