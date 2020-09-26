from tkinter import *

def basic():
    root = Tk()
    photo_coffee = PhotoImage(file ="image\coffee.png" )
    photo_cubcak = PhotoImage(file ="image\cupcake.png" )
    photo_doughnut = PhotoImage(file ="image\doughnut.png" )
    photo_softdrink = PhotoImage(file ="image\softdrink.png" )
    photo_burger = PhotoImage(file ="image\Burger.png" )
    Button(root , image = photo_coffee , borderwidth = 0).pack(side = LEFT ,padx= 20 , pady = 15)
    Button(root , image = photo_cubcak  , borderwidth = 0).pack(side = LEFT ,padx= 20 , pady = 15)
    Button(root , image = photo_doughnut  , borderwidth = 0).pack(side = LEFT ,padx= 20 , pady = 15)
    Button(root , image = photo_softdrink  , borderwidth = 0).pack(side = LEFT ,padx= 20 , pady = 15)
    Button(root , image = photo_burger  , borderwidth = 0).pack(side = LEFT ,padx= 20 , pady = 15)
    root.mainloop()

def advice():
    root = Tk()
    image = ['coffee' , 'Burger','cupcake','doughnut' , 'softdrink']
    photos =[PhotoImage(file =f'image\\{img}.png') for img in image]
    for i in range (len(photos)) :
        Button(root , image = photos[i]  , borderwidth = 0).pack(side = LEFT ,padx= 20 , pady = 15)
        
    root.mainloop()

# image = ['coffee' , 'Burger','cupcake','doghnut' , 'softdrink']
# for item in image:
#     see =  "image\\"+ item +".png"
#     print(see)

if __name__ == "__main__":
    advice()   
    