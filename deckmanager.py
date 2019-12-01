import validation as v
import os

def selectDeck():
   
    # Creates an array of strings of the decks that are currently available
    availableDecks = str(os.listdir()) # TODO THE FILE PATH CHANGES FOR EACH COMPUTER
    availableDecks = availableDecks.replace("'", "")
    availableDecks = availableDecks.replace("[", "")
    availableDecks = availableDecks.replace("]", "")
    availableDecks = availableDecks.replace(".csv", "")
    # TODO make this actually work
    selecting = True
    # Allows the user type in what deck they want to study
    while selecting == True:
        
        # Displays a list of the decks that are already there
        print("Available decks: " + availableDecks.title() + ". \n")
        
        # Gets valid name of a deck
        userFileRequest = v.getStringByLength("Type the name of the deck here to select: " , "Not a valid selection.", 3, 15)
        userFileRequest = userFileRequest.lower()
        userFileRequest = userFileRequest.replace(".", "")
        
        try:
            fh = open(userFileRequest + ".csv", "r")
            selecting = False
        except:
            print("No deck for " + userFileRequest + ".") #TODO maybe add an option to create the deck from here

        return userFileRequest

def addCards():

    userFileRequest = selectDeck()
    adding = True
    while adding == True:
            
        userPrompt = v.getStringByLength("Enter the prompt for a card, or hit <enter> to stop: ", "Invalid prompt", 0, 50)
        if userPrompt == "":
            adding = False
        else:
            userAnswer = v.getStringByLength("Enter the correct answer for " + userPrompt + ". ", "Invalid answer", 1, 50)
            with open("C:/Users/nh229u14/Desktop/decks/" + userFileRequest + ".csv", "a") as fh:
                fh = fh.write(userPrompt + "," + userAnswer + ",3\n")


