

import copy
import sys
import time

# number of cards are stored in N
N = 0 

# set_count stores the count of maximum possible Sets of 3 cards in the form of input
set_count = 0

# cardlist stores the objects of cards
# the id of an object is its index in cardlist
cardList = []

# each case is represented as a dictionary
# a, s, h belongs to case 1
# A, S, H belongs to case 2
# @, $, # belongs to case 3
case = {'a' : 1, 's' : 1, 'h' : 1, 'A' : 2, 'S' : 2, 'H' : 2, '@' : 3, '$' : 3, '#' : 3}

# each type is represented as a dictionary
# a, A, @ are of same type
# s, S, $ are of same type
# h, H, # are of same type
type = {'a' : 1, 'A' : 1, '@' : 1, 's' : 2, 'S' : 2, '$' : 2, 'h' : 3, 'H' : 3, '#' : 3}


# sets stores all the possible sets
# It is a map from set id which is an integer to a list of object ID
sets = {}

# max_counts will count the maximum number of disjoint SETs
max_count = 0

# the maxIndSet will store the IDs of sets which are maximally independent
maxIndSet = []

# Creating a data structure to represent a card.
# It will be containing attributes such as color, symbol, shadding and number 
class Card:
    color = 0
    symbol = ''
    shading = ''
    number = 0

   # will be using a constructor to initialize all the card attributes
    def __init__(self, col, shade):
        self.color = col
        self.shading = shade
        self.symbol = shade[0]
        self.number = len(shade)


# This function will be returning 1 if all the cards have either same color or all different color, else it will be returning 0 
# This fucntion will be taking three card objects as arguments 

def checkColor(card1, card2, card3):
    col1 = card1.color
    col2 = card2.color
    col3 = card3.color
    if(col1 == col2 and col2 == col3):
        return 1

    if(col1 != col2 and col2 != col3 and col3 != col1):
        return 1

    return 0

# This function will be returning 1 if all the cards have either same symbol or all of different symbol, else it will be returning 0
# This fucntion will be taking three card objects as arguments 

def checkSymbol(card1, card2, card3):
    sym1 = card1.symbol
    sym2 = card2.symbol
    sym3 = card3.symbol

    if(sym1 == sym2 and sym2 == sym3):
        return 1

    if(sym1 != sym2 and sym2 != sym3 and sym3 != sym1):
        return 1

    return 0

# This function will be returning 1 if all the cards have either same number of symbols or all of different number of symbols, else it will returning 0
# This fucntion will be taking three card objects as arguments 

def checkNumber(card1, card2, card3):

    len1 = card1.number
    len2 = card2.number
    len3 = card3.number

    if(len1 == len2 and len2 == len3):
        return 1

    if(len1 != len2 and len2 != len3 and len3 != len1):
        return 1

    return 0

# This function will be returning 1 if all the cards have symbols either of same case or all of different case, else it will returning 0
# This fucntion will be taking three card objects as arguments 

def checkCase(card1, card2, card3):
    global case
    case1 = case[card1.symbol]
    case2 = case[card2.symbol]
    case3 = case[card3.symbol]

    if(case1 == case2 and case2 == case3):
        return 1

    if(case1 != case2 and case2 != case3 and case3 != case1):
        return 1

    return 0


# This function will be returning 1 if all the cards have symbols either of same type or all of different type, else it will be returning 0
# This fucntion will be taking three card objects as arguments 

def checkType(card1, card2, card3):
    global type
    type1 = type[card1.symbol]
    type2 = type[card2.symbol]
    type3 = type[card3.symbol]

    if(type1 == type2 and type2 == type3):
        return 1

    if(type1 != type2 and type2 != type3 and type3 != type1):
        return 1

    return 0

# The utility function will be checking if card IDs i, j, k will form a Set or not
# The function returns 1 if they form a set or else it will return 0
def isSET(i, j, k):
    global cardList
    card1 = cardList[i]
    card2 = cardList[j]
    card3 = cardList[k]

    setCond = 0

    # condition to check if all the cards have either same color or all of different color
    setCond = checkColor(card1, card2, card3)

    # condition to check if all the cards have either same symbol or all of different symbol
    if setCond == 1:
        setCond = checkSymbol(card1, card2, card3)

    # condition to check if all the cards have either same number of symbols or all of different number of symbols
    if setCond == 1:
        setCond = checkNumber(card1, card2, card3)

    # condition to check if all the cards have symbols either same case or all of different case
    if setCond == 1:
        setCond = checkCase(card1, card2, card3)

    # condition to check if all the cards have symbols either of same type or all of different type
    if setCond == 1:
        setCond = checkType(card1, card2, card3)

    return setCond


