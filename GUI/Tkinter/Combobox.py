from tkinter import *
from tkinter import ttk
from datetime import  date


def on_lick (e):
    print (cby_day.get() , cby_mount.get() , cby_year.get())
    mout  = mm.index(cby_mount.get()) 
    bd = date(int(cby_year.get()),mout , int(cby_day.get()))
    print(bd)

root = Tk()
root.option_add("*font" , "consolas 25")
mm = ['jan' , 'Feb' , ' Mar']
cby_day = ttk.Combobox(root , values = list(range(1,32)) , width = 3  , state = "readonly")
cby_day.current(0)
cby_day.pack(side = LEFT)

cby_mount = ttk.Combobox(root , values = mm , width = 4 , state = "readonly")
cby_mount.current(1)
cby_mount.pack(side = LEFT)


cby_year = ttk.Combobox(root , values = list(range(1969 , 2021)) , width = 5 )
cby_year.current(1)
cby_year.pack(side = LEFT)


btn = Button(root , text = "Submit")
btn.pack()
btn.bind("<Button-1>" , on_lick)


root.mainloop()

