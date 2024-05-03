import random
def distance():
 cartte = open('c:/Users/diazf/Music/jdr/carte.txt', 'r')
 global ville1
 ville1 =cartte.readline()
 global dsIvl1Ivl2
 dsIvl1Ivl2 =cartte.readline()
 global ville2
 ville2 =cartte.readline()
 print(ville1)
 print(dsIvl1Ivl2)
 print(ville2)

def roll(): # lancer de dé
   global dé       # global c'est pour faire une variable dans un function que lon peut utilisé globalement 
   dé = random.randint(1,12)
   print(dé)
   if dé == 5:
    global embuscade
    embuscade = 1
   else:
    embuscade = 0
distance()

def deplacementt():
 file = open('c:/Users/diazf/Music/jdr/position.txt', 'r')
 positon = file.read()
 file.close
 print('destination:')
 h = input(()) 
 if h == ville2 or ville1:
  print('trage de',positon ,'a',h,'distence',dsIvl1Ivl2,"km")
  rest = int(dsIvl1Ivl2 )
  rast = 0
  while rest > rast:
   rast =(rast +1)
   roll()
  print(embuscade)
  if embuscade == 1:
   print('rencontre hostille')
  file = open('c:/Users/diazf/Music/jdr/position.txt', 'w')
  file.write(h)
  file.close


 
 else :
  print('destination inconue')
 
deplacementt()
