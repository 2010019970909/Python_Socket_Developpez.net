# Source : https://python.developpez.com/cours/apprendre-python3/?page=page_20
# Définition d'un serveur réseau rudimentaire
# Ce serveur attend la connexion d'un client

import socket, sys

myLocalIP = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close())for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
HOST = myLocalIP # '192.168.1.168'
PORT = 50000
counter =0	 # compteur de connexions actives

print("Adresse IP du serveur : " + myLocalIP)
print("Port : " + str(PORT) + "\n")

# 1) création du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# 2) liaison du socket à une adresse précise :
try:
  mySocket.bind((HOST, PORT))
except socket.error:
  print("La liaison du socket à l'adresse choisie a échoué.")
  sys.exit
 
while 1:
  # 3) Attente de la requête de connexion d'un client :
  print("Serveur prêt, en attente de requêtes ...")
  mySocket.listen(2)
 
  # 4) Établissement de la connexion :
  connexion, adresse = mySocket.accept()
  counter +=1
  print("Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1]))
 
  # 5) Dialogue avec le client :
  msgServeur ="Vous êtes connecté au serveur de Vincent. Envoyez vos messages."
  connexion.send(msgServeur.encode("Utf8"))
  msgClient = connexion.recv(1024).decode("Utf8")
  while 1:
      print("C>", msgClient)
      if msgClient.upper() == "FIN" or msgClient =="":
          break
      msgServeur = input("S> ")
      connexion.send(msgServeur.encode("Utf8"))
      msgClient = connexion.recv(1024).decode("Utf8")
 
  # 6) Fermeture de la connexion :
  connexion.send("fin".encode("Utf8"))
  print("Connexion interrompue.")
  connexion.close()
 
  ch = input("<R>ecommencer <T>erminer ? ")
  if ch.upper() =='T':
      break
