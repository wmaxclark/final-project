# Study Module

def study():

    import validation as v
    import random as r
    
    userAnswer = ""
    correctAnswer = ""
    cards = []
    card = ""
    currentCard = 0
    deckLength = 0
    correct = False

    # TODO make this actually work
    # TODO allow users to actually select which deck they are going to practice from
    # userFileRequest = v.getStringByLength("Select a deck to study: ", "Not a valid selection.", 3, 15)

    # TODO validate that this file exists
    # deck = open("C:/Users/Home/Desktop/decks/spanish.txt", "r")

    try:
        deck = open("C:/Users/Home/Desktop/decks/spanish.txt", "r")
        # deck = deckFile.readlines() 
        for card in deck:
            card = deck.readline()
            cards.append(card.rstrip("\n"))
        deck.close()
    except:
        print("No saved data. ")
        salesFile = open("sales.txt", "w")
        salesFile.close()

    
    # Creates an array of all the cards in the deck
    
##    for card in deck:
##        card = deck.readline()
##        cards.append(card.rstrip("\n"))
##    deck.close()

    # Loops through 10 times
    # TODO make this user selectable
    deckLength = len(cards)
    for i in range(10):

        # Picks a random card out of the deck that is acutally in the language that you're studying
        # TODO if possible, select cards weighted by difficulty and how many times you've got them wrong
        
        currentCard = r.randrange(0, len(cards) - 2, 2)

        # Repeats as long as you don't have the right answer
        # TODO user feedback and tracked difficulty
        correct = False
        while correct == False:
            userAnswer = v.getStringByLength("What is the English translation of: "  + str(cards[currentCard]) + "\n", "That's not even a word.. ", 0, 30)
            
            if userAnswer == str(cards[currentCard + 1]):
                correct = True
                print("Correct!")
            else:
                print("Not quite, try again")
        

    print("Good job studying! ")
