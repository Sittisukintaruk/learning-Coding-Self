from tkinter import *



root = Tk()
root.option_add("*Font", "consolas 20")
# Button(root,text = "phone" , width = 20 ).pack()
# Button(root,text = "camera" , bg = "orange").pack(fill = X)
# Button(root,text = "computer" , fg = "blue" , padx = 30).pack()
# Button(root,text = "computer" , fg = "blue" ,bd = 10 , width = 20).pack()
# Button(root,text = "computer" , fg = "blue" ,bd = 10 , state = DISABLED).pack()
# Button(root,text = "green\ntea" , fg = "green" ,bd = 10 , ).pack()
photo = PhotoImage(file = "image\\softdrink.png")

Button(root , text = "test" , image = photo ,borderwidth = 0).pack()
Button(root , text = "test" , image = photo ,compound = LEFT  ,padx = 20).pack()
Button(root , text = "test" , image = photo ,compound = RIGHT  ,padx = 20).pack()
Button(root , text = "test" , image = photo ,compound = TOP , pady = 20).pack()
Button(root , text = "test" , image = photo ,compound = BOTTOM , pady = 20).pack()

        




root.mainloop()