import sys
import os
from PIL import Image
import pyheif

def convert_image(image):
    
    try:
        heic_image = pyheif.read(image)
        image_pil = Image.frombytes(heic_image.mode, heic_image.size, heic_image.data, "raw", heic_image.mode, heic_image.stride)
        print("Done")
        path = f"{''.join(image.split('.')[0])}.png"
        image_pil.save(path, format="PNG")
        print(f"Conversion of {image} is successfull")
        os.remove(image)
    except Exception as e:
        print(f"Faced an error while trying to convert {image}: {e}")
        
    
if __name__ == '__main__':
    
    image = sys.argv[1]
    convert_image(image)