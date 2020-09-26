from PIL import Image
import os 

# p = os.getcwdb()
# print(p)


def main(): 
    try:  
        path = "Image\stum01.png"
        img = Image.open(path)  
         #Angle given 
        img = img.rotate(180)  
          
         #Saved in the same relative location 
        img.save("Image\stum01_rotate.png") 
        
    except IOError: 
        print("หารูปไม่พบ")

if __name__ == "__main__": 
    main()