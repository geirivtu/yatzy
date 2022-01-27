from dice import Die
from yatzygames import upperSection

def testprogram():
    #Run the program for upper section 1000 times and check if the results are probable.
    #If I try to get 2's, the average result should be... after 1000 tries. 

    rolleddice = [Die(),Die(),Die(),Die(),Die()]

    ones=upperSection(rolleddice,1)
    rolleddice = [Die(),Die(),Die(),Die(),Die()]
    twos=upperSection(rolleddice,2)
    rolleddice = [Die(),Die(),Die(),Die(),Die()]
    threes=upperSection(rolleddice,3)
    rolleddice = [Die(),Die(),Die(),Die(),Die()]
    fours=upperSection(rolleddice,4)
    rolleddice = [Die(),Die(),Die(),Die(),Die()]
    fives=upperSection(rolleddice,5)
    rolleddice = [Die(),Die(),Die(),Die(),Die()]
    sixes=upperSection(rolleddice,6)
    rolleddice = [Die(),Die(),Die(),Die(),Die()]
        
testprogram()
