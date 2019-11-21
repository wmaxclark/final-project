# Study Module

def study():

    import validation as v
    import random as r
    import os
    # import question as q

    userFileRequest = ""
    
    userAnswer = ""
    correctAnswer = ""
    
    userCardNumber = ""
    

    availableDecks = []
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
        userFileRequest = v.getStringByLength("Type the name here: " , "Not a valid selection.", 3, 15)
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

            # When the arrays have all been completed, the user has finished selecting and the loop is closed
            selecting = False
            
        except:
            print("No deck for " + userFileRequest + ".") #TODO maybe add an option to create the deck from here

    
    # TEST
    # print(deck)
    

    # User selects how many cards to study
    userCardNumber = v.getRangedInt("Please enter how many cards you would like to study: ", "Needs to be a number between one and thirty, please. ", 1, 30) # TODO short session medium session or long session instead of user selected
    
    for i in range(userCardNumber):
        print(userCardNumber)
        
        # Randomly picks a direction, either giving prompts and recieving answers or vice versa
        currentDirection = r.randint(0, 1)

        currentRange = r.randint(0, 100)
        if currentRange <= 10 and len(easyCards) > 0:
            currentCard = easyCards[r.randint(0, len(easyCards) - 1)]
            
        elif currentRange <= 50 and len(normalCards) > 0:
            currentCard = normalCards[r.randint(0, len(normalCards) - 1)]
            
        elif len(hardCards) > 0:
            currentCard = hardCards[r.randint(0, len(hardCards) - 1)]
    
            
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

study()
