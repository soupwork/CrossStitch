#Pillow Image Processing

from PIL import Image, ImageDraw

#filename='TestImage800x800.png'
filename = 'TestImagecircles.png'


def resize (img,xscale,yscale):
    print(f"Resize Image in pixels-  {xscale},{yscale}")
   
    resizeimg = img.resize((xscale,100))
    resizeimg.show()

def showCropSquare (img,x1=0,y1=0,x2=500,y2=500):
    print(f"show new crop square ")
    img.show()
    cropbox=ImageDraw.Draw(img)  #cropbox is a new object
    #cropbox.rectangle((x1,y1),(x2,y2), outline=(255),width=5)
    #rgb pink =(255, 102, 153), #ff6699
    #cropbox.line((x1,y1),(x2,y1), fill=(255,100,150))
    #cropbox.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255),width=7)
    cropbox.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)
    #cropbox.show()
    return


def openImage (filename):    
    print(f"open fresh Image {filename}")
    with Image.open(filename) as img:
        img.load()

    #img.show()
    print(f'image format is {img.format}')  #ex 'PNG', 'JPG'
    print(f'image size is {img.size}')  #ex '(800,800)'
    print(f'image Mode is {img.mode}')  #ex 'RGB'

    return(img)

if __name__ == "__main__":
    print(f"inside main ")
    print(f"source filename is {filename}")
    img=openImage(filename)
    showCropSquare(img)