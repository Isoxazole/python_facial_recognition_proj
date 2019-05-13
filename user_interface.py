from tkinter import *

form = Tk(className="FaceFind", useTk=1)


Label(form, text="Check Directory").grid(row=0)
entry1 = Entry(form)
entry1.grid(row=0, column=1)

form.mainloop()
