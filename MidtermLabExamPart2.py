#Set global variables for customers and square footages
customers = []
square_footages = []

#Function to find the average square footages
#Add each sqft to the total and divide by the length of square_footages array
def getAverage():
   total = 0
   for sqft in square_footages:
       total += sqft
   return total/len(square_footages)

#Get price for each sqft amount
#Check is done at input for any values outside the range of 1000 to 3000
#Price is checked in brackets by elif statements
def getPrice(sqft):
   if sqft >= 2501:
       return 3500
   elif sqft >= 2001:
       return 2000
   elif sqft >= 1501:
       return 1500
   elif sqft >= 1000:
       return 1200

#Create loop for 3 iterations
for x in range(3):
   #Enter customer name and append it to global variable
   customerName = input("Enter customer name: ")
   customers.append(customerName)
   
   #Start while loop to check for sqft input that falls outside of range
   validSqft = False
   while validSqft == False:
       squareFootage = int(input("Enter customer square footage: "))
       #If above input is in range, it is appended to the array and while condition is broken
       #Else, user is prompted to enter a valid square footage
       if squareFootage <= 3000 and squareFootage >=1000:
           square_footages.append(squareFootage)
           validSqft = True
       else:
           print("Square footage must be between 1000 and 3000")

#Print out customer name and rent based on square footage
for i in range(3):
   rent = getPrice(square_footages[i])
   print(f"Customer: {customers[i]}                 Rent: ${rent}")

#Print average square footage
averageSqft = getAverage()
print(f"Average square footage: {averageSqft}")

#Print max square footage in the array
maxSqft = max(square_footages)
print(f"Highest square footage: {maxSqft}")