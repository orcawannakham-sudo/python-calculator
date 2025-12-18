import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for display
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Function to add text to entry
def press(key):
    entry.insert(tk.END, key)

# Function to clear entry
def clear():
    entry.delete(0, tk.END)

# Function to calculate expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        b = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=calculate)
    elif text == 'C':
        b = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=clear)
        b.grid(row=row, column=col, columnspan=4, sticky="we", padx=1, pady=1)
        continue
    else:
        b = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: press(t))
    b.grid(row=row, column=col, padx=1, pady=1)

root.mainloop()
