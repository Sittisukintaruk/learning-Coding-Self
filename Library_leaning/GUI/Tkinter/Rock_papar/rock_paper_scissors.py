from tkinter import *
from random import  choice



def game():
    p1_stat = {'win' : 0 ,'losser' : 0 , 'ties' : 0}

    def rule (p1_shape , p2_shape):
        if p1_shape == p2_shape:
            p1_stat['ties'] +=1
            return "tied"

        elif (p1_shape == 'rock' and p2_shape == 'scissors' ) or ( p1_shape == 'paper' and p2_shape == 'rock' )  or ( p1_shape == 'scissors' and p2_shape == 'paper' ):
            p1_stat['win'] +=1
            return "p1 won"
        else:
            p1_stat['losser'] +=1
            return "p1 lost"

    def on_click(e):
        p1_shape = e.widget["text"]
        # print(p1_shape)
        p2_shape = choice(shapes)
        # print(p2_shape)
        resut = rule(p1_shape,p2_shape)
        tv_result.set(f'p1: {p1_shape}  p2 : {p2_shape}   result : {resut} ties'  )
        tv_results.set(f'{p1_stat["win"]} wins , {p1_stat["losser"]} losser , {p1_stat["ties"]} ties')
        # print(f'result = {resut}')
    root = Tk()
    root.option_add("*font" ,"impact 25")
    shapes = ['rock' , 'paper' , 'scissors']
    img = [PhotoImage(file =f'Rock_papar\\{img}.png') for img in shapes]
    f1 = Frame(root)
    f1.grid(row = 0 , column = 0)
    f2 = Frame(root)
    f2.grid(row = 1 , column = 0)
    # item_per_row = 3
    tv_result = StringVar()
    tv_results = StringVar()
   
    for i in range(len(img)) :
        bt = Button(f1, image = img[i] , text = shapes[i] , borderwidth = 0)
        bt.pack(side = LEFT , padx = 15)
        bt.bind('<Button-1>', on_click)
        # bt.grid(row = i // item_per_row , column = i % item_per_row)

    Label(f2 , textvariable = tv_result ,width = 40).pack()    
    Label(f2 , textvariable = tv_results ,width = 40 , bg = "gold").pack()    



    root.mainloop()


if __name__ == "__main__":
    game()


