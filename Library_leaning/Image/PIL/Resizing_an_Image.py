from PIL import Image
import os 

# p = os.getcwdb()
# print(p)


def main(): 
    try:  
        path = "Image\stum01.png"
        img = Image.open(path)  
        width, height = img.size 
        img = img.resize((int(width/2), int(height/2))) 
         #Saved in the same relative location 
        img.save("Image\Resize_stum01.png") 
        
    except IOError: 
        print("หารูปไม่พบ")

if __name__ == "__main__": 
    main()