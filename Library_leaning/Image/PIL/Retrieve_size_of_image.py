from PIL import Image
import os 

# p = os.getcwdb()
# print(p)



try:  
    path = "Image\stum01.png"
    with Image.open(path) as image:
        width , height = image.size
    print("ความสูงของรูป : {}".format(height))
    print("ความกว้างของรูป : {}".format(width))
except IOError: 
    print("หารูปไม่พบ")