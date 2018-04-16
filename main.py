# -*- coding: cp1252 -*-
from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE

try:
        # Lancement du serveur
        print("Lancement du serveur.\n")
        try:
                Popen([executable, 'serveur/serveur.py'], creationflags=CREATE_NEW_CONSOLE)
                # from serveur import serveur
        except:
                print("Erreur, impossible de lancer le serveur.\n")
                input("Appuyez sur n'importe quelle touche pour quitter.")
                exit(2)

        print("Serveur lancé dans la nouvelle fenêtre.\n")
        
        # Lancement du client
        print("Lancement du client.\n")        
        try:
                from client import client
        except:
                print("Erreur, impossible de lancer le client;\n")
                input("Appuyez sur n'importe quelle touche pour quitter.")
                exit(3)

except:
	exit(1) # Erreur inconnue

 
