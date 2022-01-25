from dice import Die

def yatzy():
    #create a list of five dice, all are set to value 1. 
    gameDice = [Die(1),Die(1),Die(1),Die(1),Die(1)]
    
    #Now I want to roll all the gameDice to make them random. 
    for dice in gameDice:
        dice.roll()

    #print("First die: "+str(gameDice[0].returnNr())+" Second die: "+str(gameDice[1].returnNr())+" Third die: "+str(gameDice[2].returnNr())+" Forth die: "+str(gameDice[3].returnNr())+" Fifth die: "+str(gameDice[4].returnNr()))

#I will create a "game" for each line in yatzy and test them as I go. 

#1's


#2's

#3's

#4's

#5's

#6's

#1 pair

#2 pairs

#3 of a kind

#4 of a kind

#Low straight

#High Straight

#Full House

#Chance

#Yatzy/Yahtsee

#To run the main program. 
yatzy()