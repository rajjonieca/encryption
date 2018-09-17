from tkinter import *
import tkinter.messagebox
from math import pow

LARGE_FONT = ("Courier New", 30)
MID_FONT = ("Courier New", 20)
SMALL_FONT = ("Courier New", 10)

root = Tk()
root.title("Encryption Shit")
root.geometry("450x470")
root.resizable(False,False)

title = Label(root,text="Encryption Shit",font=MID_FONT)
title.grid(row=0,column=0)

leftPanel = Frame(root)
leftPanel.grid(row=1,column=0,padx=10)

label1 = Label(leftPanel, text="Enter Passphrase:",font=SMALL_FONT)
label1.grid(row=0, column=0,sticky=W,pady=10)
label2 = Label(leftPanel, text="Enter Text: ",font=SMALL_FONT)
label2.grid(row=1, column=0,sticky=W,pady=10)
passEntry = Entry(leftPanel,width=40)
passEntry.grid(row=0, column=1,sticky=W)
encryptField = Text(leftPanel,width=53,height=8)
encryptField.grid(row=2,columnspan=2)

label3 = Label(leftPanel, text="Encrypted:",font=SMALL_FONT)
label3.grid(row=3,column=0,sticky=W,pady=10)
encryptedField = Text(leftPanel,width=53,height=8)
encryptedField.grid(row=4,columnspan=2)


def encryptor(event):
    e = 100
    n = 10
    rawText = encryptField.get("1.0",END)
    encrypted=""

    for letter in rawText:
        enc = (pow(ord(letter),e) % n) + 32
        encrypted = encrypted + chr(int(enc))

    encryptedField.insert("1.0",encrypted)

buttonShit = Button(leftPanel,text="ENCRYPT",bg="black",font=SMALL_FONT, fg="white")
buttonShit.grid(row=5,columnspan=2, pady=10)
buttonShit.bind("<Button-1>",encryptor)



root.mainloop()