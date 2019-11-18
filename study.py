# Study Module

def study():

    import validation as v
    import random as r
    import os

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
    
    currentCard = 0
    currentDirection = 0
    correct = False
    selecting = True

    
    # Creates an array of strings of the decks that are currently available
    availableDecks = str(os.listdir("C:/Users/Home/Desktop/decks/"))
    availableDecks = availableDecks.replace("'", "")
    availableDecks = availableDecks.replace("[", "")
    availableDecks = availableDecks.replace("]", "")

    # Allows the user type in what deck they want to study
    while selecting == True:
        
        # Displays a list of the decks that are already there
        print("Available decks: " + availableDecks.title() + ". \nWhich would you like to study?")
        
        # Gets valid name of a deck
        userFileRequest = v.getStringByLength("Type the name here: " , "Not a valid selection.", 3, 15) 
        
        try:
            # Writes prompts to an array
            deckPrompts = open("C:/Users/Home/Desktop/decks/" + userFileRequest + "/" + userFileRequest + "prompts.txt", "r")  
            for t in deckPrompts:
                t = deckPrompts.readline()
                cardPrompts.append(t.rstrip("\n"))
            deckPrompts.close()
            
            # Writes answers to an array
            deckAnswers = open("C:/Users/Home/Desktop/decks/" + userFileRequest + "/" + userFileRequest + "answers.txt", "r") 
            for j in deckAnswers:
                j = deckAnswers.readline()
                cardAnswers.append(j.rstrip("\n"))
            deckAnswers.close()
            
            # Writes difficulties to an array
            deckDifficulty = open("C:/Users/Home/Desktop/decks/" + userFileRequest + "/" + userFileRequest + "difficulty.txt", "r") 
            for f in deckDifficulty:
                f = deckDifficulty.readline()
                cardDifficulty.append(f.rstrip("\n"))
            deckDifficulty.close()

            # When the arrays have all been completed, the user has finished selecting and the loop is closed
            selecting = False
            
        except:
            print("No deck for " + userFileRequest + ".") #TODO maybe add an option to create the deck from here
        


    # User selects how many cards to study
    userCardNumber = v.getRangedInt("Please enter how many cards you would like to study: ", "Needs to be a number between one and thirty, please. ", 1, 30) # TODO short session medium session or long session instead of user selected
    userCardNumber = int(userCardNumber)
    for i in range(userCardNumber):

        # Randomly picks a direction, either giving prompts and recieving answers or vice versa
        currentDirection = r.randint(0, 1)

        # Picks a random card out of the deck weighted by the difficulty
        currentCardList = r.choices(cardPrompts, weights=cardDifficulty, cum_weights=None, k=userCardNumber)
        g = 0
        currentCard = currentCardList[g]

        
        

        
        correct = False

        # Repeats as long as you don't have the right answer
        while correct == False:
        
            
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
