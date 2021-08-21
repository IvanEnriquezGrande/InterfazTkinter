from tkinter import Tk, Button, PhotoImage, Label, LabelFrame, W, E, N, S, Entry, END, StringVar, Scrollbar, Toplevel
from tkinter import ttk

class Contacts:
    def __init__(self, root):
        self.root = root
        self.create_left_icon()
        self.create_label_frame()

    def create_left_icon(self):
        photo = PhotoImage(file = 'Resources/Logo.gif')
        label = Label(image = photo)
        label.image = photo
        label.grid(row = 0, column = 0)

    def create_label_frame(self):
        labelframe = LabelFrame(self.root, text = 'Create new contact', bg = 'sky blue', font = 'serif 10')
        labelframe.grid(row = 0, column = 1, padx = 8, pady = 8, sticky = 'ew')
        Label(labelframe, text = 'Name:', bg = 'green', fg = 'white').grid(row = 1, column = 1, sticky = W, pady = 2, padx = 15)
        self.namefield = Entry(labelframe)
        self.namefield.grid(row = 1, column = 2, sticky = W, padx = 5, pady = 2)
        Label(labelframe, text = 'Email:', bg = "blue", fg = 'white').grid(row = 2, column = 1, sticky = W, pady = 2, padx = 15)
        self.emailfield = Entry(labelframe)
        self.emailfield.grid(row = 2, column = 2, sticky = W, padx = 5, pady = 2)
        Label(labelframe, text = 'Number:', bg = "red", fg = 'white').grid(row = 3, column = 1, sticky = W, pady = 2, padx = 15)
        self.numfield = Entry(labelframe)
        self.numfield.grid(row = 3, column = 2, sticky = W, padx = 5, pady = 2)
        Button(labelframe, text = 'Add contact', command="", bg = "blue", fg = "white").grid(row = 4, column = 2, sticky = E, padx = 5, pady = 5)

if __name__ == "__main__":
    root = Tk()
    root.title('Contacts list')
    app = Contacts(root)
    root.mainloop()