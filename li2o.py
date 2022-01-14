from tkinter import *

def lisa_rot():
    if var_rot.get()=="rot":
        c.create_arc((80, 400, 400,400),start=180,extent=180, style=ARC, fill="black",width=10, outline="black")
    elif var_rot.get()=="pust":
        c.create_arc((80, 400, 400,400),start=180,extent=180, style=ARC,   fill="white",width=10, outline="black")
def lisa_li2o():
    if var_li2o.get()=="li2o":
        c.create_oval((16, 8, 475, 520),width=5, fill="orange", outline="black") 
    elif var_li2o.get()=="pust":
        c.create_oval((16, 8, 475, 520),width=5, fill="orange", outline="orange") 
def lisa_nos():
    if var_nos.get()=="nos":
        c.create_oval((225, 280, 290, 305),width=3, fill="white", outline="black") 
    elif var_nos.get()=="pust":
        c.create_oval((225, 280, 290, 275),width=3, fill="white", outline="black") 
def lisa_glaz():
    if var_glaz.get()=="glaz":
        c.create_oval((230, 100, 400, 200), fill="green",width=3, outline="black") 
        c.create_oval((200, 250, 100, 100), fill="green",width=3, outline="black") 
    elif var_glaz.get()=="pust":
        c.create_oval((300, 100, 400, 200),  fill="green", outline="green") 
        c.create_oval((200, 200, 100, 100),  fill="green", outline="green") 
aken=Tk()
aken.title("li2o")
aken.geometry('1000x500')
aken.configure(bg="black")
aken.grab_set()
c = Canvas(aken, width=500, height=500, bg="lightblue")
var_nos=StringVar()
nos=Checkbutton(aken,text="nos", variable=var_nos, onvalue="nos", offvalue="pust",bg="white",command=lisa_nos)
var_rot=StringVar()
rot=Checkbutton(aken,text="rot", variable=var_rot, onvalue="rot", offvalue="pust",bg="white",command=lisa_rot)
var_glaz=StringVar()
glaz=Checkbutton(aken,text="glaz", variable=var_glaz, onvalue="glaz", offvalue="pust",bg="white",command=lisa_glaz)
var_li2o=StringVar()
li2o=Checkbutton(aken,text="li2o", variable=var_li2o, onvalue="li2o", offvalue="pust",bg="white",command=lisa_li2o)




nos.pack(side=RIGHT)
rot.pack(side=RIGHT)
glaz.pack(side=RIGHT)
li2o.pack(side=RIGHT)
c.pack(side=RIGHT)




aken.mainloop()
