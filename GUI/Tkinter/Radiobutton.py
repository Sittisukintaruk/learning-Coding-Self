from tkinter import  *

def onselect():
    print (V_gender.get())

root = Tk()
root.option_add("*Font" , "consolas 20")
V_gender = StringVar()
V_gender.set("f")
Showindicatoron = True
Radiobutton(root, text = "male" , value = "m" , fg = "deep sky blue" , variable = V_gender , indicatoron = Showindicatoron , command = onselect).pack(side = LEFT , padx = 30)
Radiobutton(root, text = "female" , value = "f" , fg = "hot pink" , variable = V_gender , indicatoron = Showindicatoron , command = onselect).pack(side = LEFT)







root.mainloop()