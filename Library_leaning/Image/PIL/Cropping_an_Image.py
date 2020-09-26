from PIL import Image
import os 

# p = os.getcwdb()
# print(p)


def main(): 
    try:  
        path = "Image\stum01.png"
        img = Image.open(path)  
        width, height = img.size 
        area = (0, 0, width/2, height/2) 
        img = img.crop(area) 
        
         #Saved in the same relative location 
        img.save("Image\cropped_stum01.png") 
        
    except IOError: 
        print("หารูปไม่พบ")

if __name__ == "__main__": 
    main()