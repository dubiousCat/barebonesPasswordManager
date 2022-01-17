#create main window

from tkinter import *
from cryptography.fernet import Fernet
import os

#encrypting methods
def encrypt():
    id = e1.get()
    password = e2.get()
    passCheck = e3.get()

    if id == "" or password == "" or passCheck == "":
        output1.delete("1.0", END)
        output1.insert(END, "fill in all required information")
    elif password != passCheck:
        output1.delete("1.0", END)
        output1.insert(END, "passwords do not match")
    else:
        #create txt file for storing passwords and what they're for
        f = open("username.txt", "a")
        f.write(id)
        f.write("\t")
        encrypted = hash(password)
        f.write(str(encrypted))
        f.write("\n")
        output1.delete("1.0", END)
        output1.insert(END, "password recorded")

def decrypt():
    #read txt file, print decrypted passwords

    output1.delete("1.0", END)
    outPrint = ""
    for line in open('username.txt'):
        contents = line.strip().split()
        outPrint += contents[0] + unhash(contents[1]) + "\n\n"
    
    output1.insert(END, outPrint)

#encrypting methods
def hash(input):
    fernet = Fernet(key)
    encMessage = fernet.encrypt(input.encode('utf-8'))
    return encMessage

def unhash(encoded):
    fernet = Fernet(key)
    return fernet.decrypt(encoded).decode()

#get key from file
f = open("passKey.txt", "rb")
key = f.read()
f.close()

root = Tk()

root.title("Password Manager")
root.geometry("800x700")

#ask user for password to encrypt 
l1 = Label(text = "what password is for:").place(x=50, y=150)
l2 = Label(text = "password:").place(x=50, y=180)
l3 = Label(text = "retype password:").place(x=50, y=210)

e1 = Entry(width = 50)
e1.place(x=250, y=150)
e2 = Entry(show = "*", width = 50)
e2.place(x=250, y=180)
e3 = Entry(show = "*", width = 50)
e3.place(x=250, y=210)

output1 = Text(height = 20, width = 87)
output1.place(x = 50, y = 240)

#button for encrypting
submitNew = Button(height = 1, width = 20, text = "Encrypt", command = lambda:encrypt())
submitNew.place(x = 600, y = 150)

#button for decrypting
getPass = Button(height = 1, width = 20, text = "Decrypt All", command = lambda:decrypt())
getPass.place(x = 600, y = 180)

root.mainloop()

#make log in screen
#set/reset password function