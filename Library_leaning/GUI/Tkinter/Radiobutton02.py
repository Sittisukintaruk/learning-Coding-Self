from tkinter import *

def on_clink(e):
    print(e.widget["text"] , e.widget["value"])
    


d = {"Thai" : "th" , "japanese" : "jp" , "Korean" : "Kr" , "Chinese" : "cn"}
root = Tk()
root.option_add("*font" , "consolas  20")
tv_code = StringVar()
tv_code.set("th")
n_column = 2
i = 0
for k,v in d.items():
    r = Radiobutton(root , text = k , value = v  , variable = tv_code ,indicatoron = False , width = 11 , bg = "gold" )
    r.bind("<Button-1>" , on_clink )
    r.grid(row = i // n_column  , column = i % n_column)
    i += 1





root.mainloop()