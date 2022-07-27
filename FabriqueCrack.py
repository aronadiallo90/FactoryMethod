from BruteForce import BruteForce
from Dictionnaire import Dictionnaire


class FabriqueCrack:

    @staticmethod 
    def getInstance(choix):
        if choix == 1:
           return BruteForce()
        elif choix ==2:
             if choix == 2:
              return Dictionnaire() 