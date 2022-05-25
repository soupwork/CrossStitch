#Pillow Image Processing

from PIL import Image, ImageDraw

#filename='TestImage800x800.png'
filename = 'TestImagecircles.png'
#boxcolor=(200,200,200)  #light grey box
#boxcolor=(255,0,0)  # Red box
# boxcolor=(0,0,255)  # blue box
# boxcolor=(0,255,0)  # green box
# boxcolor=(100,0,60)  # maroon box
# boxcolor=(100,0,10)  # brown box
boxcolor=(242,141,242)  # pink box

def resize (img,xsize,ysize):
    print(f"Resize Image in pixels-  {xsize},{ysize}")
    #img.reduce()
    resizeimg = img.resize((xsize,ysize))
    resizeimg.show()
    return(resizeimg)

def showCropSquare (img,xy=(10,10,500,500)):
    print(f"show new crop square ")
    # img.show()
    #img is a Image Object
    #cropbox is a ImageDraw object
    cropbox=ImageDraw.Draw(img)  

    #cropbox.rectangle((x1,y1),(x2,y2), outline=(255),width=5)
    #rgb pink =(255, 102, 153), #ff6699
    #cropbox.line((x1,y1),(x2,y1), fill=(255,100,150))
    cropbox.rectangle(xy, outline=boxcolor,width=7)
    #cropbox.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)
    img.show() #cropbox is tied to img
    return (img)


def cropSquare(img,xy):
    #img is the image object
    #xy is a 4-tuple(x0,y0,x1,y1)
    cropimg=img.crop(xy) 
    cropimg.show()
    return(cropimg)
    #end cropSquare

def openImage (filename):    
    print(f"open fresh Image {filename}")
    with Image.open(filename) as img:
        img.load()

    imageInfo(img)
    return(img)
    #end openImage

def saveImage(img,path='d:/dougsprogs/CrossStitch/', newfilename='testfile.png'):
    """save image and close """
 
    print(f"new path+filename is {path}{newfilename}")
    fp=f'{path}{newfilename}'
    #print('image type is ',type(img))
    img.save(fp)
    return
    #end saveImage


def imageInfo(img):
    """prints out the goodies about the image"""    
    print(f'image format is {img.format}')  #ex 'PNG', 'JPG'
    print(f'image size is {img.size}')  #ex '(800,800)'
    print(f'image Mode is {img.mode}')  #ex 'RGB'
    img.show()
    return
 

def blankImage():
      img = Image.new('RGB', (800,600),(200,200,200))  #this is the image object
      imgdraw = ImageDraw.Draw(img) #this is the image draw object


if __name__ == "__main__":
    print(f"inside main ")
    print(f"source filename is {filename}")
    img = openImage(filename)
    print('1-in main, image type is ',type(img))
    img = showCropSquare(img)
    xy=(10,10,500,500)
    img=cropSquare(img,xy)
    print('2-in main, image type is ',type(img))
    newsize=50
    img=resize(img,newsize,newsize)
    print('3-in main, image type is ',type(img))
    saveImage(img)
    
