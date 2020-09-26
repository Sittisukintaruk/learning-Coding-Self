from tkinter import *

def demo1 ():
    root = Tk()

    root.option_add("*font" , "impact 25")


    Button(root , text =  "apple" , width = 20).pack()
    Button(root , text =  "banana" , width = 20).pack()
    Button(root , text =  "Coconut" , width = 20).pack()
    Button(root , text =  "tuplip" , width = 20).pack(side = RIGHT ,padx = 10)
    Button(root , text =  "papaya" , width = 20).pack()

    # b1 = Button(root , text = "banana") 
    # b1.pack(side = LEFT)



    root.mainloop()

def demo2():
    root = Tk(className='Python Examples - Window Size')
    root.geometry("276x500")
    root.resizable(0, 0)
    root.option_add("*font" , "impact 25")
    # mw.option_add("*Button.Background", "black")
    # mw.option_add("*Button.Foreground", "red")


    Button(root , text =  "apple" , width = 20).pack()
    Button(root , text =  "banana" , width = 20).pack()
    Button(root , text =  "Coconut" , width = 20).pack()
    Button(root , text =  "tuplip" , width = 20).pack()
    Button(root , text =  "papaya" , width = 20).pack()

    # b1 = Button(root , text = "banana") 
    # b1.pack(side = LEFT)



    root.mainloop()


def demo3():
    root = Tk(className='Python Examples - Window Size')
    root.option_add("*Font" , "impact 30")
    for c in "rainblow":
        Button(root, text = c).pack(side = BOTTOM)
    root.mainloop()



if __name__ == "__main__":
    demo3()