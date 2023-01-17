# EncryptedMessages
Simple GUI-based app that allows users to encrypt and decrypt text.

This code is a simple implementation of a graphical user interface (GUI) using the Tkinter library in Python. The purpose of this code is to provide a basic understanding of how to create a GUI application and how to perform encryption and decryption using base64 encoding and decoding.

The code creates a window with a text area, an entry field and a button. It also defines two functions, encrypt() and decrypt() that perform encryption and decryption of text entered in the text area using base64 encoding and decoding respectively. The code also uses a hardcoded password "1234" for encryption and decryption which is not a safe practice, and it displays an error message using the messagebox module if the password entered is invalid.

The following imports are used in this code:

from tkinter import *: imports all classes, constants and functions from the tkinter module.
from tkinter import messagebox: imports the messagebox class from the tkinter module, which is used to display message boxes.
import base64: imports the base64 module, which provides functions for base64 encoding and decoding.
It's important to note that this code is not intended for production use and it does not provide a high level of security. It is intended as a demonstration of basic concepts of GUI development and encryption techniques.
