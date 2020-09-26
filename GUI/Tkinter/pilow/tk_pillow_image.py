from tkinter import *
from PIL import Image,ImageTk

def basic():
    root = Tk()
    root.option_add("*font" , "consolas 30")
    img = Image.open("pilow\\image-1.jpg")
    img = img.resize((int(img.width * .5) , int(img.height * .5)))
    photo = ImageTk.PhotoImage(img)
    lbe = Label( image = photo)
    lbe.pack()
    Label(root , text = "วัดพระธาตุ จังหวัดนาก").pack()
                    
def adv():
    images = ['phumin-1','phumin-2','phumin-3']
    img_list = []
    root = Tk()
    root.option_add("*font" , "consolas 30")

    for i,img in enumerate(images):

        imgs = Image.open(f'pilow\\{img}.jpg')
        # imgs = imgs.resize((int(imgs.width * .5) , int(imgs.height * .5)))
        img_list.append(ImageTk.PhotoImage(imgs))
        
        lbe = Label( image = img_list[i])
        lbe.grid(row = 0 , column = i)
        Label(root , text = f'{img}.jpg' ).grid(row = 1 , column = i)



   
    root.mainloop()
    
    

if __name__ == "__main__":
    adv()