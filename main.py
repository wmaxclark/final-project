
def main():

    import validation as v
    import study as s
    # import deckManager as d
    quitProgram = False
    choice = 0
        
    while quitProgram == False:

        # Main Loop
        
        print("Welcome to Very Small Flashcard App.\nPlease select an option from the following: ")
        showMenu()
        choice = v.getRangedInt("Your Selection: ", "Enter an option 1-4", 1, 4)
        if choice == 1:
            s.study()

        # elif choice == 2:
            # d.addCards()
            #TODO

        # elif choice == 3:
            # d.addDeck()
            #TODO

        elif choice == 4:
            quitProgram = True
    
    print("\nBye!")

def showMenu():
     
    print("\t l. Study some flashcards from your deck.")
    print("\t 2. Add flashcards to an existing deck.") #TODO
    print("\t 3. Create a new deck of cards.") #TODO
    print("\t 4. Quit")

main()
