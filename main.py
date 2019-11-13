
def main():

    import validation as v
    import study as s
    quitProgram = False
    choice = 0
        
    while quitProgram == False:

        # Main Loop
        
        print("Welcome to Very Small Flashcard App.\nPlease select an option from the following: ")
        showMenu()
        choice = v.getRangedInt("Your Selection: ", "Enter an option 1-4", 1, 4)
        if choice == 1:
            s.study()

        elif choice == 2:
            s.study()
            #TODO

        elif choice == 3:
            s.study()
            #TODO

        elif choice == 4:
            quitProgram = True
    
    print("\nBye!")

def showMenu():
     
    print("\t l. Study some flashcards from your deck.")
    print("\t 2. Some other crap") #TODO
    print("\t 3. Some other crap") #TODO
    print("\t 4. Quit")

main()
