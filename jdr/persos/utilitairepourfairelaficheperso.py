

inp = input(())
a = 'dqdsjfds \n dddd'
b = { "nom": "Guilhem", "age": "16", "taille": "182", "sexe": "homme", "classs": "soldat", "pvbasse": "100", "pvreele": 100, "posistion": "ville-fort" }


file = open('c:/Users/diazf/Music/jdr/alll.json', 'w')
file.writelines(a)
file.writelines(b)
file.close