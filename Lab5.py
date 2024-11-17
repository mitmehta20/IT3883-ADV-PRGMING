#Create global variable for a list of students
students = []

#Create a function to add a student to the list
def add_student(name, age, studentId, gpa):
    student = {
        'First Name': name,
        'Last Name': age,
        'Student ID': studentId,
        'GPA': gpa
    }
    students.append(student)

#Create a function to remove a students GPA
def remove_gpa(student):
    del student['GPA']
    return student

#Prompt the user to enter information for 3 users and send info to add a student
for i in range(3):
    name = input("Enter First Name: ")
    age = input("Enter Last Name: ")
    studentId = input("Enter Student ID: ")
    gpa = input("Enter GPA: ")
    add_student(name, age, studentId, gpa)

#Print the students within the list
for student in students:
    print(student)

#Break line for dramatic effect
print("\n")

#Print students again but after they have been called to remove GPA
print("Removing GPA from each student")
for student in students:
    print(remove_gpa(student))