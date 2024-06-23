from PIL import Image
def assign_form(file):
    char_arr = list()
    img = file
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            char_arr.append(img.getpixel((j,i)))
        char_arr.append('n')
    return char_arr