def clienfichier():    
    file = open("./persos/enemi/tep.json", 'w')
    fil = open("./persos/enemi/test.json", 'r')
    x = fil.read()
    file.write(x)
    file.close
    fil.close
clienfichier()
