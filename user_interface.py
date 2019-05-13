from tkinter import *

form = Tk(className="FaceFind", useTk=1)
form.geometry("500x500")

# User will input the directory for checking here, default if blank will be root/C:
Label(form, text="Check Directory").grid(row=0)
entry1 = Entry(form)
entry1.grid(row=0, column=1)

# Location of picture used for comparison goes here
Label(form, text='Picture Location').grid(row=1)
entry2 = Entry(form)
entry2.grid(row=1, column=1)

# show picture match paths here
show_matches = Label(form, bg="gray", height=10, width = 50,
                     text="Matches will Display here").grid(row=2, columnspan=4)

Scrollbar(show_matches)

form.mainloop()
