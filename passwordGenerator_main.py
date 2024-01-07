#Random password generator

from tkinter import *
from random import *
from tkinter import messagebox

obj = Tk()
obj.geometry("400x500")
obj.title("Password generator")

#chr to convert the number into an ascii character

def new_password():
    gen_password.delete(0, END)
    pw_length = int(entry.get())
    my_password = ''
    for x in range(0, pw_length):
        my_password += chr(randint(33, 126))
    gen_password.insert(0, my_password)

def accept():
    messagebox.showinfo("Password generator", "Password accepted.")

name = LabelFrame(obj, text="Enter your name")
name.pack(pady=10)

#entrybox for username entry
name_entry = Entry(name, font=("Arial", 20))
name_entry.pack(pady=20, padx=20)

frame = LabelFrame(obj, text="Number of characters")
frame.pack(pady=5)

#entry box to designate number of characters
entry = Entry(frame, font=("Calibre", 20))
entry.pack(pady=20, padx=20)

#entry box for our returned password
gen_password = Entry(obj, font=("Calibre", 20), bd=0)
gen_password.pack(pady=20)

#frame for buttons
button_frame = Frame(obj)
button_frame.pack(pady=20)

#creating buttons
my_button = Button(button_frame, text="Generate strong password", bg="#5c6bc0", fg="white", font="Arial 10", command=new_password)
my_button.grid(row=0, column=1, padx=10)

accept_button = Button(button_frame, text="Accept", bg="#5c6bc0", fg="white", font="Arial 10", command=accept)
accept_button.grid(row=1, column=1, padx=10, pady=10)

obj.mainloop()