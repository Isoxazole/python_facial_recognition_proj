from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import walkDirs


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


def show_recognized_faces():
    filename = "Recognized_Faces_Location.txt"
    show_matches.configure(state='normal')
    with open(filename, "r") as f:
        matches = f.readlines()
    for match in matches:
        show_matches.insert('end', match.strip() + "\n")
    show_matches.configure(state='disabled')

def submit():
    good_to_start = True
    if entry1.get() == "":
        default_path = os.path.abspath(os.sep)
        messagebox.showinfo("Default Directory Used", "We noticed you didn't enter anything for your search "
                                                      "directory, so it will now be set to \"%s\"" % default_path)
        good_to_start = False
    elif not os.path.exists(entry1.get()) or not os.path.isdir(entry1.get()):
        messagebox.showerror("Error", "'%s' is not a valid directory path.\n"
                                      " Please enter a valid path for your search directory of choice" % entry1.get())
        good_to_start = False
    if not os.path.exists(entry2.get()) or not entry2.get().upper().endswith(tuple(i for i in walkDirs.imageFiles)):
        messagebox.showerror("Error", "'%s' is not a valid picture path.\n"
                                      " Please enter a valid path for your picture of choice" % entry2.get())
        good_to_start = False
    if good_to_start:

        directory_path = os.path.abspath(entry1.get())
        picture_path = os.path.abspath(entry2.get())

        #Run directory walk with path inputted
        walkDirs.walk_dirs(directory_path)

        known_face_file, count = faceRec.face_rec(picture_path)

        show_recognized_faces()

        messagebox.showinfo("FaceFind Search Completed", f"There were %s recognized faces\n"
                           "The full path of the images with the recognized face is here:\n %s" % (count, known_face_file))

        # print(directory_path)
        # print(picture_path)


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
search_button = Button(form, text="Search", command=submit)
search_button.grid(row=2, column=0)

# show picture match paths here
# Text box and scroll bar made here
show_matches = Text(form, bg="gray", height=10, width=50, state='disabled')
show_matches.grid(row=3, columnspan=4)

scroll_bar = Scrollbar(form, orient=VERTICAL)
scroll_bar.grid(sticky=NS, column=4, row=3)
scroll_bar.config(command=show_matches.yview)

show_matches.config(yscrollcommand=scroll_bar.set)


form.mainloop()
