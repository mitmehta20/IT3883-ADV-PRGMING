#Function for calculating new salary based on input
def calculate_new_salary(current_salary, raise_percentage):
    pay_raise = current_salary * (float(raise_percentage) / 100)
    new_salary = current_salary + pay_raise
    print("Pay Raise: $", pay_raise)
    print("New Salary: $", new_salary)

#Function for determining pay raise based on input
def determine_pay_raise(current_salary, performance_rating):
    match performance_rating:
        case 0:
            calculate_new_salary(current_salary, 0)
        case 1:
            calculate_new_salary(current_salary, 1.25)
        case 2:
            calculate_new_salary(current_salary, 2)
        case 3:
            calculate_new_salary(current_salary, 2.5)
        case 4:
            calculate_new_salary(current_salary, 3.25)
        case 5:
            calculate_new_salary(current_salary, 3.5)

x=0
while x == 0:
    performance_rating = int(input("Enter Employee Performance Rating (0-5): "))

    if(performance_rating < 0 or performance_rating > 5):
        print("Invalid Input. Please Enter an Integer between ")
    else:
        x=1

current_salary = float(input("Enter Employee Current Salary (In Dollars): "))

print("\n")

determine_pay_raise(current_salary, performance_rating)