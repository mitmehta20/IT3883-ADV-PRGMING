#Mit Mehta

#import json to change json string to dict
import json

#open input file in read mode and create output file in append mode
fileInput = open("input.txt", "r")
fileOutput = open("output.txt", "a")

#initialize array of students
students = []

#function to get academic status by gpa
def getStatus(gpaStr):
    gpa = float(gpaStr)
    if gpa >= 3.5:
        return "Dean’s List"
    elif gpa >= 2.0:
        return "Regular Standing"
    else:
        return "Probation"

#read all lines of input file to a variable
lines = fileInput.readlines()

#loop through the variable and turn json string back to dict object
for line in lines:
    student = json.loads(line)
    #call function to get status, then add it to the student
    status = getStatus(student['gpa'])
    student['status'] = status
    #add student to students array
    students.append(student)

#Create header for output file and left align all items with 20 spaces
header = f"{'First Name':<20}{'Last Name':<20}{'Student ID':<20}{'GPA':<20}{'Academic Status':<20}\n"
fileOutput.write(header)
#loop through students and append each student as a line in the file with the same spacing
for student in students:
    line = f"{student['firstName']:<20}{student['lastName']:<20}{student['studentId']:<20}{student['gpa']:<20}{student['status']:<20}"
    fileOutput.write(line + '\n')