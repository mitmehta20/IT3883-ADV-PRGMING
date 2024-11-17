# Mit Mehta Lab 6

#Import tkinter
import tkinter as tk

#Set tkinter root
root = tk.Tk()

#Set GUI dimension and title
root.geometry("500x500")
root.title("Lab 6")

# Set and insert empty label for age analysis display
label = tk.Label(root, text="")
label.pack()

# Insert Label to prompt user to insert age
promptLabel = tk.Label(root, text="Enter your age")
promptLabel.pack()

#Insert entry for user to write age
entry = tk.Entry(root, width=50)
entry.pack()

# Define button handler function
def button_click():

    try:
        # Change user input to int for analysis
        age = int(entry.get())

        #Create if-elif-else function to change the display label based on the age
        if age >= 65:
            label.config(text="SENIOR CITIZEN")
        elif age >= 18:
            label.config(text="YOU ARE OLD ENOUGH TO VOTE")
        else:
            label.config(text="YOU ARE NOT OLD ENOUGH TO VOTE")
    # Catch exception if User does not enter a number. Display message and prompt for retry
    except ValueError:
        label.config(text="INVALID INPUT. PLEASE ENTER AGE AS A NUMBER")

# Insert button and set the onClick operation to button_click function
button = tk.Button(root, text="Analyze", command=button_click)
button.pack()

# Start the GUI
root.mainloop()