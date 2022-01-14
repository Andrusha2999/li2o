from tkinter import *

def lisa_nos():
    if var_nina.get()=="Nina":
        c.create_oval((225, 245, 275, 305),width=3, fill="crimson", outline="black") 
    elif var_nina.get()=="tühi":
        c.create_oval((225, 225, 275, 275),width=3, fill="thistle", outline="thistle") 
def lisa_rot():
    if var_suu.get()=="":
        c.create_arc((100, 300, 400,400),start=180,extent=180, style=ARC, fill="black",width=10, outline="black")
    elif var_suu.get()=="tühi":
        c.create_arc((100, 300, 400,400),start=180,extent=180, style=ARC,   fill="thistle",width=10, outline="thistle")
def lisa_glaz():
    if var_eyes.get()=="Silmad":
        c.create_oval((300, 100, 400, 200), fill="whitesmoke",width=3, outline="black") 
        c.create_oval((200, 200, 100, 100), fill="whitesmoke",width=3, outline="black") 
    elif var_eyes.get()=="tühi":
        c.create_oval((300, 100, 400, 200),  fill="thistle", outline="thistle") 
        c.create_oval((200, 200, 100, 100),  fill="thistle", outline="thistle") 
def lisa_nao():
    if var_nao.get()=="Nägu":
        c.create_oval((10, 10, 490, 490),width=5, fill="lavender", outline="black") 
    elif var_nao.get()=="tühi":
        c.create_oval((10, 10, 490, 490),width=5, fill="thistle", outline="thistle") 
def lisa_sunnimark():
    if var_sunnimark.get()=="Sünnimärk":
        c.create_oval((300, 300, 315, 315),width=3, fill="sienna", outline="black") 
    elif var_sunnimark.get()=="tühi":
        c.create_oval((300, 300, 315, 315),width=3, fill="thistle", outline="thistle") 
aken=Tk()
aken.title("li2o")
aken.geometry('1000x500')
aken.configure(bg="blue")
aken.grab_set()
c = Canvas(aken, width=500, height=500, bg="thistle")
var_nina=StringVar()
ch_nina=Checkbutton(aken,text="Nina", variable=var_nina, onvalue="Nina", offvalue="tühi",bg="white",command=lisa_nos)
var_suu=StringVar()
ch_suu=Checkbutton(aken,text="Suu", variable=var_suu, onvalue="Suu", offvalue="tühi",bg="white",command=lisa_suu)
var_eyes=StringVar()
ch_eyes=Checkbutton(aken,text="Silmad", variable=var_eyes, onvalue="Silmad", offvalue="tühi",bg="white",command=lisa_eyes)
var_nao=StringVar()
ch_nao=Checkbutton(aken,text="Nägu", variable=var_nao, onvalue="Nägu", offvalue="tühi",bg="white",command=lisa_nao)
var_sunnimark=StringVar()




ch_nina.pack(side=RIGHT)
ch_suu.pack(side=RIGHT)
ch_eyes.pack(side=RIGHT)
ch_nao.pack(side=RIGHT)
c.pack(side=RIGHT)




aken.mainloop()
