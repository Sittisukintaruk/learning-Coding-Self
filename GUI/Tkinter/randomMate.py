import random
from tkinter import *

randomlist = []
# count = int(input("Putnumber : "))
count = 4



def setlayout():
    def getRandom(count):
        for i in range(count):
            Eample_randoms = random.randrange(1, 9)
            randomlist.append(Eample_randoms)

    def getSumNumber(e):
        randomlist.clear()
        getRandom(count)
        Eample_randoms = random.randrange(10, 99)
        x = str(Eample_randoms)
        list_total.set(x)


        btn_text.set(randomlist[0])
        btn1_text.set(randomlist[1])
        btn2_text.set(randomlist[2])
        btn3_text.set(randomlist[3])


        tager = " ".join(map(str,randomlist))
        tager_total.set(tager)
        
        
    
   
    
    root = Tk()
    list_total = StringVar()
    tager_total = StringVar()
    btn_text = StringVar()
    btn1_text = StringVar()
    btn2_text = StringVar()
    btn3_text = StringVar()


    btn_text.set("0")
    btn1_text.set("0")
    btn2_text.set("0")
    btn3_text.set("0")


    getRandom(count)
    list_total.set("00")
    tager_total.set("0 0 0 0")

    root.option_add("*font" ,"consolas 80")
    f1 = Frame(root,bg = "red" ) 
    f1.grid(row = 0 , columnspan = 2 ,sticky = "news")
    f2 = Frame(root,bg = "blue" ) 
    f2.grid(row = 1 , columnspan = 2 ,sticky = "news")
    
    f3 = Frame(root,bg = "orange" ) 
    f3.grid(row = 2 , columnspan = 2 ,sticky = "news")

  


    lb = Label(f1 ,text = "00" ,textvariable = list_total)
    lb.pack(fill = X ,padx = 5 , pady  = 5)

    bn = Button(f2 ,text = "Random")
    bn.pack(fill = X ,padx = 5 , pady  = 5)
    bn.bind("<Button-1>" ,getSumNumber )
    
    lb = Button(f3 ,text = randomlist[0] ,textvariable=btn_text)
    lb.pack(side = LEFT ,padx = 10 , pady  = 10)

    lb1 = Button(f3 ,text = randomlist[1] ,textvariable=btn1_text)
    lb1.pack(side = LEFT ,padx = 10 , pady  = 10)

    lb2 = Button(f3 ,text = randomlist[2] ,textvariable=btn2_text)
    lb2.pack(side = LEFT ,padx = 10 , pady  = 10)


    lb3 = Button(f3 ,text = randomlist[3] ,textvariable=btn3_text)
    lb3.pack(side = LEFT ,padx = 10 , pady  = 10)


    root.mainloop()







if __name__ == "__main__":

    setlayout()
    # print(",".join(map(str , randomlist)))


