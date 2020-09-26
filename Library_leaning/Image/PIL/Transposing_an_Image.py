from PIL import Image 
  
def main(): 
    try: 
        #Relative Path 
        img = Image.open("Image\stum01.png")  
          
        #transposing image  
        transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT) 
          
        #Save transposed image 
        transposed_img.save("Image\Transpose_stum01.png") 
    except IOError: 
        pass
  
if __name__ == "__main__": 
    main() 