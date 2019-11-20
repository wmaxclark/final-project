# Study Module

def study():

    import validation as v
    import random as r
    # import question as q
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
    deck = open("spanish.txt", "r")

    
    # Creates an array of all the cards in the deck
    
    for card in deck:
        card = deck.readline()
        cards.append(card.rstrip("\n"))
    deck.close()

    # Loops through 10 times
    for i in range(10):

        # Picks a random card out of the deck that is acutally in the language that you're studying
        # TODO if possible, select cards weighted by difficulty and how many times you've got them wrong
        deckLength = len(cards)
        currentCard = r.randrange(0, deckLength - 1, 2)

        # Repeats as long as you don't have the right answer
        # TODO keep track of how many you got right/wrong
        # TODO get input on how hard it was
        correct = False
        while correct == False:
            userAnswer = v.getStringByLength("What is the English translation of: "  + str(cards[currentCard]) + "\n", "That's not even a word.. ", 0, 30)
            
            if userAnswer == str(cards[currentCard + 1]):
                correct = True
                print("Correct!")
            else:
                print("Not quite, try again")
        

    print("Good job studying! ")
