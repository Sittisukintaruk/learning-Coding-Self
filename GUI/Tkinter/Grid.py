from  tkinter import*

#Goldblog
tk_mancout = 0
tk_femanecount = 0
tk_total = 0

def on_cilckMale():
    global tk_mancout , tk_total
    tk_mancout +=1
    tk_total += 1

    tk_male.set(tk_mancout)
    tk_totals.set(f"total : {tk_total}") 
    print(f"get Male {tk_mancout}")
    

def on_cilckFeMale():
    global tk_femanecount , tk_total
    tk_femanecount +=1
    tk_total += 1

    tk_female.set(tk_femanecount)
    tk_totals.set(f"total : {tk_total}") 
    print(f"get Female {tk_femanecount}")

root = Tk()
root.resizable(0,0)
root.option_add("*font" ,"impact 25")

tk_male = IntVar()
tk_female = IntVar()
tk_totals = StringVar()



Button(root , text = "Male" ,bg = "cyan"  ,command = on_cilckMale ,width = 8).grid(row = 0 ,column = 0 ,ipady = 20)
Button(root , text = "Female" ,bg = "tomato", command = on_cilckFeMale ,width = 8).grid(row = 0 ,column = 1 ,ipady = 20 )
Label(root , textvariable = tk_male , bg = "cyan").grid(row = 1 ,  column =  0  ,sticky = "news")
Label(root , textvariable = tk_female , bg = "tomato").grid(row = 1 ,  column =  1 ,sticky = "news")
Label(root , textvariable = tk_totals , bg = "yellow").grid(row = 2 ,  columnspan = 2 ,sticky = "news")





root.mainloop()