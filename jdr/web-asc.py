
import urllib.request

url = "https://www.zendesk.fr/marketplace/apps/?class.name=AI+and+Bots"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)
page = urllib.request.urlopen(req)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# Ajouter un retour à la ligne après chaque '>'
html = html.replace('"', '"\n')
html = html.replace('support', 'support\n')

print(html)



def chercher_mot_et_suivant_variable(variable, mot):
    position = variable.find(mot)
    if position != -1:
        debut = position + len(mot)
        fin = debut + 25
        return variable[debut:fin]
    else:
        return "Le mot n'a pas été trouvé dans la variable."

# Utilisation de la fonction
ma_variable = "Ceci est un exemple de texte dans lequel nous allons chercher un mot."
print(chercher_mot_et_suivant_variable(html, 'support'))

def chercher_suite_et_suivant_variable(variable, suite):
    position = variable.find(suite)
    if position != -1:
        debut = position + len(suite)
        fin = debut + 20
        return variable[debut:fin]
    else:
        return "La suite de caractères n'a pas été trouvée dans la variable."

# Utilisation de la fonction
ma_variable = "Ceci est un exemple de texte dans lequel nous allons chercher une suite de caractères."
print(chercher_suite_et_suivant_variable(html, 'https://www.zendesk.fr/marketplace/apps/support/1038068/shopify-ai-agent-by-adelante/?queryID=30d6698ab40cdd3748314b3ef67ae01b'))

import urllib.request
from bs4 import BeautifulSoup

url = "https://www.zendesk.fr/marketplace/apps/?class.name=AI+and+Bots&page=1&star=1"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)
page = urllib.request.urlopen(req)
html_bytes = page.read()

# Utiliser BeautifulSoup pour extraire le contenu du <body>
soup = BeautifulSoup(html, 'html.parser')
body = soup.body

# Ajouter un retour à la ligne après chaque '>'
body_html = str(body)

print(body_html)


def chercher_mot_et_suivant_variable(variable, mot):
    position = variable.find(mot)
    if position != -1:
        debut = position + len(mot)
        fin = debut + 25
        return variable[debut:fin]
    else:
        return "Le mot n'a pas été trouvé dans la variable."

# Utilisation de la fonction
ma_variable = "Ceci est un exemple de texte dans lequel nous allons chercher un mot."
print(chercher_mot_et_suivant_variable(body_html, 'col'))