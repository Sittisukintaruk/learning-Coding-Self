from tkinter import *

root = Tk()
root.option_add("*Font" , "consolas 25")

# Label(root, text = "apple").pack()
# Label(root, text = "apple" ,fg = "red").pack(anchor = E)  
# Label(root, text = "apple" ,bg = "green").pack(anchor = W)
# Label(root, text = "apple" , fg = "red" , bg = "green").pack(pady = 10)
# Label(root, text = "banana" , fg = "red" , bg = "yellow" , width = 15).pack()
# Label(root, text = "แผ่นดินของเรา"  , bg = "deep sky blue" ,).pack(fill = X)
# Label(root, text = "Green\ntea"  , bg = "green" ,).pack(fill = X)
Label(root, text = "happen is when you think , what you say , and what you do are in harmony"  , bg = "gold" ).pack(fill = X)
Label(root, text = "happen is when you think , what you say , and what you do are in harmony"  , bg = "red", wraplength = 400 ,justify = RIGHT).pack(fill = X)
Label(root, text = "happen is when you think , what you say , and what you do are in harmony"  , bg = "orange",wraplength = 700 ,justify = LEFT ).pack(fill = X)
Label(root, text = "happen is when you think , what you say , and what you do are in harmony"  , bg = "blue", wraplength = 700 ).pack(fill = X)

root.mainloop()