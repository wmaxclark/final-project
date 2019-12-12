# Study Module
import validation as v
import random as r
import deckmanager as d
import os
import csv

def getDeck():

    deck = []
    userFileRequest = d.selectDeck()
    
    # Loops while reading file
    readFile = open("C:/Users/Home/Desktop/final_project/decks/" + userFileRequest + ".csv", "r")
    for line in readFile:

        #line = readFile.readline()
        # Strips carriage return
        line = line.rstrip("\n")
        line = line.rstrip("\r")
                
        # Splits line into a list called a card
        card = line.split(",")

        # Appends card to deck
        deck.append(card)

    # Close the file
    readFile.close()
    
    # Returns the card arrays
    return(deck, userFileRequest)


def study():

    attempts = 0
    deck = []
    card = []
    picker = 0
    currentCard = []
    outfile = ''
    userFileRequest = ""
    
    # Gets the deck of cards from the getDeck function
    deck, userFileRequest = getDeck()

    # User selects how many cards to study
    userCardNumber = v.getRangedInt("Please enter how many cards you would like to study: ",
                                    "Needs to be a number between one and thirty, please. ", 1, 30)
    # Checks if the deck is valid
    if len(deck) == 0:
        print("No cards in deck.")
    else:
        # Loops as many times as specified by input
        for i in range(userCardNumber):
            
            # Randomly picks a direction, either giving prompts and recieving answers or vice versa
            currentDirection = r.randint(0, 1)
            
            # Picks a random number from the cards
            picker = r.randint(0, len(deck) - 1)

            # Sets current card to random card
            currentCard = deck[picker]

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
                        attempts += 1

                        # Hint displays when attempts is over 3
                        if attempts > 3:
                            print("\nHint: " + currentCard[0][:3])
            

        # Opens file to write and closes when finished
        outfile = open("C:/Users/Home/Desktop/final_project/decks/" + userFileRequest + ".csv", "w")

        # Loops for cards in deck 
        for card in deck:

            # Processes cards
            card = str(card)
            card = card.replace("'", "")
            card = card.replace("[", "")
            card = card.replace("]", "")
            card = card.replace(" ", "")
            outfile.write(card + "\n")
        
        # Completion notice
        print("Good job studying! \n")
