"""from tkinter import *
from tkinter import ttk"""

# stexcum enq arajin cragiry
"""root = Tk()
frm = ttk.Frame(root, padding=100)#paddingy chapsy skzbnakan aktivacumic heto
frm.grid()#stexcum enq form
ttk.Label(frm, text="Hello World!").grid(column=3, row=0)#label anuny ev vayry columy 0 aysinqn syuny rowy aysinqn dirqy
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)#stexcum enq kojaky root destroy oakum e cragiry
root.mainloop()#end cragiry
#"""

# def min
"""a=[45,25,56,89,12,2]
b=a[0]
for i in a:
   if i<b:
      b=i
print(b)"""

            # stexcum enq kalkulator

import tkinter as tk
from tkinter import messagebox


win = tk.Tk()
win.geometry(f"240x270+100+200")  # chapsery bscveluc
win["bg"] = "#38ffe9"
win.title("kalkulator")


calc = tk.Entry(win, justify=tk.RIGHT, font=("Arial", 15), width=15)  # justify=sksi aj koxmic grel
calc.insert(0, "0")
calc.grid(row=0, column=0, columnspan=4, stick="we", padx=5)



def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char=='\r':
        calculate()

win.bind("<Key>", press_key)


def add_digit(digit):
    value = calc.get()
    if value[0] == "0" and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)


def add_operation(operacion):
    value = calc.get()
    if value[-1] in ("-+/*"):
        value = value[:-1]
    elif "+" in value or "-" in value or "/" in value or "*" in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operacion)


def calculate():
    value = calc.get()
    if value[-1] in "-+*/":
        value = value + value[:-1]
    try:
        calc.delete(0, tk.END)
    except NameError:
        messagebox.showinfo("Attention","write only numbers!!")
        calc.insert(0,0)


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=("Arial", 13), command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), fg="red",
                     command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), fg="red",
                     command=calculate)


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 13), fg="red",
                     command=clear)




make_digit_button("1").grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_digit_button("2").grid(row=1, column=1, stick="wens", padx=5, pady=5)
make_digit_button("3").grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_digit_button("4").grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_digit_button("5").grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_digit_button("6").grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_digit_button("7").grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_digit_button("8").grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_digit_button("9").grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_digit_button("0").grid(row=4, column=0, stick="wens", padx=5, pady=5)

make_operation_button("+").grid(row=1, column=3, stick="wens", padx=5, pady=5)
make_operation_button("-").grid(row=2, column=3, stick="wens", padx=5, pady=5)
make_operation_button("/").grid(row=3, column=3, stick="wens", padx=5, pady=5)
make_operation_button("*").grid(row=4, column=3, stick="wens", padx=5, pady=5)
make_calc_button("=").grid(row=4, column=2, stick="wens", padx=5, pady=5)
make_clear_button("C").grid(row=4, column=1, stick="wens", padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
