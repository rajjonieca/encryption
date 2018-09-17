"""
This is a Encryption File System for the Fulfillment of Enterprise Security Course
"""
from tkinter import *
from tkinter import ttk
from math import pow

import tkinter.simpledialog
import tkinter.messagebox

LARGE_FONT = ("Courier New", 30)
MID_FONT = ("Courier New", 20)
SMALL_FONT = ("Courier New", 12)



class ChowderES(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)  #initializes tkinter

        container = Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for f in (StartPage, EncryptPage, GenKeyPage):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  #raise it to the front


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="ChowderES", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        genkeyButton = Button(self, text="Generate Key", font=SMALL_FONT, command=lambda :controller.show_frame(GenKeyPage))
        genkeyButton.pack()

        encButton = Button(self, text="Encrypt Text File", font=SMALL_FONT, command=lambda :controller.show_frame(EncryptPage))
        encButton.pack()

        dscButton = Button(self, text="Decrypt Text File", font=SMALL_FONT)
        dscButton.pack()

class GenKeyPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        topFrame = Frame(self)
        topFrame.pack(side=TOP, pady=15)

        midFrame = Frame(self)
        midFrame.pack()

        passFrame = Frame(self)
        passFrame.pack(fill=X, padx=50, pady=20)

        buttonsFrame = ttk.Frame(self)
        buttonsFrame.pack(side=BOTTOM, pady=20, padx=20)

        label = Label(topFrame, text="ChowderES Key Generator!", font=MID_FONT)
        label.pack()

        labelName = Label(midFrame, text="Enter your Name: ", font=SMALL_FONT)
        labelName.grid(row=0, column=0, sticky=W)
        entryName = Entry(midFrame, width=40)
        entryName.grid(row=0, column=1)

        labelEmail = Label(midFrame, text="Enter your Email: ", font=SMALL_FONT)
        labelEmail.grid(row=1, column=0, sticky=W)
        entryEmail = Entry(midFrame, width=40)
        entryEmail.grid(row=1, column=1)

        labelKey = Label(midFrame, text="Enter your Keyname: ", font=SMALL_FONT)
        labelKey.grid(row=2, column=0, sticky=W)
        entryKey = Entry(midFrame, width=40)
        entryKey.grid(row=2, column=1)

        label2 = Label(passFrame, text="Enter Passphrase to protect your new key ", font=SMALL_FONT)
        label2.grid(columnspan=2, pady=20)

        labelPass = Label(passFrame, text="Enter Passphrase: ", font=SMALL_FONT)
        labelPass.grid(row=1, column=0, sticky=W),
        entryPass = Entry(passFrame, width=40, show="*")
        entryPass.grid(row=1, column=1)

        labelRepass = Label(passFrame, text="Reenter Passphrase: ", font=SMALL_FONT)
        labelRepass.grid(row=2, column=0, sticky=W)
        labelRepass = Entry(passFrame, width=40, show="*")
        labelRepass.grid(row=2, column=1)

        back = Button(buttonsFrame, text="Back", command=lambda :controller.show_frame(StartPage), font=SMALL_FONT)
        back.pack(side=LEFT)
        next = Button(buttonsFrame, text="Next", font=SMALL_FONT)
        next.pack(side=LEFT)

class EncryptPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        topFrame = Frame(self)
        topFrame.pack(side=TOP, pady=5)

        midFrame = Frame(self, width=300, height=100)
        midFrame.pack(padx=10)

        buttonsFrame = Frame(self)
        buttonsFrame.pack(side=BOTTOM, pady=5, padx=20)

        label = Label(topFrame, text="ChowderES File Encryptor", font=MID_FONT)
        label.pack()

        label2 = Label(midFrame, text="Enter Text to Encrypt:", font=SMALL_FONT)
        label2.pack(pady=15)
        text1 = Text(midFrame)
        text1.pack()

        back = Button(buttonsFrame, text="Back", font=SMALL_FONT, command=lambda :controller.show_frame(StartPage))
        back.pack(side=LEFT, pady=20)
        next = Button(buttonsFrame, text="Next", font=SMALL_FONT)
        next.pack(side=LEFT, pady=20)


root = ChowderES()

root.mainloop()
