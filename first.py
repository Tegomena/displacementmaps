import math 
import random
from PIL import Image, ImageDraw 

colors = ["grey", "lightgrey", "black"]

def addRectangulars(anImage, w, h, number):
    for i in range(number):

        x1 = random.randint(0,w)
        y1 = random.randint(0,w)
        
        x2 = x1 + 100
        y2 = y1 + 100

        shape = [x1,y1,x2,y2] 
        anImage.rectangle(shape, fill =colors[random.randint(0,2)]) 
    return anImage


def addVertLine(anImage, w, h, number):
    for i in range(number):
        x1 = random.randint(0,w)
        y1 = random.randint(0,w)
        
        x2 = x1 
        y2 = y1 + 100

        shape = [x1,y1,x2,y2] 
        anImage.line(shape, fill =colors[random.randint(0,2)], width=10) 
    return anImage


def addHorLine(anImage, w, h, number):
    for i in range(number):
        x1 = random.randint(0,w)
        y1 = random.randint(0,w)
        
        x2 = x1 + 100 
        y2 = y1

        shape = [x1,y1,x2,y2] 
        anImage.line(shape, fill =colors[random.randint(0,2)], width=10) 
    return anImage

def addCircle(anImage, w, h, number):
    for i in range(number):
        x1 = random.randint(0,w)
        y1 = random.randint(0,w)
        
        x2 = x1 + 100 
        y2 = y1 + 100

        shape = [x1,y1,x2,y2] 
        anImage.ellipse(shape, fill=colors[random.randint(0,2)]) 
    return anImage



if __name__ == "__main__":
    w, h = 1000, 1000
    image = Image.new("RGB", (w, h), color="white") 
    img = ImageDraw.Draw(image)   
  
    img = addRectangulars(img, w, h, 50)
    img = addCircle(img, w, h, 50)
    img = addVertLine(img, w, h, 50)
    img = addHorLine(img, w, h, 50)
    

    image.show() 
    image.save("one.png")