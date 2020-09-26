from PIL import Image 
  
def main(): 
    try: 
        #Relative Path 
        img = Image.open("Image\stum01.png")  
        #splitting the image 
        print (img.split())
        
    except IOError: 
        pass
  
if __name__ == "__main__": 
    main() 