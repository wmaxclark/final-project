# Study Module

def study():

    import validation as v
    import random as r
    import os
    # import question as q

    userFileRequest = ""
    
    userAnswer = ""
    correctAnswer = ""
    deckPrompts = ""
    deckAnswers = ""
    deckDifficulty = ""
    userCardNumber = ""
    

    availableDecks = []
    cardPrompts = []
    cardAnswers = []
    cardDifficulty = []
    currentCardList = []
    difficultyChanges = []
    deck = []
    card = []

    
    currentCard = 0
    currentDirection = 0
    deckLength = 0
    correct = False
    selecting = True

    
    # Creates an array of strings of the decks that are currently available
    availableDecks = str(os.listdir("C:/Users/Home/Desktop/decks/"))
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
                line.rstrip("\n")
                # Splits line into a list called a card
                card = line.split(",")
                # Creates an array of all the cards in the deck
                deck.append(card)
            fh.close()

            # When the arrays have all been completed, the user has finished selecting and the loop is closed
            selecting = False
            
        except:
            print("No deck for " + userFileRequest + ".") #TODO maybe add an option to create the deck from here

    
    
    print(deck)
    

    # User selects how many cards to study
    userCardNumber = v.getRangedInt("Please enter how many cards you would like to study: ", "Needs to be a number between one and thirty, please. ", 1, 30) # TODO short session medium session or long session instead of user selected
    userCardNumber = int(userCardNumber)
    for i in range(userCardNumber):

        # Randomly picks a direction, either giving prompts and recieving answers or vice versa
        currentDirection = r.randint(0, 1)

        

        # Repeats as long as you don't have the right answer
        # TODO keep track of how many you got right/wrong

        while correct == False:
        
            userAnswer = v.getStringByLength("What is the English translation of: "  + str(cards[currentCard]) + "\n", "That's not even a word.. ", 0, 30)
            
            # Checks direction
            # TODO tracked difficulty
            if currentDirection == 0:

                # Gets an answer from user
                userAnswer = v.getStringByLength("Prompt: "  + str(cardPrompts[currentCard]) + "\nAnswer: ", "That's not even a word.. \n", 0, 30) # TODO X word and Y word

                # Checks user answer against answer cards
                if userAnswer == str(cardAnswers[currentCard]):
                    print("Correct!\n")
                    g += 0
                    currentCard = currentCardList[g]
                    correct = True
                else:
                    print("Not quite, try again\n")

                


            elif currentDirection == 1:

                # Gets an answer from user
                userAnswer = v.getStringByLength("Answer: "  + str(cardAnswers[currentCard]) + "\nPrompt: ", "That's not even a word.. \n", 0, 30) # TODO X word Y word

                # Checks user answer against prompt cards as the direction is reversed
                if userAnswer == str(cardPrompts[currentCard]):
                    print("Correct!\n")
                    g += 0
                    currentCard = currentCardList[g]
                    correct = True
                else:
                    print("Not quite, try again\n")
        

    print("Good job studying! ")

study()