'''

Algorithm:
Traverse the sets list from left to right. There are two cases:
Include the current set or Exclude the current set.
In case of exclude, setInd is incremented and and function is recursively called.
In case of include, first check if the current has cards which are different from already picked one's.
    If YES, then include, else doesn't include.
    If included:
    add cards in the current set to cardsPicked list. add the current set to setsPicked List
    count the number of independent sets formed and update maxIndSet and max_count accordingly.
    Increment setInd, count and recursively call the same function.
'''

# This function will be finding the maximum number of disjoint sets
# setInd is used to point a set in sets dictionary
# setsPicked is a list containing independent sets picked so far.
# cardsPicked is a list containing union of cards of all the sets picked so far.

def maxDisjointSets(setInd, cardsPicked, setsPicked, count):

    global max_count, maxIndSet, sets, set_count
    if setInd >= set_count:
        return

    if count >= max_count:
        max_count = count
        maxIndSet = setsPicked

    #excluding part
    maxDisjointSets(copy.deepcopy(setInd + 1), copy.deepcopy(cardsPicked), copy.deepcopy(setsPicked), copy.deepcopy(count))

    #including part
    if((sets[setInd][0] not in cardsPicked) and (sets[setInd][1] not in cardsPicked) and (sets[setInd][2] not in cardsPicked)):
        cardsPicked.append(sets[setInd][0])
        cardsPicked.append(sets[setInd][1])
        cardsPicked.append(sets[setInd][2])

        count = count + 1
        setsPicked.append(setInd)

        if count >= max_count:
            max_count = count
            maxIndSet = setsPicked

        maxDisjointSets(copy.deepcopy(setInd+1), copy.deepcopy(cardsPicked), copy.deepcopy(setsPicked), copy.deepcopy(count))


    return

# This function will print the cards in the set
# i, j, k are the ids of cards in the set
def printSet(i, j, k):
    global cardList
    print("============================================================\n")
    print(cardList[i].color, "  ", cardList[i].shading, "  ", cardList[i].symbol, "  ", cardList[i].number, "\n")
    print (cardList[j].color, "  ", cardList[j].shading, "  ", cardList[j].symbol, "  ", cardList[j].number, "\n")
    print (cardList[k].color, "  ", cardList[k].shading, "  ", cardList[k].symbol, "  ", cardList[k].number, "\n")
    print ("============================================================\n")
    return


# The utility function will be creating all the possible Sets
# This function will return the count of maximum possibles Sets
def possibleSets():
    count = 0
    global sets, set_count
    for i in range(0, N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if(isSET(i, j, k)):
                    #printSet(i, j, k)
                    sets[count] = []
                    sets[count].append(i)
                    sets[count].append(j)
                    sets[count].append(k)
                    count = count + 1

    set_count = count
    return count

# the program execution begins from here

if __name__ == '__main__':
    print(len(sys.argv), sys.argv)
    
    file = open('Test.txt', 'r')
    Lines = file.readlines()
    testCases = {}
    currentTestCase = 0
    for line in Lines:
        
        if line.strip().isnumeric():
            
            testCases[currentTestCase] = [int(line)]
        else:
            if line == "\n":
                currentTestCase += 1
                continue
            testCases[currentTestCase].append(line)

    for key in testCases.keys():
        t0 = time.time()

        N = testCases[key][0]
        cards = testCases[key][1::] 
        cardList = []

        for card in cards:
            attr = card.split()
            obj = Card(attr[0], attr[1])
            cardList.append(obj)

    
        # prints Maximum possible sets of size 3.
        print(possibleSets())

        # call to compute maximum number of disjoint SETs
        maxDisjointSets(0, [], [], 0)

        # prints maximum number of disjoint SETs
        print(max_count)


        # prints cards in each set from maximum number of disjoint SETs
        for i in range(0, max_count):
                print("\n")
                card1 = cardList[sets[maxIndSet[i]][0]]
                card2 = cardList[sets[maxIndSet[i]][1]]
                card3 = cardList[sets[maxIndSet[i]][2]]

                print(card1.color, " ", card1.shading)
                print(card2.color, " ", card2.shading)
                print(card3.color, " ", card3.shading)
        print(time.time() - t0)
        # time taken


