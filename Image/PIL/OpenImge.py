from PIL import Image
import os 

# p = os.getcwdb()
# print(p)

path = "Image\stum01.png"

try:  
    img  = Image.open(path)
    img.show()
except IOError: 
    print("หารูปไม่พบ")