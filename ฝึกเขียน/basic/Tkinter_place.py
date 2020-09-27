from tkinter import *


root = Tk()
root.option_add("*font" ,"consolas 20" )
# bt = Button(root ,  text = "Test-Place" , borderwidth = 5)
# bt.place(x = 100 , y = 100 , relx = 0.3 , rely = 0.3)
lable1 = Label(root , text = "label 1")
et1 = Entry(root , width = 10)
lable2 = Label(root , text = "label 2")
et2 = Entry(root , width = 10)
lable3 = Label(root , text = "label 3")
et3 = Entry(root , width = 10)

lable1.place(x = 100 , y = 120  )
# et1.place(x = 130 , y = 10)
# lable2.place(x = 10 , y = 50)
# et2.place(x = 130 , y = 50)
# lable3.place(x = 10 , y = 90)
# et3.place(x = 130 , y = 90)

root.geometry("300x300+120+120")        
root.mainloop()