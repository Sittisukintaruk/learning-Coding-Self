from tkinter import *





def criteriaget():
    def on_drag(e):
        color_hex = f'#{sc[0].get():02X}{sc[1].get():02X}{sc[2].get():02X}'
        rating_score.set(color_hex)
        Lablecolor["bg"] = color_hex

    root = Tk()
    root.option_add("*font" , "consolas 20")
    rating_score = StringVar()

    criteria = ['red' , 'green' , 'blue']
    sc = []
    for i , c in enumerate(criteria):
        Label(root , text = c, fg = c ).grid(row = i , column = 0 , sticky = "sw" ,padx = 10 , pady = 10 )
        w = Scale(root , from_ = 1 , to = 200 , orient = HORIZONTAL , length = 200 , width = 30 , fg = c)
        w.grid(row = i , column = 1)
        w.set(120)
        w.bind('<B1-Motion>', on_drag)
        w.bind('<Button-1>', on_drag)
        sc.append(w)

    Lablecolor = Label(root ,textvariable = rating_score)
    Lablecolor.grid(row = 3 , columnspan = 2 , sticky = "news")
    root.mainloop()



def test():
    def on_drag(e):
        total = 0
        for score in sc:
            total += score.get()
            rating_score.set(f'{total / len(sc):.2f}') 
        
        pass

         
    root = Tk()
    root.option_add("*font" , "consolas 20")
    rating_score = StringVar()

    criteria = ['price', 'performance' , 'design' , 'service' , 'reriabilty']
    sc = []
    for i , c in enumerate(criteria):
        Label(root , text = c ).grid(row = i , column = 0 , sticky = "sw" ,padx = 10 , pady = 10 )
        w = Scale(root , from_ = 1 , to = 10 , orient = HORIZONTAL , length = 200 , width = 30 )
        w.grid(row = i , column = 1)
        w.set(120)
        w.bind('<B1-Motion>', on_drag)
        w.bind('<Button-1>', on_drag)
        sc.append(w)

    Lablecolor = Label(root ,textvariable = rating_score)
    Lablecolor.grid( columnspan = 2 , sticky = "news")
    root.mainloop()


if __name__ == "__main__":
    test()


