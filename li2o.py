from tkinter import *
def lisa_nos():
    if var_nos.get()=="nos":
        lbl.configure(text="")
    elif var_nos.get()=="tühi":
        lbl.configure(text="On vaja nina kustutada ära")
def lisa_s():
    if var_suu.get()=="suu":
        vastus.configure(text="Lisame suu canva peale")
    else:
        vastus.configure(text="On vaja suu kunstutada ära")
tk = Tk()
tk.geometry("1000*1000")
tk.title("ruuvõrrend")
var_nos=StringVar()
f1=Frame(tk,width=500,height=500)
f1.pack(side=TOP)
f2=Frame(tk,width=500,height=500)
f2.pack(side=BOTTOM)
c=Canvas(tk, width=500, height=500, bg="white")
c.pack()
с_nos=Checkbutton(f1,text = "нос", variable=var_nos,onvalue="nina",offvalue="tühi",command=lisa_nos)
c_nos.pack()
var_suu=StingVar()
с_s=Checkbutton(f1,text = "suu",font="Arial 20",command=lisa_s)
c_s.pack()
с3=Checkbutton(f1,text = "глаза",font="Arial 20",command=...)
c3.pack()
с4=Checkbutton(f1,text = "нос",font="Arial 20",command=...)
c4.pack()
с5=Checkbutton(f1,text = "рот",font="Arial 20",command=...)
c5.pack()
var=IntVar
c.create_oval((0,0,500,500))
c.create_oval((0,40,100,100))
c.create_oval((0,40,100,100))



tk.mainloop()

