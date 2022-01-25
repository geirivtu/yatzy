from pickle import APPEND
from dice import Die

#I will create a "game" for each line in yatzy and test them as I go.
#The upper section will be the same for all, except the number, therefore I create one game for all.
def upperSection(gameDice,number):
    gameDice=gameDice
    for dice in gameDice:
        dice.roll()
    results=[]

    #We have two more chances to get more 1's and all 1's should be added to results. 
    for dice in gameDice:
        if dice.returnNo()==number:
            results.append(dice.returnNo())
            gameDice.remove(dice)

    #Last time to get those numbers. 
    for dice in gameDice:
        if dice.returnNo()==number:
            results.append(dice.returnNo())
            gameDice.remove(dice)

    print(results) #The results seem too low. Need to fix this later. 

    #1 pair

    #2 pairs

    #3 of a kind

    #4 of a kind

    #Low straight

    #High Straight

    #Full House

    #Chance

    #Yatzy/Yahtsee

def yatzy():
    #create a list of five dice, all are set to value 1. 
    gameDice = [Die(1),Die(1),Die(1),Die(1),Die(1)]
    
    #Now I want to roll all the gameDice to make them random. 
    for dice in gameDice:
        dice.roll()

    #print("First die: "+str(gameDice[0].returnNo())+" Second die: "+str(gameDice[1].returnNo())+" Third die: "+str(gameDice[2].returnNo())+" Forth die: "+str(gameDice[3].returnNo())+" Fifth die: "+str(gameDice[4].returnNo()))

    #First game:
    upperSection(gameDice,1)


#To run the main program. 
yatzy()