from tkinter import  *


def on_clik():
    print(chk1.get(), chk2.get(), chk3.get())

root = Tk()
root.option_add("*font" , "impact 30")
chk1 = BooleanVar()
chk2 = BooleanVar()
chk3 = BooleanVar()
Label(root , text = "You Interest" ,bg = "gold").pack()
Checkbutton(root, text = "music" , variable = chk1).pack(anchor = W)
Checkbutton(root, text = "Book" , variable = chk2).pack(anchor = W)
Checkbutton(root, text = "Movie" , variable = chk3).pack(anchor = W)
Button(root , text = "submit" , command = on_clik).pack()


root.mainloop()