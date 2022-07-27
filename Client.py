
from FabriqueCrack import FabriqueCrack


# password = input("Veillez entrer le mot de pass à pirater :")   
choix = int( input("Veillez choisir 1 pour BruteForce  2 pour Attaque par dictionnaire :")  )
FabriqueCrack.getInstance(choix).cracker()