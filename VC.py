from PIL import Image
import random



im = Image.open('num.png')
pixelMap = im.load()

size = (im.size[0]*2, im.size[1])
img1 = Image.new(im.mode, size)
img2 = Image.new(im.mode, size)

pixelsNew1 = img1.load()
pixelsNew2 = img2.load()

count = 0
for i in range(int(img1.size[0]/2)):
    for j in range(img1.size[1]):
        if 255 in pixelMap[i,j]: # bialy
            if random.random() < 0.5: # czarno-bialy
                pixelsNew1[i + count,j] = (0,0,0,255)
                pixelsNew1[i + count + 1,j] = (255,255,255,255)
              
                pixelsNew2[i + count,j] = (0,0,0,255)
                pixelsNew2[i + count + 1,j] = (255,255,255,255)
            else:                     # bialo-czarny
                pixelsNew1[i + count,j] = (255,255,255,255)
                pixelsNew1[i + count + 1,j] = (0,0,0,255)

                pixelsNew2[i + count,j] = (255,255,255,255)
                pixelsNew2[i + count + 1,j] = (0,0,0,255)
        else:                    # czarny
            if random.random() < 0.5: # czarno-bialy bialo-czarny
                pixelsNew1[i + count,j] = (0,0,0,255)
                pixelsNew1[i + count + 1,j] = (255,255,255,255)

                pixelsNew2[i + count,j] = (255,255,255,255)
                pixelsNew2[i + count + 1,j] = (0,0,0,255)
            else:                     # bialo-czarny czarno-bialy
                pixelsNew1[i + count,j] = (255,255,255,255)
                pixelsNew1[i + count + 1,j] = (0,0,0,255)

                pixelsNew2[i + count,j] = (0,0,0,255)
                pixelsNew2[i + count + 1,j] = (255,255,255,255)
    count += 1
img1 = img1.save("udzial1.png")
img2 = img2.save("udzial2.png")

im1 = Image.open('udzial1.png')
pixelMap1 = im1.load()
im2 = Image.open('udzial2.png')
pixelMap2 = im2.load()

decipher = Image.new(im.mode, im.size)
pixelMapDec = decipher.load()

count = 0
for i in range(int(im1.size[0]/2)):
    for j in range(im1.size[1]):
        # bialy
        if 255 in pixelMap1[i + count,j] and 255 in pixelMap2[i + count,j] and 0 in pixelMap1[i + count + 1,j] and 0 in pixelMap2[i + count + 1,j]:
            pixelMapDec[i, j] = (255,255,255,255)
        elif 0 in pixelMap1[i + count,j] and 0 in pixelMap2[i + count,j] and 255 in pixelMap1[i + count + 1,j] and 255 in pixelMap2[i + count + 1,j]:
            pixelMapDec[i, j] = (255,255,255,255)
        # czarny
        elif 0 in pixelMap1[i + count,j] and 255 in pixelMap2[i + count,j] and 255 in pixelMap1[i + count + 1,j] and 0 in pixelMap2[i + count + 1,j]:
            pixelMapDec[i, j] = (0,0,0,255)
        elif 255 in pixelMap1[i + count,j] and 0 in pixelMap2[i + count,j] and 0 in pixelMap1[i + count + 1,j] and 255 in pixelMap2[i + count + 1,j]:
            pixelMapDec[i, j] = (0,0,0,255)
    count += 1
decipher = decipher.save('odszyfrowanie.png')