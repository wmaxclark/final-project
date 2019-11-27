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
    
    # Calls selectdeck to pick which deck to study
    userFileRequest = d.selectDeck()

    # Opens the deck to read mode
    fh = open(userFileRequest + ".csv", "r")

    # Loops while reading file
    for line in fh:
        
        # Strips carriage return
        line = line.rstrip("\n")
        
        # Splits line into a list called a card
        card = line.split(",")

        # Adds to easy card list if labeled easy
        if card[2] == "1":
            easyCards.append(card)
            
        # Adds to normal card list if labeled normal
        elif card[2] == "2":
            normalCards.append(card)
            
        # Adds to hard card list if labeled hard
        elif card[2] == "3":
            hardCards.append(card)

    fh.close()
    
    # Returns the card arrays
    return(easyCards, normalCards, hardCards)
    

def study():

    userAnswer = ""
    correctAnswer = ""    
    userCardNumber = ""
    picker = 0

    deck = []
    card = []
    currentCard = []
    easyCards = []
    normalCards = []
    hardCards = []
    
    currentCard = []
    currentDirection = 0
    deckLength = 0
    correct = False
    selecting = True


    easyCards, normalCards, hardCards = getDeck()
    
    # User selects how many cards to study
    userCardNumber = v.getRangedInt("Please enter how many cards you would like to study: ", "Needs to be a number between one and thirty, please. ", 1, 30) # TODO short session medium session or long session instead of user selected
    
    for i in range(userCardNumber):
        
               
        # Randomly picks a direction, either giving prompts and recieving answers or vice versa
        currentDirection = r.randint(0, 1)

        currentRange = r.randint(0, 100)
        if currentRange <= 10 and len(easyCards) > 0:
            picker = r.randint(0, len(easyCards) - 1)
            currentCard = easyCards[picker]
            
            
        elif currentRange <= 40 and len(normalCards) > 0:
            picker = r.randint(0, len(normalCards) - 1)
            currentCard = normalCards[picker]
            
            
        elif len(hardCards) > 0:
            picker = r.randint(0, len(hardCards) - 1)
            currentCard = hardCards[picker]
            
    
            
        # Repeats as long as you don't have the right answer
        # TODO keep track of how many you got right/wrong
        # print(currentCard)
        correct = False
        while correct == False:
            
            # Checks direction
            # TODO tracked difficulty
            if currentDirection == 0:

                # Gets an answer from user
                userAnswer = v.getStringByLength("Prompt: "  + str(currentCard[0]) + "\nAnswer: ", "That's not even a word.. \n", 0, 30) # TODO X word and Y word

                # Checks user answer against answer cards
                if userAnswer == str(currentCard[1]):
                    print("Correct!\n")
                    

                    
                    correct = True
                else:
                    print("Not quite, try again\n")
                
            elif currentDirection == 1:

                # Gets an answer from user
                userAnswer = v.getStringByLength("Answer: "  + str(currentCard[1]) + "\nPrompt: ", "That's not even a word.. \n", 0, 30) # TODO X word Y word

                # Checks user answer against prompt cards as the direction is reversed
                if userAnswer == str(currentCard[0]):
                    print("Correct!\n")
                    
                    correct = True
                else:
                    print("Not quite, try again\n")
        

    print("Good job studying! ")


