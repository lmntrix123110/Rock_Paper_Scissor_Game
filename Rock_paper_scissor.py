from tkinter import *
from PIL import Image, ImageTk
from random import randint

win=Tk()
win.title("Game of ROCK-PAPER-SCISSOR")
win.geometry("700x400+500+200")
win.config(bg='#FF8768')

#1st Row
lab1=Label(win, text="Computer", font=("Times New Roman",40,"bold"), bg='#FF8768', fg='#57B0EF')
lab1.place(x=100, y=10, height=60, width=250)

lab2=Label(win, text="User", font=("Times New Roman",40,"bold"), bg='#FF8768', fg='#57B0EF')
lab2.place(x=500, y=10, height=60, width=130)

#Command
def ran(n):
    if n==1:
        img1=Image.open("RR.jpg")
        img1=img1.resize((120, 120), Image.ANTIALIAS)
        test1=ImageTk.PhotoImage(img1)

        Ilab1=Label(image=test1)
        Ilab1.image=test1
        Ilab1.place(x=120, y=120)
    elif n==2:
        img1=Image.open("RP.jpg")
        img1=img1.resize((120, 120), Image.ANTIALIAS)
        test1=ImageTk.PhotoImage(img1)
    
        Ilab1=Label(image=test1)
        Ilab1.image=test1
        Ilab1.place(x=120, y=120)
    else:
        img1=Image.open("RS.jpg")
        img1=img1.resize((120, 120), Image.ANTIALIAS)
        test1=ImageTk.PhotoImage(img1)
    
        Ilab1=Label(image=test1)
        Ilab1.image=test1
        Ilab1.place(x=120, y=120)

def rock():
    img2=Image.open("LR.jpg")
    img2=img2.resize((120, 120), Image.ANTIALIAS)
    test2=ImageTk.PhotoImage(img2)
    
    Ilab2=Label(image=test2)
    Ilab2.image=test2
    Ilab2.place(x=480, y=120)
    n=randint(1,4)
    ran(n)
    if n==1:
        lab=Label(win, text="Draw", font=("Times New Roman",20,"bold"), bg='#FF8768', fg='#AC75FF')
        lab.place(x=320, y=350, width=100)
    elif n==2:
        lab=Label(win, text="Lose", font=("Times New Roman",20,"bold"), bg='#FF8768', fg='#AC75FF')
        lab.place(x=320, y=350, width=100)
    else:
        lab=Label(win, text="Win", font=("Times New Roman",20,"bold"), bg='#FF8768', fg='#AC75FF')
        lab.place(x=320, y=350, width=100)

def paper():
    img2=Image.open("LS.jpg")
    img2=img2.resize((120, 120), Image.ANTIALIAS)
    test2=ImageTk.PhotoImage(img2)
    
    Ilab2=Label(image=test2)
    Ilab2.image=test2
    Ilab2.place(x=480, y=120)
    n=randint(1,4)
    ran(n)
    if n==1:
        lab=Label(win, text="Win", font=("Times New Roman",20,"bold"), bg='#FF8768', fg='#AC75FF')
        lab.place(x=320, y=350, width=100)
    elif n==2:
        lab=Label(win, text="Draw", font=("Times New Roman",20,"bold"), bg='#FF8768', fg='#AC75FF')
        lab.place(x=320, y=350, width=100)
    else:
        lab=Label(win, text="Lose", font=("Times New Roman",20,"bold"), bg='#FF8768', fg='#AC75FF')
        lab.place(x=320, y=350, width=100)

def scissor():
    img2=Image.open("LP.jpg")
    img2=img2.resize((120, 120), Image.ANTIALIAS)
    test2=ImageTk.PhotoImage(img2)
    
    Ilab2=Label(image=test2)
    Ilab2.image=test2
    Ilab2.place(x=480, y=120)
    n=randint(1,4)
    ran(n)
    if n==1:
        lab=Label(win, text="Lose", font=("Times New Roman",20,"bold"), bg='#FF8768', fg='#AC75FF')
        lab.place(x=320, y=350, width=100)
    elif n==2:
        lab=Label(win, text="Win", font=("Times New Roman",20,"bold"), bg='#FF8768', fg='#AC75FF')
        lab.place(x=320, y=350, width=100)
    else:
        lab=Label(win, text="Draw", font=("Times New Roman",20,"bold"), bg='#FF8768', fg='#AC75FF')
        lab.place(x=320, y=350, width=100)

#2nd Row
img1=Image.open("RR.jpg")
img1=img1.resize((120, 120), Image.ANTIALIAS)
test1=ImageTk.PhotoImage(img1)

Ilab1=Label(image=test1)
Ilab1.image=test1
Ilab1.place(x=120, y=120)

img2=Image.open("LR.jpg")
img2=img2.resize((120, 120), Image.ANTIALIAS)
test2=ImageTk.PhotoImage(img2)

Ilab2=Label(image=test2)
Ilab2.image=test2
Ilab2.place(x=480, y=120)

#3rd Row
rock1=Button(win, text="Rock", font=("Times New Roman", 20), command=rock, bg='#DC785E', fg='#FF3500')
rock1.place(x=100, y=300, height=40, width=130)

paper1=Button(win, text="Paper", font=("Times New Roman", 20), command=paper, bg='#DC785E', fg='#FF3500')
paper1.place(x=300, y=300, height=40, width=130)

scissor1=Button(win, text="Scissor", font=("Times New Roman", 20), command=scissor, bg='#DC785E', fg='#FF3500')
scissor1.place(x=500, y=300, height=40, width=130)

win.mainloop()