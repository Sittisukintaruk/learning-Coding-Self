# importing required packages 
from tkinter import *
from PIL import ImageTk, Image 

# creating main window 
root = Tk() 

# arranging application parameters 
img = ImageTk.PhotoImage(Image.open("Image\stum01.png"))
imge = Image.open("Image\stum01.png")
width , height = imge.size
canvas = Canvas(root, width = 1080, height = 800) 

canvas.pack() 

# loading the image 
img = ImageTk.PhotoImage(Image.open("Image\stum01.png")) 

# arranging image parameters 
# in the application 
canvas.create_image(135, 20,image = img , anchor= NW) 

# running the application 
root.mainloop() 
