from wand.image import Image
from wand.display import display

def print_img_info(img):
    print("Format:", img.format)
    print("Size:", img.size)
    print("Mode:", img.mode)

def show_img(img):
    display(img)
    
if __name__=="__main__":
    import sys
    input_file = sys.argv[1]
    img = Image(filename=input_file)
    print_img_info(img)