from random import random
from random import randint

#Defining one die and creating a function for rolling it. 

class Die:
    def __init__(self,nr):
        self._nr=nr

    def roll(self):
        self._nr = randint(1,6)

    def returnNr(self):
        return self._nr