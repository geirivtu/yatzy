from random import random
from random import randint

#Defining one die and creating a function for rolling it. 

class Die:
    def __init__(self):
        self._no=None

    def roll(self):
        self._no=randint(1,6)

    def returnNo(self):
        return self._no