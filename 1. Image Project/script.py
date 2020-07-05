from PIL import Image


def rotateResize(img):
    """img should contain the complete path for the file"""
    img = Image.open(img)
    print(img.format,img.size)
    rgb_im = img.convert('RGB')
    rgb_im.save('colors.jpg')
    print(rgb_im.format)
    #convertedImage = img.rotate(angle).resize(size).save(img)
    #saveIt = convertedImage.convert("RGB")
    #saveIt.save("abc.jpg")
    #print(convertedImage.format,convertedImage.size)
    #convertedImage.save("pleaseSave")


angle = 270 #270 = 90 in clock-wise terms
size = 128,128
format = "JPEG"
rotateResize("images/ic_add_location_black_48dp")
