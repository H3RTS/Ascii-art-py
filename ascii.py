from PIL import Image

ascii_char = ' .:-=+*#%@'  #from the smallest to the largest char

with Image.open("macron.jpg") as image:
    
    image = image.resize((10, 10))

    for y in range(image.height):
        line = ""
        for x in range(image.width): ## we get the pixel in RGB format
            rgb = image.getpixel((x, y)) ## we do the average to make a shade of gray
            grey = sum(rgb) // len(rgb) ##we do a cross product to get the index
            index = grey * 9 // 255 ## we add 2 spaces, because in console the height of a tank is greater than its width
            line += ascii_char[index] + "  "
        print(line)
