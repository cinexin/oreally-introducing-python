from PIL import Image

def print_img_info(img):
    print("Format:", img.format)
    print("Size:", img.size)
    print("Mode:", img.mode)
    print("Additional info: ", img.info)
    
def show_img(img):
    img.show()
    
def crop_img(img):
    # crop accepts a 4-tuple indicating: left, top, right, down
    width, height = img.size
    left = 10
    right = width - 10
    top = 10
    down = height - 10
    crop = (left, top, right, down)
    cropped_img = img.crop(crop)
    return cropped_img

def save_img(img, name, format):
    img.save(name, format)
    
if __name__=="__main__":
    import sys
    file_name = sys.argv[1]
    img = Image.open(file_name)
    print_img_info(img)
    show_img(img)
    cropped_img = crop_img(img)
    print_img_info(cropped_img)
    show_img(cropped_img)
    output_name = sys.argv[2]
    output_format = 'PNG'
    save_img(cropped_img, output_name, output_format)
    saved_img = Image.open(output_name)
    print_img_info(saved_img)