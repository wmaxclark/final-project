def main():

    import validation as v

    userTestName = ""
    userPoints = ""
    userMaximum = ""
    userWeight = ""
    entering = True
    
    try:
        readFile = open("scores.csv", "r")
        readFile.close()
    except:
        readFile = open("scores.csv", "w")
        readFile.append("Test Name, Points, Maximum, Weight\n")
        readFile.close()

    
    while entering == True:
        choice = v.getStringByLength("Hit <enter> to enter scores, or type 'quit' to exit. ", "Invalid choice", 0, 4)
        
        if choice == "":
            userTestName = v.getStringByLength("Please input the name of the item: ", "Invalid name. ", 3, 30)
            userPoints = v.getValidInt("Please input the amount of points achieved: ", "Invalid points. ")
            userMaximum = v.getValidInt("Please input the maximum possible points: ", "Invalid maximum. ")
            userWeight = v.getValidInt("Please input the weight of the item: ", "Invalid weight. ")
            writeFile = open("scores.csv", "a")
            writeFile.write(userTestName + "," + str(userPoints) + "," + str(userMaximum) + "," + str(userWeight) + "\n")
            writeFile.close()
            
        elif choice == "quit":
            entering = False

main()
