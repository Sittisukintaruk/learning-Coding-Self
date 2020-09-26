from PIL import Image
import os 

# p = os.getcwdb()
# print(p)


def main(): 
    try:  
        path = "Image\stum01.png"
        img = Image.open(path)  
        
        
        #Getting histogram of image 
        print (img.histogram())
    except IOError: 
        print("หารูปไม่พบ")

if __name__ == "__main__": 
    main()