import tkinter as tk

# Function to change the color of the first label to green
def change_label_1_green():
    label1.config(bg="green")

# Function to change the color of the first label to red
def change_label_1_red():
    label1.config(bg="red")

# Function to change the color of the second label to green
def change_label_2_green():
    label2.config(bg="green")

# Function to change the color of the second label to red
def change_label_2_red():
    label2.config(bg="red")

# Function to handle color changes based on user input
def handle_command():
    command = command_entry.get().lower()  # Get the text entered in the Entry widget
    if command == "green label 1":
        change_label_1_green()
    elif command == "red label 1":
        change_label_1_red()
    elif command == "green label 2":
        change_label_2_green()
    elif command == "red label 2":
        change_label_2_red()
    else:
        print("Invalid command. Use 'green label 1', 'red label 1', 'green label 2', or 'red label 2'.")

# Create the Tkinter root window
root = tk.Tk()

# Create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create the first Label widget (label 1)
label1 = tk.Label(frame, width=2, height=1, relief="solid", bg="white")
label1.grid(row=0, column=0, padx=10, pady=10)

# Create the second Label widget (label 2)
label2 = tk.Label(frame, width=10, height=5, relief="solid", bg="white")
label2.grid(row=0, column=1, padx=10, pady=10)

# Create an Entry widget for command input
command_entry = tk.Entry(frame, width=20)
command_entry.grid(row=1, column=0, columnspan=2, pady=10)

# Create a Button widget to trigger the command
command_button = tk.Button(frame, text="Change Color", command=handle_command)
command_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
