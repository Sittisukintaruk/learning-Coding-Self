from tkinter import *


root = Tk()
root.option_add("*font" , "consolas 20")

f1 = Frame(root , bg = "green" )
f1.grid(row = 0 , column = 0 , columnspan = 2)

f2 = Frame(root, bg ="red")
f2.grid(row = 1,column = 0 ,sticky = "news" )


f3 = Frame(root, bg ="blue" )
f3.grid(row = 1,column = 1 ,sticky = "news" )


Label(f1 , text = "this is a label" ,width = 25).pack(padx = 10 , pady = 10)
for i in ['mocha' , 'latte' , 'espresso' ,'americanp','capucino']:
    Button(f2 , text = i , width = 10).pack(fill = X,padx = 10 , pady = 10 )

for i,c in enumerate("123456789"):
    Button(f3,text = c).grid(row = i // 3 , column = i % 3 , padx =     15 , pady = 15 )

Button(f3,text = "0" ,width = 10).grid(row = 4 , columnspan = 3 , padx =     15 , pady = 15 )

root.mainloop()