from tkinter import Tk, Button, PhotoImage, Label, LabelFrame, W, E, N, S, Entry, END, StringVar, Scrollbar, Toplevel
from tkinter import ttk

class Contacts:
    def __init__(self, root):
        self.root = root
        self.create_left_icon()

    def create_left_icon(self):
        photo = PhotoImage(file = 'Resources/Logo.gif')
        label = Label(image = photo)
        label.image = photo
        label.grid(row = 0, column = 0)



if __name__ == "__main__":
    root = Tk()
    root.title('Contacts list')
    app = Contacts(root)
    root.mainloop()