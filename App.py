import tkinter as tk
from tkinter import messagebox

#calculator functions
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
    if char == "C":
        entry_display.delete(0, tk.END)
    elif char == "=":
        try:
            expression = entry_display.get()
            result = eval(expression) 
            entry_display.delete(0, tk.END)
            entry_display.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    else:
        entry_display.insert(tk.END, char)


#GUI
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

#congifure grid
entry_display = tk.Entry(root, font=("Arial", 18), justify="right")
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#buttons mapping
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("X", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 14), command=lambda char=text: on_numpad_click(char))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

#execute program
print("Hello There ^v^")
import time
time.sleep(1)
print("Program is lauching....")
time.sleep(1)
root.mainloop()
