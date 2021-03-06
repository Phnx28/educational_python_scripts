from PIL import Image, ImageOps, ImageDraw

dicew = 100

im = Image.open("/tmp/image.png")
im = ImageOps.grayscale(im)
im = ImageOps.equalize(im)

diceh = im.height / im.width * dicew

dicesize = int(im.width / dicew)

nim = Image.new("L", (im.width, im.height), 'white')
nimd = ImageDraw.Draw(nim)

for y in range(0, im.height-dicesize, dicesize):
    for x in range(0, im.width-dicesize, dicesize):
        thisSectorColor = 0
        for dicex in range(0, dicesize):
            for dicey in range(0, dicesize): 
                thisSectorColor += im.getpixel((x+dicex, y+dicey))
        thisSectorColor = thisSectorColor / (dicesize **2 )
        
        nimd.rectangle(((x, y),(x+dicesize, y+dicesize)), thisSectorColor)
        diceNumber = (255-thisSectorColor) * 6 / 255 + 1
        #print (x, y, thisSectorColor, diceNumber)
        print diceNumber,
    print
