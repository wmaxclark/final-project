# Study Module

def study():

    import validation as v
    import random as r
    
    userAnswer = ""
    correctAnswer = ""
    
    cardPrompts = []
    cardAnswers = []
    cardDifficulty = ""
    currentCard = 0
    deckLength = 0
    correct = False
    selecting = True

    # Allows the user type in what deck they want to study
    # TODO display a list of the decks that are already there
##    userFileRequest = v.getStringByLength("Select a deck to study: ", "Not a valid selection.", 3, 15)
##    deckPrompts = open("C:/Users/Home/Desktop/decks/" + userFileRequest + "prompts.txt", "r")

    
    while selecting == True:
        userFileRequest = v.getStringByLength("Select a deck to study: ", "Not a valid selection.", 3, 15)
        try:
            deckPrompts = open("C:/Users/Home/Desktop/decks/" + userFileRequest + "prompts.txt", "r")
            for i in deckPrompts:
                i = deckPrompts.readline()
                cardPrompts.append(i.rstrip("\n"))
            deckPrompts.close()
            
            deckAnswers = open("C:/Users/Home/Desktop/decks/" + userFileRequest + "answers.txt", "r")
            for j in deckAnswers:
                j = deckAnswers.readline()
                cardAnswers.append(j.rstrip("\n"))
            deckAnswers.close()
            selecting = False
        except:
            print("No deck for " + userFileRequest + ".") #TODO maybe add an option to create the deck
        


    # Loops through 10 times
    # TODO make this user selectable
    userCardNumber = v.getRangedInt("Please enter how many cards you would like to study. Twenty of a particular subject per day is recommended: ", "Needs to be a number between one and thirty, please. ", 1, 30) 
    for i in range(userCardNumber):

        # Picks a random card out of the deck that is acutally in the language that you're studying
        # TODO if possible, select cards weighted by difficulty and how many times you've got them wrong
        
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
