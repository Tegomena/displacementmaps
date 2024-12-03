import math 
import random
from PIL import Image, ImageDraw 
from datetime import datetime
import configparser


class displacement:

    def __init__(self):
        self.colors = colors = ["grey", "lightgrey", "dimgrey", "gainsboro", "lightslategray", "slategrey"]


    def rgb2hex(self, r,g,b):
        return "#{:02x}{:02x}{:02x}".format(r,g,b)


    def calculateColors(self, steps):
        colors = []
        step = int(256 / steps)
        for i in range(steps):
            value = (i * step) 
            hexValue = self.rgb2hex(value, value, value)
            colors.append(hexValue)
        self.colors = colors



    def addRectangulars(self, anImage, w, h, number):
        theColor = self.colors[random.randint(0,len(self.colors)-1)]
        for i in range(number):

            x1 = random.randint(0,w)
            y1 = random.randint(0,w)
        
            x2 = x1 + 100
            y2 = y1 + 100

            shape = [x1,y1,x2,y2] 
            anImage.rectangle(shape, fill =theColor) 
        return anImage


    def addVertLine(self, anImage, w, h, number):       
        theColor = self.colors[random.randint(0,len(self.colors)-1)] 
        for i in range(number):
            x1 = random.randint(0,w)
            y1 = random.randint(0,w)
        
            x2 = x1 
            y2 = y1 + 100

            shape = [x1,y1,x2,y2] 
            anImage.line(shape, fill =theColor, width=10) 
        return anImage


    def addHorLine(self, anImage, w, h, number):
        theColor = self.colors[random.randint(0,len(self.colors)-1)] 
        for i in range(number):
            x1 = random.randint(0,w)
            y1 = random.randint(0,w)
        
            x2 = x1 + 100 
            y2 = y1

            shape = [x1,y1,x2,y2] 
            anImage.line(shape, fill =theColor, width=10) 
        return anImage

    def addCircle(self, anImage, w, h, number):
        for i in range(number):
            x1 = random.randint(0,w)
            y1 = random.randint(0,w)
        
            x2 = x1 + 100 
            y2 = y1 + 100

            shape = [x1,y1,x2,y2] 
            anImage.ellipse(shape, fill=self.colors[random.randint(0,2)]) 
        return anImage

    def addHorizontalRadiator(self, anImage, w, h, steps, number):
        theColor = self.colors[random.randint(0,len(self.colors)-1)]

        for i in range(number):
            x1 = random.randint(0,w)
            y1 = random.randint(0,w)
                    
            x2 = x1 
            y2 = y1 + 100 

            for i2 in range(steps):
                x1 = x1 + 30
                x2 = x2 + 30
                shape = [x1,y1,x2,y2] 
                anImage.line(shape, fill = theColor, width=10) 
        return anImage

    def addVerticalRadiator(self, anImage, w, h, steps, number):
        theColor = self.colors[random.randint(0,len(self.colors)-1)]

        for i in range(number):
            x1 = random.randint(0,w)
            y1 = random.randint(0,w)
        
            x2 = x1 + 100
            y2 = y1  

            for i2 in range(steps):
                y1 = y1 + 30
                y2 = y2 + 30
                shape = [x1,y1,x2,y2] 
                anImage.line(shape, fill =theColor, width=10) 
        return anImage

    def addVerticalRowOfHoles(self, anImage, w, h, steps, number):
        theColor = self.colors[random.randint(0,len(self.colors)-1)]
        for i in range(number):
            x1 = random.randint(0,w)
            y1 = random.randint(0,w)
        
            x2 = x1 + 10
            y2 = y1 + 10 

            for i2 in range(steps):
                y1 = y1 + 30
                y2 = y2 + 30
                shape = [x1,y1,x2,y2] 
                anImage.ellipse(shape, fill=theColor)  
        return anImage

    def addHorizontalRowOfHoles(self, anImage, w, h, steps, number):
        theColor = self.colors[random.randint(0,len(self.colors)-1)]
        for i in range(number):
            x1 = random.randint(0,w)
            y1 = random.randint(0,w)
        
            x2 = x1 + 10
            y2 = y1 + 10 

            for i2 in range(steps):
                x1 = x1 + 30
                x2 = x2 + 30
                shape = [x1,y1,x2,y2] 
                anImage.ellipse(shape, fill=theColor)  
        return anImage




if __name__ == "__main__":

    dis = displacement()
    dis.calculateColors(10)


    w, h = 1000, 1000
    image = Image.new("RGB", (w, h), color="white") 
    img = ImageDraw.Draw(image)   
  
    count = 50
    img = dis.addRectangulars(img, w, h, count)
    img = dis.addCircle(img, w, h, count // 2)
    img = dis.addVertLine(img, w, h, count)
    img = dis.addHorLine(img, w, h, count)
    img = dis.addHorizontalRadiator(img, w, h, 5, 5)
    img = dis.addVerticalRadiator(img, w, h, 3, 5)

    img = dis.addVerticalRowOfHoles(img, w, h, 5, 5)
    img = dis.addHorizontalRowOfHoles(img, w, h, 5, 5)


    now = datetime.now()
    filename = now.strftime("%d-%m-%Y_%H-%M-%S") + ".png"

    image.save(filename)

    image.show() 