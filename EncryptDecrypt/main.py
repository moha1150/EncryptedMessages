from tkinter import *
from tkinter import messagebox
import base64
import os



def decrypt():
    password=code.get()


    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="blue")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="DECRYPT", font="arial",fg="white",bg="blue").place(x=10,y=0)
        text2=Text(screen2,font="calibri", bg="white", relief=GROOVE, wrap=WORD, bd=1)
        text2.place(x=10, y=40, width=380,height=150)

        text2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("encryption","Input Password")

    elif password !="1234":
        messagebox.showerror("encryption","Invalid Password")

def encrypt():
    password=code.get()


    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="red")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="ENCRYPT", font="arial",fg="white",bg="red").place(x=10,y=0)
        text2=Text(screen1,font="calibri", bg="white", relief=GROOVE, wrap=WORD, bd=1)
        text2.place(x=10, y=40, width=380,height=150)

        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("encryption","Input Password")

    elif password !="1234":
        messagebox.showerror("encryption","Invlaid Password")


def main_screen():

    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("425x425")

    #icon
    image_icon=PhotoImage(file="key.png")
    screen.iconphoto(False,image_icon)
    screen.title("TXTApp")

    def reset():
        code.set("")
        text1.delete(1.0,END)


    Label(text="Enter Text for Encryption and Decryption", fg="black", font=("Helvetica", 15)).place(x=10,y=10)
    text1=Text(font="Arial", bg="white", relief=GROOVE, wrap=WORD, bd=3)
    text1.place(x=10, y=50, width=300, height=150)

    Label(text="Enter Secret Key for Encryption and Decryption", fg="black", font=("Arial",15)).place(x=10,y= 200)

    code=StringVar()
    Entry(textvariable=code,width=25,bd=1,font=("calibri",20),show="*").place(x=10,y=230)
    
    Button(text="ENCRYPT", height="2", width=12, bg="red", fg="white", bd=1, command=encrypt).place(x=10,y=280)
    Button(text="DECRYPT", height="2", width=12, bg="green", fg="white", bd=1, command=decrypt).place(x=200,y=280)
    Button(text="RESET", height="2", width=33, bg="blue", fg="white", bd=1, command=reset).place(x=10,y=330)





    screen.mainloop()


main_screen()