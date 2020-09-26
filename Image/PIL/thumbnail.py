from PIL import Image 

def main(): 
    try: 
        #Relative Path 
        img = Image.open("Image\stum01.png")  
         #In-place modification 
        img.thumbnail((200, 200))  
        img.save("Image\Thumbnail_stum01.png") 

     
        
    except IOError: 
        pass
  
if __name__ == "__main__": 

    main() 