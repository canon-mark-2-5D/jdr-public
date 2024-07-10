import json
import logging 
from urllib.request import urlopen
url = "https://raw.githubusercontent.com/canon-mark-2-5D/testwebjdr/main/test"
page = urlopen(url)
page
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
etat = 0
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
def fichepeso():
  with open("./enemi/fiche-enemi-1.json", "r") as f:
   data = json.load(f)
   global type
   type = (data["nom"])
   classs =(data["classs"])
   global pvbasse
   pvbasse =(data["pvbasse"])
   global pvréele
   pvréele =(data["pvreele"])

def recherche():
 asc = input(())
 if html == 'test':
  print("samarche")
 elif html == 'sqfmjlk1':
  print("dfsio")
 elif asc == 'stop':
  global etat 
  etat = (1)
while etat == 0:
 recherche()