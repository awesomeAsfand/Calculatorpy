import tkinter as tk
from tkinter import *
from tkinter.ttk import *
root = Tk()
root.geometry('650x500')
root.title("Calculator")
lbl= Label(root, text="", font=50).pack()

input_text = StringVar()
lbl = StringVar()
global expression


def btn_click(item):
    try:
        global expression
        expression += str(item)
        input_text.set(expression)

    except:
        "name error"


def btn_clear():
    global expression
    expression = " "
    input_text.set("")


def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    lbl.set(result)
    expression = " "




input_frame = tk.Frame(root, width=450, height=30)
input_frame.pack(side=TOP)
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=5)
btn_frame = tk.Frame(root, width=300, height=300, bg="black")
btn_frame.pack()
clear = tk.Button(btn_frame, text="Clear", fg="black", command=lambda: btn_clear(), width=65, height=3, cursor="hand2").grid(row=0, column=0, columnspan=3)
divide= tk.Button(btn_frame, text="/", width=20, height=3, command= lambda : btn_click("/"), cursor="hand2").grid(row=0, column=3,padx = 1, pady = 1)
seven = tk.Button(btn_frame, text="7", width=20, height=3, command=lambda :btn_click(7), cursor="hand2").grid(row=1,column=0,padx=1,pady=1)
eight= tk.Button(btn_frame, text="8", width=20, height=3, command=lambda :btn_click(8), cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
nine= tk.Button(btn_frame,text="9", width=20, height=3, command=lambda :btn_click(9), cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
multiply= tk.Button(btn_frame, text="*", width=20, height=3, command=lambda :btn_click("*")).grid(row=1, column=3,padx=1,pady=1)
four= tk.Button(btn_frame, text="4", width=20, height=3, command=lambda : btn_click(4), cursor="hand2").grid(row=2, column=0, padx=1,pady=1)
five= tk.Button(btn_frame, text="5", width=20, height=3, command=lambda : btn_click(5), cursor="hand2").grid(row=2, column=1, padx=1,pady=1)
six= tk.Button(btn_frame, text="6", width=20, height=3, command=lambda : btn_click(6), cursor="hand2").grid(row=2, column=2, padx=1,pady=1)
plus= tk.Button(btn_frame, text="+", width=20, height=3, command=lambda : btn_click("+"), cursor="hand2").grid(row=2, column=3, padx=1,pady=1)
three= tk.Button(btn_frame, text="3", width=20, height=3, command=lambda : btn_click(3), cursor="hand2").grid(row=3, column=0, padx=1,pady=1)
two= tk.Button(btn_frame, text="2", width=20, height=3, command=lambda : btn_click(2), cursor="hand2").grid(row=3, column=1, padx=1,pady=1)
one= tk.Button(btn_frame, text="1", width=20, height=3, command=lambda : btn_click(1), cursor="hand2").grid(row=3, column=2, padx=1,pady=1)
minus= tk.Button(btn_frame, text="-", width=20, height=3, command=lambda : btn_click("-"), cursor="hand2").grid(row=3, column=3, padx=1,pady=1)
zero= tk.Button(btn_frame, text="0", width=42, height=3, command=lambda : btn_click(0), cursor="hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point= tk.Button(btn_frame, text=".", width=20, height=3, command=lambda : btn_click("."), cursor="hand2").grid(row=4, column=2, padx=1,pady=1)
equal= tk.Button(btn_frame, text="=", width=20, height=3, command=lambda : btn_equal(), cursor="hand2").grid(row=4, column=3, padx=1,pady=1)










root.mainloop()