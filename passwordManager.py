#extremely basic program that encrypts and decrypts strings using the same key and 
#stores encrypted strings and key in text files
#uses tkinter to make extremely basic gui

from this import s
from tkinter import *
from cryptography.fernet import Fernet

#encrypting methods
def encrypt():
    siteName = e1.get()
    username = e4.get()
    password = e2.get()
    passCheck = e3.get()

    if siteName == "" or password == "" or passCheck == "" or username == "":
        output1.delete("1.0", END)
        output1.insert(END, "Fill in all required information")
    elif password != passCheck:
        output1.delete("1.0", END)
        output1.insert(END, "Passwords do not match")
    else:
        #create txt file for storing passwords and what they're for
        toHash = siteName
        f = open("username.txt", "ab")
        toHash += "| |"
        toHash += username
        toHash += "| |"
        toHash += password
        encrypted = hash(toHash)
        f.write(encrypted)
        f.write(b"\n")
        output1.delete("1.0", END)
        output1.insert(END, "Password recorded")
        f.close()

def decrypt():
    #read txt file, print decrypted passwords
    output1.delete("1.0", END)
    output1.insert(END, b"Site| |Username| |Password\n==========================================================================\n")
    for line in open('username.txt', 'rb'):
        output1.insert(END, unhash(line))
        output1.insert(END, b"\n")

#delete password
def deleteEntry():
    siteName = e1.get()

    if(siteName == ""):
        output1.delete("1.0", END)
        output1.insert(END, "Must provide site name of entry to delete")
        return 

    f = open("username.txt", "rb+")
    entries = f.readlines()
    f.seek(0)
    f.truncate()

    for n, line in enumerate(entries):
        decrypted = str(unhash(line))
        currentSite = decrypted.split("|")[0]

        if(currentSite != siteName):
            f.write(line)
    
    output1.delete("1.0", END)
    output1.insert(END, "Deleted successfully")

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

#create main window
root = Tk()
root.title("Password Manager")
root.geometry("800x700")

#ask user for password to encrypt 
l1 = Label(text = "Site:").place(x=50, y=120)
l4 = Label(text = "Username:").place(x=50, y=150)
l2 = Label(text = "Password:").place(x=50, y=180)
l3 = Label(text = "Retype password:").place(x=50, y=210)

e1 = Entry(width = 50)
e1.place(x=250, y=120)
e4 = Entry(width = 50)
e4.place(x=250, y=150)
e2 = Entry(show = "*", width = 50)
e2.place(x=250, y=180)
e3 = Entry(show = "*", width = 50)
e3.place(x=250, y=210)

output1 = Text(height = 20, width = 87)
output1.place(x = 50, y = 240)

#button for encrypting
submitNew = Button(height = 1, width = 20, text = "Encrypt", command = lambda:encrypt())
submitNew.place(x = 600, y = 120)

#button for decrypting
getPass = Button(height = 1, width = 20, text = "Decrypt All", command = lambda:decrypt())
getPass.place(x = 600, y = 150)

#button for deleting entry
getPass = Button(height = 1, width = 20, text = "Delete Site Entry", command = lambda:deleteEntry())
getPass.place(x = 600, y = 180)

root.mainloop()