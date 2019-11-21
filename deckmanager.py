def addCards():

    import validation as v

    # Allows the user type in what deck they want to study
    while selecting == True:
        
        # Displays a list of the decks that are already there
        print("Available decks: " + availableDecks.title() + ". \nWhich would you like to add cards to?")
        
        # Gets valid name of a deck
        userFileRequest = v.getStringByLength("Type the name here: " , "Not a valid selection.", 3, 15)
        
        
        try:
            fh = open("C:/Users/nh229u14/Desktop/decks/" + userFileRequest + ".csv", "r") # TODO make this filepath always work
            fh.close()
            selecting = False
            
        except:
            print("No deck for " + userFileRequest + ".") #TODO maybe add an option to create the deck from here

        
    while adding == True:
        
        userPrompt = v.getStringByLength("Enter the prompt for a card: ", "Invalid prompt", 1, 50)
        userAnswer = v.getStringByLength("Enter the correct answer for " + userPrompt + ".", "Invalid answer", 1, 50)
        userDifficulty = v.getRangedInt("Now rate the difficulty of this card 1-5, with 1 being the least difficult, 5 being the most difficult. ", "Invalid difficulty", 1, 5)
        fh = open("C:/Users/nh229u14/Desktop/decks/" + userFileRequest + ".csv", "r")
        fh.append(userPrompt + "," + userAnswer + "," + userDifficulty)
    
