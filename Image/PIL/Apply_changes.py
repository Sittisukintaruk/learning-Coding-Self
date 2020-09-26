# Code to apply operations on all the images 
# present in a folder one by one 
# operations such as rotating, cropping,  
from PIL import Image 
from PIL import ImageFilter 
import os 

"โอนไฟล์"


def main(): 
    try: 
        # get = os.getcwdb()
        # print(get)
        inPath =  "C:\\Users\\DIY\\Desktop\\Python\\library\\Image\\PIL\\Image"
        outPath =  "C:\\Users\\DIY\\Desktop\\Python\\library\\Image\\PIL\\Image_new"
        


        for imagePath in os.listdir(inPath):
            # imagePath contains name of the image  
            inputPath = os.path.join(inPath, imagePath)
            
            # inputPath contains the full directory name 
            img = Image.open(inputPath) 

            fullOutPath = os.path.join(outPath, 'invert_'+imagePath)
            # fullOutPath contains the path of the output 
            # image that needs to be generated 
            img.rotate(90).save(fullOutPath)
            print(fullOutPath)
       
    except IOError: 
        pass
  
if __name__ == "__main__": 
    main() 