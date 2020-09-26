from tkinter import *
from datetime import datetime


def record_tranaction(menus_item):
    with open("sale.csv" ,mode='a' , newline='' ,encoding= 'UTF-8') as f:
        price = menus[menus_item] 
        dt = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        f.write(f'{menus_item} , {price} , {dt} \n')


def show(e):
    menus_item = e.widget.cget("text")
    tv_menu.set(f"menu = {menus_item} , price = {menus[menus_item]} Baht") 
    record_tranaction(menus_item)



root = Tk()
root.option_add("*font" , "impact 20")
menus = {"mocha" : 35 , "latte" : 40 ,"espresso" : 50 , "green tea" : 25 , "tea" : 30 ,"coke" : 40}
item_per_row = 3
tv_menu = StringVar()

for i,k in enumerate (menus.keys()):
    btn = Button(root ,text = k  , width = 15)
    btn.grid(row = i // item_per_row ,column = i % item_per_row )
    btn.bind("<Button-1>" , show)


Label(root, text ="menu" , textvariable = tv_menu , fg = "green").grid(columnspan = item_per_row)

# root.geometry()
# root.resizable()





root.mainloop()