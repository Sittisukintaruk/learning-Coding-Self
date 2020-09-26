from PIL import Image
import os 

# p = os.getcwdb()
# print(p)


def main(): 
    try:  
        path = "Image\stum01.png"
        path1 = "Image\stum03.png"
        img = Image.open(path)  
        #Relative Path 
        #Image which we want to paste 
        img1 = Image.open(path1)
        width, height = img1.size   
        img1 = img1.resize((int(width/2), int(height/2)))    
        img.paste(img1, (50, 50)) 
         #Saved in the same relative location 
        img.save("Image\Pasted_stum01.png") 
        
    except IOError: 
        print("หารูปไม่พบ")

if __name__ == "__main__": 
    main()