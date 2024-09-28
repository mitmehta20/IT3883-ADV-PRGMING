#Initialization of nested array for all student information
studentInfos = []

#function to return letter grade for inputed grade
def convertToLetterGrade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
    
#function for finding the average of a list of grades passed in
def getAverage(grades):
    #Total starts at 0 and increments by the next amount
    #The sum is then divided by the length of the array
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades)

#function to create student info
def createStudentInfo():
    #Loop that iterates 6 times to collect student info
    #Each student will have their own array element that will include their name, grades, and letter grades
    for studentCount in range(6):
        studentInfo = []
        #get student name and insert into empty student info
        name = input("Enter Student Name: ")
        studentInfo.append(name)
        letterGrades = []
        grades = []
        #Loop through and collect 6 grades for each student
        #Each grade is passed through the letter converter and store respectively in the arrays on lines 35 & 36
        for gradeCount in range(6):
            grade = float(input(f"Enter Grade for Test {gradeCount + 1} (Number between 0-100): "))
            grades.append(grade)
            letterGrade = convertToLetterGrade(grade)
            letterGrades.append(letterGrade)
        
        #Add grades, letter grades, and average to the student info array
        #Then append studentInfo to the global array
        studentInfo.append(grades)
        studentInfo.append(letterGrades)
        average = getAverage(grades)
        studentInfo.append(average)
        studentInfos.append(studentInfo)


#Function for printing all student infos
def printStudentInfo():
    print("\n\n")
    #For each student, we print name, (letter) grades, and average
    for student in studentInfos:
        print(f"Student Name: {student[0]}")
        for grade in student[1]:
            print(f"Grade {student[1].index(grade) + 1}          {grade}          {student[2][student[1].index(grade)]}")
        print(f"Average Grade: {student[3]}")
        print("\n")

#Script start
createStudentInfo()
printStudentInfo()


