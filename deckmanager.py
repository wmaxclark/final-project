import validation as v
import os
import study


def deckList():
    
    deckList = []
    
    # Creates an array of strings of the decks that are currently available
    availableDecks = os.listdir()

    # Iterates through the directory list
    for i in availableDecks:

        # Checks if the file ends in CSV
        if i[-4:] == ".csv":

            # If so, adds to deck list
            deckList.append(i)

    # Converts to string and processes to look nice
    deckList = str(deckList)
    deckList = deckList.replace("\n", "")
    deckList = deckList.replace("'", "")
    deckList = deckList.replace("[", "")
    deckList = deckList.replace("]", "")
    deckList = deckList.replace(".csv", "")
    deckList = deckList.title()

    return deckList

def selectDeck():

    selecting = True
    
    # Repeats as long as the user is selecting which deck
    while selecting == True:
        
        # Displays a list of the decks that are already there
        print("Available decks: " + deckList() + ". \n")
        
        # Gets valid name of a deck
        userFileRequest = v.getStringByLength("Type the name of the deck here to select: " , "Not a valid selection.", 3, 15)

        # Adjusts for varience in user input
        userFileRequest = userFileRequest.lower()
        userFileRequest = userFileRequest.replace(".", "")

        # Validates that this file exists
        try:
            fh = open(userFileRequest + ".csv", "r")
            fh.close()
            selecting = False
        except:
            print("No deck for " + userFileRequest + ".")

    return userFileRequest

def addCards():

    # Retrieves the current file from the user
    userFileRequest = selectDeck()
    adding = True

    # Loops so long as you are adding cards
    while adding == True:

        # Gets user prompt
        userPrompt = v.getStringByLength("Enter the prompt for a card, or hit <enter> to stop: ", "Invalid prompt", 0, 50)

        # If the input is empty, quits the function
        if userPrompt == "":
            adding = False

            
        else:
            # Gets answer from user
            userAnswer = v.getStringByLength("Enter the correct answer for " + userPrompt + ". ", "Invalid answer", 1, 50)

            # Writes the card to the csv
            with open(userFileRequest + ".csv", "a") as fh:
                fh = fh.write(userPrompt + "," + userAnswer + "\n")

def addDeck():

    newName = True
    listOfDecks = ""
    listOfDecks = deckList()
    
    # Gets the name of the new deck)
    while newName == True:
        userFileRequest = v.getStringByLength("Type the name of the new deck: " , "Not a valid deck name.", 3, 15)

        # Capitalizes input to match the existing decks
        userFileRequest = userFileRequest.title()

        # Checks if the input exists within the list of decks
        if listOfDecks.count(userFileRequest) > 0:
            print("That deck already exists. Please pick a different name. ")
        else:
            newName = False

    # Creates a new csv with the specified name
    userFileRequest = userFileRequest.lower()
    fh = open(userFileRequest + ".csv", "w")
    fh.close()


