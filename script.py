from PIL import Image
from numpy import asarray
gradient = " .:;x$&"
chars = [c for c in gradient]
chars.reverse()

def Open_image(name,sizer=10):
    img = Image.open(name)
    l = img.size[0]//sizer
    h = img.size[1]//sizer

    scale = 20/8
    l=int(l*scale)

    img = img.resize((l,h))
    img = img.convert('L')
    img = asarray(img)
    return img

def Pic_to_text(img, chars):
    h = len(img)
    l = len(img[0])
    ch_len = len(chars)
    pic = [['' for i in range(l)] for j in range(h)]
    delta = 255/(ch_len)
    for i in range(h):
        for j in range(l):
            index = int(img[i][j]//delta)
            pic[i][j] = chars[index]
    return pic

def Write(pic, name):
    with open(f"{name}.txt","w+") as f:
        for s in pic:
            for ch in s:
                f.write(ch)
            f.write("\n")

