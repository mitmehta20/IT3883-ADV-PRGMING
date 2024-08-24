inputs = []
x = 0

def addInputs():
    inputs.append(input("Insert Input: "))

def displayInputs():
    concatString = ""
    for inputItem in inputs:
        concatString += inputItem
    print(concatString)

def clearInputs():
    inputs.clear()

while x == 0:
    print("Enter '1' to insert input")
    print("Enter '2' to display previous results")
    print("Enter '3' to clear inputs")
    print("Enter '4' to close program")

    choiceInput = input("Enter Choice: ")

    if choiceInput == '1':
        addInputs()
    elif choiceInput == '2':
        displayInputs()
    elif choiceInput == '3':
        clearInputs()
    elif choiceInput == '4':
        x=1

