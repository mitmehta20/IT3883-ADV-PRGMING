#Start with Empty input and counter for 'while' loop
inputs = []
x = 0

#Function for appending input to the array
def addInputs():
    inputs.append(input("Insert Input: "))

#Function for concatinating all inputs and printing to console
def displayInputs():
    concatString = ""
    for inputItem in inputs:
        concatString += inputItem
    print(concatString)

#Function for clearing all inputs in the array
def clearInputs():
    inputs.clear()

#While loop that prints prompt and awaits response
while x == 0:
    print("Enter '1' to insert input")
    print("Enter '2' to display previous results")
    print("Enter '3' to clear inputs")
    print("Enter '4' to close program")

    #Records input choice
    choiceInput = input("Enter Choice: ")

    #Checks choice input and calls function accordingly
    #Case:4 - changes while loop variable to 1 to exit loop
    #Case: !1 && !2 && !3 && !4 - Prints invalid input
    if choiceInput == '1':
        addInputs()
    elif choiceInput == '2':
        displayInputs()
    elif choiceInput == '3':
        clearInputs()
    elif choiceInput == '4':
        x=1
    else:
        print("Invalid Input")

