# Study Module
import validation as v
import random as r
import deckmanager as d
import os
import csv

def getDeck():

    easyCards = []
    normalCards = []
    hardCards = []
    deck = []
    listOfLines = []
    
    # Loops while reading file
    readFile = open(d.selectDeck() + ".csv", "r")
    for line in readFile:

        #line = readFile.readline()
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

    # Close the file
    readFile.close()
    
    # Returns the card arrays
    return(easyCards, normalCards, hardCards)


def study():

    attempts = 0
    deck = []
    picker = 0
    currentDifficulty = 0
    currentCard = []
    
    # Gets the deck of cards from the getDeck function
    easyCards, normalCards, hardCards = getDeck()

    print(easyCards, normalCards, hardCards)
    # User selects how many cards to study
    # TODO short session medium session or long session instead of user selected
    userCardNumber = v.getRangedInt("Please enter how many cards you would like to study: ",
                                    "Needs to be a number between one and thirty, please. ", 1, 30)

    # Loops as many times as specified by input
    for i in range(userCardNumber):
        
        # Randomly picks a direction, either giving prompts and recieving answers or vice versa
        currentDirection = r.randint(0, 1)

        # Picks a number which will be used to weight how often each type of card will be picked
        currentRange = r.randint(0, 100)
        try:
            # If the range is for easy and easyCards isn't empty
            if currentRange <= 10 and len(easyCards) != 0:
                # Picks a random number from the cards
                picker = r.randint(0, len(easyCards) - 1)
                currentDifficulty = 1
                currentCard = easyCards[picker]

            # If the range is for normal and normalCards isn't empty
            elif currentRange <= 50 and len(normalCards) != 0:
                # Picks a random number from the cards
                picker = r.randint(0, len(normalCards) - 1)
                currentDifficulty = 2
                currentCard = normalCards[picker]

            # If the range is for hard and hardCards isn't empty
            elif len(hardCards) != 0:
                # Picks a random number from the cards
                picker = r.randint(0, len(hardCards) - 1)
                currentDifficulty = 3
                currentCard = hardCards[picker]
        except:
            break
            print("No cards")

        # Repeats as long as you don't have the right answer
        correct = False

        # Loops as long as the user hasn't answered correctly
        while correct == False:

            # Resets attempts tracker
            attempts = 0
            
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
                    # Adds to attempts
                    attempts += 1
                    # Hint displays when attempts is over 3
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
                    # Adds to attempts
                    attempts += 1
                    # Hint displays when attempts is over 3
                    if attempts > 3:
                        print("\nHint: " + currentCard[0][:3])

            # Checks the number of attempts
            if attempts == 0:
                # Checks how difficult the card was
                if currentDifficulty == 1:
                    # Replaces the value according to the attempts
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

    # Opens file to write and closes when finished
    with open("../decks/spanish.csv", "w", newline='') as outFile:
        # Creates object to 
        writer = csv.writer(outFile)
        for card in easyCards:
            writer.writerow(card)
        for card in normalCards:
            writer.writerow(card)
        for card in hardCards:
            writer.writerow(card)
        
    print("Good job studying! ")
