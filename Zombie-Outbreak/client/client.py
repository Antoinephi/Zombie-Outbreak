'''
Created on 31 janv. 2013

@author: philippa
'''

from carte import Coordonnees, CaseWater, Arena
import socket
import sys

print(sys.version)

# infos de connexion au serveur
hote = "localhost"
port = 8080
pseudo  = "toto"

# connexion au serveur
def connection():
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con.connect((hote, port))
    return con

# identification du joueur 
def login():
    print("Saisir votre pseudo : "),
    nick = input()
    return nick

# recupere les infos de config de la partie 
def config(msg): 
    for i in range(msg.__len__()):
        if(msg[i] == "end"):
            print(msg[i] + " !!!!")
        else :    
            print(msg[i])
        msg_w = msg[i].rsplit(" ")
        if(msg_w.__len__() > 2 and msg_w[0] == "water"):   
            coo = Coordonnees(msg_w[1], msg_w[2])
            c = CaseWater(coo)
            arene.setCase(msg_w[1], msg_w[2], c)
        i += 1
        
#nick = login()
print(sys.version)
connexion_client = connection()
print("connecte au serveur")

connexion_client.sendall("nick %s \n" % ("toto"))
print("ok")
msg_recu = connexion_client.recv(10000)
config(msg_recu.rsplit("\n"))
arene = Arena.Arena(50,50)
while(msg_recu != ""):
        msg_recu = connexion_client.recv(10000)
        config(msg_recu.rsplit("\n"))
        
        
        pass

connexion_client.close()