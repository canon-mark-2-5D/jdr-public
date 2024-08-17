#!/usr/bin/env python3
  
from combat11 import comba

import socket
adresseIP = "127.0.0.1"	# Ici, le poste local
port = 51000	# Se connecter sur le port 50000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((adresseIP, port))
print("Connecté au serveur")
print("Tapez FIN pour terminer la conversation. ")
message = ""
while message.upper() != "FIN":
	message = input("> ")
	if message == 'combat':
		client.send(message.encode("utf-8"))
		reponse = client.recv(255)
		file = open("./persos/enemi/tep.json", 'w')
		x = reponse.decode("utf-8")
		file.write(x)
		file.close
		print(reponse.decode("utf-8"))		
		comba()
	else:
		client.send(message.encode("utf-8"))
		reponse = client.recv(255)
		print(reponse.decode("utf-8"))
print("Connexion fermée")
client.close()