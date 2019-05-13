from tkinter import *
from tkinter import filedialog

form = Tk(className="FaceFind", useTk=1)
form.geometry("500x500")

# User will input the directory for checking here, default if blank will be root/C:
Label(form, text="Check Directory").grid(row=0)
entry1 = Entry(form)
entry1.grid(row=0, column=1)

def browse_button(entry):
    filename = filedialog.askdirectory()
    entry.insert(0, filename)

def browse_file(entry):
    filename = filedialog.askopenfilename()
    entry.insert(0, filename)


# browse directory button for search directory
browse_directory = Button(text="Browse", command=(lambda: browse_button(entry1)))
browse_directory.grid(row=0, column=2)

# Location of picture used for comparison goes here
Label(form, text='Picture Location').grid(row=1)
entry2 = Entry(form)
entry2.grid(row=1, column=1)

# browse directory button for search directory
browse_directory = Button(text="Browse", command=(lambda: browse_file(entry2)))
browse_directory.grid(row=1, column=2)

# this should check that the picture is actually a picture by the extension
search_button = Button(form, text="Search")
search_button.grid(row=2, column=0)


# show picture match paths here
show_matches = Label(form, bg="gray", height=10, width=50,
                     text="Matches will Display here").grid(row=3, columnspan=4)

Scrollbar(show_matches)

form.mainloop()
