# final-project
Final project for CIS 121

This program allows a user to study text-based flashcards, create new decks of cards, and add new cards to existing decks. The program takes input from users and CSV files. 

The main function is the study function. This calls a function called getDeck(). This function then calls the selectDeck() function in the deckmanager module.  The user is asked to select the deck to study, and their selection is turned into a list called deck. The program then prompts users for the number of cards that they would like to study. Then, it checks to validate that there are cards in the deck selected. 

If there are cards within the deck, the program will loop as many times as the user has selected. It uses two randint() functions to generate a direction and to pick a random card from the list of cards available. 

The addCards() function also relies on the selectDeck() function, and the addDeck() function simply creates a file with the name specified. 

All functions rely on the deckList() function, which returns a list of the current decks.
