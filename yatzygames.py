from dice import Die

#I will create a "game" for each line in yatzy and test them as I go.
#The upper section will be the same for all, except the number, therefore I create one game for all.
def upperSection(gameDice,number):
    results=[] #This will be a list with all the results in integers, not the dice objects. 
    for i in range(3):
        for dice in gameDice:
            dice.roll()
            if dice.returnNo()==number:
                results.append(dice.returnNo())
                gameDice.remove(dice)
    for element in results:
        gameDice.append(Die()) #I removed the Die element, must return them to the list. In case I forget to reset the dice in the main program. 
    points=sum(results)
    return points 

#1 pair
def onepair(gameDice):
    results=[]
    #Sort the values of the dice. Compare two dice together from the top. If they are the same, remove them from gameDice and put them into results list. 
    for i in range(3):
        values=[]
        for dice in gameDice:
            dice.roll()
            values.append(dice.returnNo())
        sortedvalues=sorted(values,reverse=True)
        for i in range(len(sortedvalues)-1):
            if sortedvalues[i]==sortedvalues[i+1]:
                results.extend(sortedvalues[i:i+2])
                gameDice=gameDice[:-2] #everything except the two last elements. 
                break
    
    print(sortedvalues)
    print(results)

#2 pairs, 3 of a kind, 4 of a kind, Low straight, High Straight, Full House, Chance, Yatzy/Yahtsee

def yatzy():
    #create a list of five dice, all are set to value 1. 
    gameDice = [Die(),Die(),Die(),Die(),Die()]

    #First game:
    ones=upperSection(gameDice,1)
    print(ones)
    gameDice = [Die(),Die(),Die(),Die(),Die()] #Resetting the dice. 

    #One pair:
    onepair(gameDice)
    gameDice = [Die(),Die(),Die(),Die(),Die()] #Resetting the dice. 

yatzy()