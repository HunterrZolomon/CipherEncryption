from tkinter import *
import socket
from tkinter.ttk import Combobox
from encrypt import reverse_encrypt
from encrypt import caesar_encrypt
from encrypt import rot_encrypt
from encrypt import transposition_encrypt



root = Tk()
root.title('Client')
root.geometry("500x250")

file_name = StringVar()
btn = StringVar()
encrypted = StringVar()


text = Text(root,height=15,width=500)
try:  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    text.insert(INSERT,"Socket created successfully!\n")
except socket.error as err:  
    text.insert(INSERT,"socket creation failed with error %s\n" %(err))

port = 8080
try:  
    s.connect(('127.0.0.1', port)) 
    text.insert(INSERT,"Connected to server!\n") 
except socket.error as err:  
    text.insert(INSERT,"Connection error :  %s\n" %(err))


label = Label(root,text = 'Enter filename : ')
label.place(x=5,y=40)
file_entry = Entry(root)
file_entry.place(x=120,y=40)


label = Label(root,text = 'Select the appropriate choice: ')
label.place(x=5,y=70)
rdbtn1 = Radiobutton(root,text='Encryption',value='E',variable = btn)
rdbtn1.place(x=10,y=95)
rdbtn2 = Radiobutton(root,text='Decryption',value='D',variable = btn)
rdbtn2.place(x=125,y=95)

label = Label(root,text = 'Select the type of encryption: ')
label.place(x=5,y=125)
data=("1. Reverse Cipher Encryption", "2. Caesar Cipher Encryption", "3. ROT13 Cipher Encryption", "4. Transposition Cipher Encryption")
cb=Combobox(root, values=data,width = 30)
cb.place(x=220, y=125)


def execute() :
    fname = file_entry.get()
    s.send(bytes(fname,'utf-8'))

    print("Filename is ",fname)
    f = open(fname)
    msg = f.readline()
    f.close()
    print("Message :",msg)

    pr = btn.get()
    print("Choice : ",pr)
    s.send(bytes(pr,'utf-8'))

    choice = cb.get()
    ch = choice[0]
    print("Choice selected is ",ch)
    s.send(bytes(ch,'utf-8'))

    if ch == '1' :
        if pr == 'E':
            encrypted = reverse_encrypt(msg)
        elif pr == 'D':
            encrypted = msg
    elif ch == '2' :
        if pr == 'E':
            encrypted = caesar_encrypt(msg)
        elif pr == 'D':
            encrypted = msg
    elif ch == '3':
        if pr == 'E':
            encrypted = rot_encrypt(msg)
        elif pr == 'D':
            encrypted = msg
    elif ch == '4':
        if pr == 'E':
            encrypted = transposition_encrypt(msg)
        elif pr == 'D':
            encrypted = msg
    print("Encrypted Cipher : ",encrypted)
    s.send(bytes(encrypted,'utf-8'))
    


submit_button = Button(root,text = 'Submit',command = execute)
submit_button.place(x=5,y=160)
text.pack()
mainloop()
s.close()


