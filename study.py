# Study Module
import validation as v
import random as r
import deckmanager as d
import os


def getDeck():

    easyCards = []
    normalCards = []
    hardCards = []
    deck = []
    listOfLines = []
    
    
    # Calls selectdeck to pick which deck to study
    userFileRequest = d.selectDeck()

    # Opens the deck to read mode
    readFile = open("spanish.csv", "r") # FIX THIS BUT I HAVE NO IDEA HOW THIS DOESN"T WORK
        
    listOfLines = readFile.readlines()
    
        
    # Loops while reading file
    for line in listOfLines:
        
        # Strips carriage return
        line = line.rstrip("\n")
                
        # Splits line into a list called a card
        card = line.split(",")
        
        # Adds to easy card list if labeled easy
        if "1" in card:
            easyCards.append(card)
            
        # Adds to normal card list if labeled normal
        elif "2" in card:
            normalCards.append(card)
            
        # Adds to hard card list if labeled hard
        elif "3" in card:
            hardCards.append(card)

    
    print(easyCards, normalCards, hardCards)
    
    # Returns the card arrays
    return(easyCards, normalCards, hardCards, userFileRequest)

def study():

    attempts = 0
    deck = []
    picker = 0
    currentDifficulty = 0
    currentCard = []
    
    # Gets the deck of cards from the getDeck function
    easyCards, normalCards, hardCards, userFileRequest = getDeck()
         
  
    
    # User selects how many cards to study
    # TODO short session medium session or long session instead of user selected
    userCardNumber = v.getRangedInt("Please enter how many cards you would like to study: ",
                                    "Needs to be a number between one and thirty, please. ", 1, 30)

    for i in range(userCardNumber):
        
        # Randomly picks a direction, either giving prompts and recieving answers or vice versa
        currentDirection = r.randint(0, 1)

        currentRange = r.randint(0, 100)
        if currentRange <= 10 and len(easyCards) > 0:
            picker = r.randint(0, len(easyCards) - 1)
            currentDifficulty = 1
            currentCard = easyCards[picker]

        elif currentRange <= 50 and len(normalCards) > 0:
            picker = r.randint(0, len(normalCards) - 1)
            currentDifficulty = 2
            currentCard = normalCards[picker]

        elif len(hardCards) > 0:
            picker = r.randint(0, len(hardCards) - 1)
            currentDifficulty = 3
            currentCard = hardCards[picker]


        
        # Repeats as long as you don't have the right answer
        correct = False
        while correct == False:
            

            # Checks direction
            if currentDirection == 0:

                # Gets an answer from user
                userAnswer = v.getStringByLength(
                    "Prompt: " + str(currentCard[0]) + "\nAnswer: ",
                    "That's not even a word.. \n", 0, 30)

                # Checks user answer against answer cards
                if userAnswer == str(currentCard[1]):
                    print("Correct!\n")
                    correct = True
                else:
                    print("Not quite, try again\n")
                    attempts += 1
                    if attempts > 3:
                        print("\nHint: " + currentCard[1][:3])

            elif currentDirection == 1:

                # Gets an answer from user
                userAnswer = v.getStringByLength(
                    "Answer: " + str(currentCard[1]) + "\nPrompt: ",
                    "That's not even a word.. \n", 0, 30)

                # Checks user answer against prompt cards as the direction is reversed
                if userAnswer == str(currentCard[0]):
                    print("Correct!\n")

                    correct = True
                else:
                    print("Not quite, try again\n")
                    attempts += 1
                    if attempts > 3:
                        print("\nHint: " + currentCard[0][:3])

    if attempts == 0:
        if currentDifficulty == 1:
            easyCards[picker][2] = "1"
        elif currentDifficulty == 2:
            normalCards[picker][2] = "1"
        elif currentDifficulty == 3:
            hardCards[picker][2] = "1"
    elif attempts <= 2:
        if currentDifficulty == 1:
            easyCards[picker][2] = "2"
        elif currentDifficulty == 2:
            normalCards[picker][2] = "2"
        elif currentDifficulty == 3:
            hardCards[picker][2] = "2"
    else:
        if currentDifficulty == 1:
            easyCards[picker][2] = "3"
        elif currentDifficulty == 2:
            normalCards[picker][2] = "3"
        elif currentDifficulty == 3:
            hardCards[picker][2] = "3"
        
        
    
    outfile = open("spanish.csv", "w")
    outfile.close()
    outfile = open("spanish.csv", "a")

    for card in easyCards:
        for i in range(2):
            card.append(easyCards(i))
        card.append("\n")
        outfile.write(str(card))
    outfile.writelines(str(easyCards))
    outfile.writelines(str(normalCards))
    outfile.writelines(str(hardCards))
        
            

    print("Good job studying! ")
    
study()
