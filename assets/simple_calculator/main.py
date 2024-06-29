import tkinter as tk

def on_button_click(character):
    if character == "=":
        try:
            # Evaluate the expression and display the result
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            # Display an error message
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif character == "C":
        # Clear the entry
        entry.delete(0, tk.END)
    else:
        # Append the character to the entry lol
        entry.insert(tk.END, character)
        
# Create the main window
app = tk.Tk()
app.title("Calculator")

# Create the buttons
entry = tk.Entry(app, width=16, font=('Helevetica', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# BUTTONS LMAO
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# values bruhhh
row_val = 1
col_val = 0

# Loop over the buttons list
for button in buttons:
    action = lambda x=button: on_button_click(x)
    tk.Button(app, text=button, width=5, height=2, command=action, font=('Helevetica', 18)).grid(row=row_val, column=col_val) # Say what you will about the font but its not BAD OKAY
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
        
# Run the application
app.mainloop()