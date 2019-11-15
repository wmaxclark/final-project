# Study Module

def study():

    import validation as v
    import random as r
    import os
    
    userAnswer = ""
    correctAnswer = ""

    availableDecks = []
    cardPrompts = []
    cardAnswers = []
    cardDifficulty = ""
    currentCard = 0
    deckLength = 0
    correct = False
    selecting = True

    
    # TODO display a list of the decks that are already there
    availableDecks = str(os.listdir("C:/Users/Home/Desktop/decks/"))
    #availableDecks = availableDecks.name()
    availableDecks = availableDecks.replace("'", "")
    availableDecks = availableDecks.replace("[", "")
    availableDecks = availableDecks.replace("]", "")

    # Allows the user type in what deck they want to study
    
    while selecting == True:
        print("Please select a deck to study from the following: " + availableDecks)
        userFileRequest = v.getStringByLength("Type the name here: " , "Not a valid selection.", 3, 15) # Gets valid name of a deck
        try:
            deckPrompts = open("C:/Users/Home/Desktop/decks/" + userFileRequest + "/" + userFileRequest + "prompts.txt", "r") # Writes prompts to an array 
            for i in deckPrompts:
                i = deckPrompts.readline()
                cardPrompts.append(i.rstrip("\n"))
            deckPrompts.close()
            
            deckAnswers = open("C:/Users/Home/Desktop/decks/" + userFileRequest + "/" + userFileRequest + "answers.txt", "r") # Writes answers to an array
            for j in deckAnswers:
                j = deckAnswers.readline()
                cardAnswers.append(j.rstrip("\n"))
            deckAnswers.close()
            selecting = False
        except:
            print("No deck for " + userFileRequest + ".") #TODO maybe add an option to create the deck from here
        


    # Loops through 10 times
    # TODO make this user selectable
    userCardNumber = v.getRangedInt("Please enter how many cards you would like to study. Twenty of a particular subject per day is recommended: ", "Needs to be a number between one and thirty, please. ", 1, 30) 
    for i in range(userCardNumber):

        # Picks a random card out of the deck that is acutally in the language that you're studying
        # TODO if possible, select cards weighted by difficulty and how many times you've got them wrong
        # TODO if possible, pick between prompts and answers randomly
        currentCard = r.randrange(0, len(cardPrompts) - 1)

        # Repeats as long as you don't have the right answer
        # TODO user feedback and tracked difficulty
        correct = False
        while correct == False:
            userAnswer = v.getStringByLength("What is the English translation of: "  + str(cardPrompts[currentCard]) + "\n", "That's not even a word.. \n", 0, 30)
            
            if userAnswer == str(cardAnswers[currentCard]):
                correct = True
                print("Correct!\n")
            else:
                print("Not quite, try again\n")
        

    print("Good job studying! ")
