from hand import Hand

def manyOfOne(number):
    rollinghand=Hand([1,2,3,4,5])
    resulthand=Hand([])
    for i in range(3):
        rollinghand.rolls()
        for dice in rollinghand:
            if dice==number:
                resulthand.append(dice)
                rollinghand.remove(dice)
    return resulthand

def onepair(gameDice):
    results=[]
def twopairs(gameDice):
    results=[]

def threeofakind(gameDice):
    results=[]

def fourofakind():
    results=[]

def lowstraight():
    results=[]

def highstraight():
    results=[]

def fullhouse():
    results=[]

def chance():
    results=[]

def yahtsee():
    results=[]

def yatzy():
    ones=manyOfOne(1)
    print(ones)
    twos=manyOfOne(2)
    print(twos)
    threes=manyOfOne(3)
    print(threes)
    fours=manyOfOne(4)
    print(fours)
    fives=manyOfOne(5)
    print(fives)
    sixes=manyOfOne(6)
    print(sixes)
    points=sum(ones)+sum(twos)+sum(threes)+sum(fours)+sum(fives)+sum(sixes)
    if points>=50:
        points+=50
    print(points)

if __name__ == "__main__": #This will not be run if yatzygames gets imported to another file. 
    yatzy()