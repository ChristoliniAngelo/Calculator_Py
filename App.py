import time
import math
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

def power(a, b):
    return math.pow(a, b)

def square_root(a):
    if a < 0:
        return "Error: Square root of negative number"
    return math.sqrt(a)

def on_numpad_click(char):
    current_text = entry_display.get()
    if char == "C":
        entry_display.delete(0, tk.END)
    elif char == "Del":
        entry_display.delete(len(current_text) - 1, tk.END)
    elif char == "=":
        try:
            expression = entry_display.get()
            expression = expression.replace("^", "**")
            expression = expression.replace(')(', ')*(')  # Handle cases like 10(5+2)
            result = eval(expression)
            entry_display.delete(0, tk.END)
            entry_display.insert(0, str(result))
            print(f"{expression} = {result}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    elif char == "√":
        try:
            if current_text:
                number = float(current_text)
                result = square_root(number)
                entry_display.delete(0, tk.END)
                entry_display.insert(0, str(result))
                print(f"√{number} = {result}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    else:
        if char in '(' and current_text and current_text[-1].isdigit():
            entry_display.insert(tk.END, '*' + char)
        else:
            entry_display.insert(tk.END, char)

# GUI
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.configure(bg="#2e3f4f")

# Entry Display
entry_display = tk.Entry(root, font=("Arial", 20), justify="right", bg="#dbe2ef", fg="#0f4c75")
entry_display.grid(row=0, column=0, columnspan=4, padx=15, pady=15, ipady=15)

# Buttons mapping
buttons = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("/", 1, 3), ("(", 1, 4), (")", 1, 5),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("√", 2, 4), ("^", 2, 5),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# UI colors and fonts
button_bg = "#3d5a80"
button_fg = "#ffffff"
button_active_bg = "#98c1d9"
button_font = ("Arial", 16)

for (text, row, col) in buttons:
    button = tk.Button(
        root,
        text=text,
        font=button_font,
        bg=button_bg,
        fg=button_fg,
        activebackground=button_active_bg,
        command=lambda char=text: on_numpad_click(char)
    )
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Add "Del" and "C" buttons with rowspan
del_button = tk.Button(
    root,
    text="Del",
    font=button_font,
    bg=button_bg,
    fg=button_fg,
    activebackground=button_active_bg,
    command=lambda: on_numpad_click("Del")
)
del_button.grid(row=3, column=4, columnspan=2, padx=5, pady=5, sticky="nsew")

clear_button = tk.Button(
    root,
    text="Clear",
    font=button_font,
    bg=button_bg,
    fg=button_fg,
    activebackground=button_active_bg,
    command=lambda: on_numpad_click("C")
)
clear_button.grid(row=4, column=5, columnspan=2, padx=5, pady=5, sticky="nsew")

# Adjust row and column weights
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(6):
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