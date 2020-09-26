from tkinter import *


root = Tk()
root.option_add("*font" , "impact 20")

def on_click():
    lbs = tv_kag.get() * 2.2
    tv_bot.set(f"{lbs:.2f} lbs.")


tv_kag = DoubleVar()
tv_bot = StringVar() 

ent_kg = Entry(root  ,textvariable = tv_kag , width = 4)
ent_kg.pack(side = LEFT )
Label (root ,text =  "Kg.").pack(side = LEFT)
Button(root , text = "=" ,bg ="green" ,command =on_click).pack(side = LEFT)
lbl_ibs = Label (root ,textvariable = tv_bot)
lbl_ibs.pack(side = LEFT)







root.mainloop()