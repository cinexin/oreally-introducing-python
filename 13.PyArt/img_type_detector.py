import imghdr
import sys

def get_image_type(file):
    return imghdr.what(sys.argv[1])


if __name__ == "__main__":
    img_type = get_image_type(sys.argv[1])
    print("Type of %s file is: %s " %(sys.argv[1], img_type))