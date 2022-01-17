from tkinter import *
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = open("passKey.txt", "wb")
f.write(key)
f.close()