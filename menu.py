#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry('500x200')
window.configure(bg="#e6e6e6")

# -----------------------------------|
# Create a new style ----------------|
# -----------------------------------|

# create the style object
s = ttk.Style()

# add the style and naming that style variable as
# W.Tbutton (TButton is used for ttk.Button
s.configure('W.TButton', font=
('calibri', 10, 'bold', 'underline'),
            foreground='green',
            background='red')

window.title('Welcome to TK')
welcome_label = ttk.Label(window, text="Welcome to HTML Image Optimizer")
input_text_label = ttk.Label(window, text="Please enter image path:")
input_text = ttk.Entry(window, width=25)
ok_button = ttk.Button(window, text='OK', style='W.TButton')

print("ok_button.winfo_class() is: ".format(welcome_label.winfo_class()))

welcome_label.grid(column=0, row=0, pady=20, padx=10)
# NOTE: Use the sticky option to align the label in itself into the view, not the contents.
input_text_label.grid(column=0, row=1, sticky=W, padx=10)
input_text.grid(column=1, row=1)
ok_button.grid(column=1, row=2, sticky=E, pady=10)
window.mainloop()
