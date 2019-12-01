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

    # Creates an array of strings of the decks that are currently available
    availableDecks = str(os.listdir()) # TODO THE FILE PATH CHANGES FOR EACH COMPUTER
    availableDecks = availableDecks.replace("'", "")
    availableDecks = availableDecks.replace("[", "")
    availableDecks = availableDecks.replace("]", "")
    availableDecks = availableDecks.replace(".csv", "")
    # TODO make this actually work

    # Allows the user type in what deck they want to study
    while selecting == True:

        # Displays a list of the decks that are already there
        print("Available decks: " + availableDecks.title() + ". \nWhich would you like to study?")

        # Gets valid name of a deck
        userFileRequest = v.getStringByLength("Type the name here: ", "Not a valid selection.", 3, 15)
        userFileRequest = userFileRequest.lower()
        userFileRequest = userFileRequest.replace(".", "")

        try:
            fh = open("spanish.csv", "r")
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

                # Creates an array of all the cards in the deck
                deck.append(easyCards + normalCards + hardCards)

            fh.close()

            # Closes loop
            selecting = False

        except:
            # TODO maybe add an option to create the deck from here
            print("No deck for " + userFileRequest + ".")

    # TEST
    # print(deck)



    easyCards, normalCards, hardCards = getDeck()

def study():
    
    # User selects how many cards to study
    # TODO short session medium session or long session instead of user selected
    userCardNumber = v.getRangedInt("Please enter how many cards you would like to study: ",
                                    "Needs to be a number between one and thirty, please. ", 1, 30)

    for i in range(userCardNumber):

        # Randomly picks a direction
        # Either giving prompts and recieving answers or vice versa

        print(userCardNumber)
        
        # Randomly picks a direction, either giving prompts and recieving answers or vice versa
        currentDirection = r.randint(0, 1)

        currentRange = r.randint(0, 100)
        if currentRange <= 10 and len(easyCards) > 0:
            currentCard = easyCards[r.randint(0, len(easyCards))]

        elif currentRange <= 50 and len(normalCards) > 0:
            currentCard = normalCards[r.randint(0, len(normalCards))]

        elif len(hardCards) > 0:
            currentCard = hardCards[r.randint(0, len(hardCards))]
 
        # Repeats as long as you don't have the right answer
        # TODO keep track of how many you got right/wrong
        # print(currentCard)
        correct = False
        while correct == False:
            

            # Checks direction
            # TODO tracked difficulty
            if currentDirection == 0:

                # Gets an answer from user
                # TODO X word and Y word
                userAnswer = v.getStringByLength(
                    "Prompt: " + str(currentCard[0]) + "\nAnswer: ",
                    "That's not even a word.. \n", 0, 30)

                # Checks user answer against answer cards
                if userAnswer == str(currentCard[1]):
                    print("Correct!\n")
                    correct = True
                else:
                    print("Not quite, try again\n")

            elif currentDirection == 1:

                # Gets an answer from user
                # TODO X word Y word
                userAnswer = v.getStringByLength(
                    "Answer: " + str(currentCard[1]) + "\nPrompt: ",
                    "That's not even a word.. \n", 0, 30)

                # Checks user answer against prompt cards as the direction is reversed
                if userAnswer == str(currentCard[0]):
                    print("Correct!\n")

                    correct = True
                else:
                    print("Not quite, try again\n")

    print("Good job studying! ")
