from tkinter import *

root = Tk()
root.option_add("*font","impact 30")

Label(root , text = "weight (kg.)").grid(row = 0, column = 0 ,sticky = E , padx = 10 , pady = 10)
Entry(root , width = 6 ).grid(row = 0, column = 1 , padx = 10 )
Label(root , text = "height (m.)").grid(row = 1, column = 0 ,sticky = E , padx = 10 , pady = 10 )
Entry(root , width = 6 ).grid(row = 1, column = 1 , padx = 10 )
Label(root , text = "BMI").grid(row = 2 ,columnspan = 2 , padx = 10 , pady = 10)
Button(root , text = "Calculate", borderwidth = 5).grid(row = 3 ,columnspan = 2 , pady = 5)











root.mainloop()