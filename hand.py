from random import random
from random import randint

class Hand(list):
    def __init__(self,alist):
        list.__init__(self,alist)

    def showHand(self):
        return self

    def rolls(self):
        length=len(self)
        for i in range(len(self)):
            self[i]=randint(1,6)
        return self

if __name__ == "__main__":
    hand=Hand()
    print(hand)
