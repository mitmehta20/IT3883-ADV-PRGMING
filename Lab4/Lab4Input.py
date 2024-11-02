#Mit Mehta

#import json to store json strings in input file
import json

#open input file in append mode 
inputFile = open('input.txt', 'a')

#loop 8 times to collect 8 student information
for x in range(8):
    #create student dict object and collect each piece of information
    student = {
        'firstName': input('Enter Student First Name: '),
        'lastName': input("Enter Student Last Name: "),
        'studentId': input("Enter student ID: "),
        'gpa': input("Enter GPA: ")
    }
    
    #write to student json string to file
    inputFile.write(json.dumps(student))
    inputFile.write('\n')

#close the input file
inputFile.close()
