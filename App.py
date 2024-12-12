import time
import tkinter as tk
from tkinter import messagebox

# Calculator functions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def on_numpad_click(char):
    current_text = entry_display.get()
    if char == "C":
        entry_display.delete(0, tk.END)
    elif char == "Del":
        entry_display.delete(len(current_text) - 1, tk.END)
    elif char == "=":
        try:
            expression = entry_display.get()
            expression = expression.replace(')(', ')*(')  # Handle cases like 10(5+2)
            result = eval(expression)
            entry_display.delete(0, tk.END)
            entry_display.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    else:
        if char in '(' and current_text and current_text[-1].isdigit():
            entry_display.insert(tk.END, '*' + char)
        else:
            entry_display.insert(tk.END, char)

# GUI
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Configure grid
entry_display = tk.Entry(root, font=("Arial", 18), justify="right")
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons mapping
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("(", 5, 0), (")", 5, 1), ("C", 5, 2), ("Del", 5, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 14), command=lambda char=text: on_numpad_click(char))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Adjust row and column weights
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Execute program
print("Hello There ^v^")
time.sleep(1)
print("Calculator is launching....")
time.sleep(1)
root.mainloop()
time.sleep(1)
print("Calculator is closing....")
messagebox.showinfo("Goodbye", "Thank you for using the calculator")
print("Goodbye ^O^")