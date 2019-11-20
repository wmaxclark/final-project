#integers
def getValidInt(message, errorMessage):
    #storage
    isValidInt = False
    testInput = ""
    intToReturn = 0

    #input
    while isValidInt == False:
        try:
            testInput = input(message + " ")

            #processing
            intToReturn = int(testInput)
            isValidInt = True
        except:
            print(errorMessage)
            input("Press <enter> to try again.")

    #output
    
    return intToReturn

def getRangedInt(message, errorMessage, lowerbound, upperbound):
    #storage
    isValidInt = False
    testInput = ""
    intToReturn = 0

    #input
    while isValidInt == False:
        try:
            testInput = input(message + " ")

            #processing
            intToReturn = int(testInput)
            if(intToReturn < lowerbound or intToReturn > upperbound):
                raise ValueError()
            isValidInt = True
        except:
            print(errorMessage)
            input("Press <enter> to try again.")

    #output
    
    return intToReturn

#floats
def getValidFloat(message, errorMessage):
    #storage
    isValidFloat = False
    testInput = ""
    floatToReturn = 0.0

    #input
    while isValidFloat == False:
        try:
            testInput = input(message + " ")

            #processing
            floatToReturn = float(testInput)
            isValidFloat = True
        except:
            print(errorMessage)
            input("Press <enter> to try again.")

    #output
    
    return floatToReturn

def getRangedFloat(message, errorMessage, lowerbound, upperbound):
    #storage
    isValidFloat = False
    testInput = ""
    floatToReturn = 0.0

    #input
    while isValidFloat == False:
        try:
            testInput = input(message)

            #processing
            floatToReturn = float(testInput)
            if(floatToReturn < lowerbound or floatToReturn > upperbound):
                raise ValueError()
            isValidFloat = True
        except:
            print(errorMessage)
            input("Press <enter> to try again.")

    #output
    
    return floatToReturn

#strings
def  getStringByLength(message, errorMessage, minCharacters, maxCharacters):
    #storage
    isValidString = False
    testInput = ""

    #input
    while isValidString == False:
        try:
            testInput = input(message)
            if(len(testInput) < minCharacters or len(testInput) > maxCharacters):
                 raise ValueError()
            isValidString = True
        except:
            print(errorMessage)
            input("Press <enter> to try again.")
    #output
    return testInput
