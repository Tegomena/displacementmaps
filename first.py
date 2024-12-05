import random
from PIL import Image, ImageDraw 
from datetime import datetime
import configparser

import argparse

class displacement:

    def __init__(self, config):
        self.config = config
        self.colors = ["grey", "lightgrey", "dimgrey", "gainsboro", "lightslategray", "slategrey"]
        self.calculateColors(int(self.config["imagesettings"]["numberofcolors"]))
        self.newImage()


    def newImage(self):
        image = Image.new("RGB", (int(self.config["imagesettings"]["width"]), int(self.config["imagesettings"]["width"])), color="white") 
        img = ImageDraw.Draw(image)
        self.img = img
        self.image = image

    def saveImageToFile(self, filename):
        self.image.save(filename)

    def getRandomStartpoint(self):
        x1 = random.randint(0,int(self.config["imagesettings"]["width"]))
        y1 = random.randint(0,int(self.config["imagesettings"]["height"]))
        return x1, y1


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

    def addRectangulars(self):
        theColor = self.colors[random.randint(0,len(self.colors)-1)]
        for i in range(int(self.config["rectangulars"]["number"])):
            x1, y1 = self.getRandomStartpoint()
        
            x2 = x1 + 100
            y2 = y1 + 100

            shape = [x1,y1,x2,y2] 
            self.img.rectangle(shape, fill =theColor) 

    def addVertLine(self):       
        theColor = self.colors[random.randint(0,len(self.colors)-1)] 
        for i in range(int(self.config["vertlines"]["number"])):
            x1, y1 = self.getRandomStartpoint()
        
            x2 = x1 
            y2 = y1 + 100

            shape = [x1,y1,x2,y2] 
            self.img.line(shape, fill =theColor, width=10) 
        
    def addHorLine(self):
        theColor = self.colors[random.randint(0,len(self.colors)-1)] 
        for i in range(int(self.config["horlines"]["number"])):
            x1, y1 = self.getRandomStartpoint()
        
            x2 = x1 + 100 
            y2 = y1

            shape = [x1,y1,x2,y2] 
            self.img.line(shape, fill =theColor, width=10) 

    def addCircle(self):
        for i in range(int(self.config["circles"]["number"])):
            x1, y1 = self.getRandomStartpoint()
        
            x2 = x1 + 100 
            y2 = y1 + 100

            shape = [x1,y1,x2,y2] 
            self.img.ellipse(shape, fill=self.colors[random.randint(0,2)]) 
        

    def addHorizontalRadiator(self):
        theColor = self.colors[random.randint(0,len(self.colors)-1)]

        for i in range(int(self.config["horizontalradiator"]["number"])):
            x1, y1 = self.getRandomStartpoint()
                    
            x2 = x1 
            y2 = y1 + 100 

            for i2 in range(int(self.config["horizontalradiator"]["steps"])):
                x1 = x1 + 30
                x2 = x2 + 30
                shape = [x1,y1,x2,y2] 
                self.img.line(shape, fill = theColor, width=10) 
        

    def addVerticalRadiator(self):
        theColor = self.colors[random.randint(0,len(self.colors)-1)]

        for i in range(int(self.config["verticalradiator"]["number"])):
            x1, y1 = self.getRandomStartpoint()
        
            x2 = x1 + 100
            y2 = y1  

            for i2 in range(int(self.config["verticalradiator"]["steps"])):
                y1 = y1 + 30
                y2 = y2 + 30
                shape = [x1,y1,x2,y2] 
                self.img.line(shape, fill =theColor, width=10) 
        

    def addVerticalRowOfHoles(self):
        theColor = self.colors[random.randint(0,len(self.colors)-1)]
        for i in range(int(self.config["verticalrowofholes"]["number"])):
            x1, y1 = self.getRandomStartpoint()
        
            x2 = x1 + 10
            y2 = y1 + 10 

            for i2 in range(int(self.config["verticalrowofholes"]["steps"])):
                y1 = y1 + 30
                y2 = y2 + 30
                shape = [x1,y1,x2,y2] 
                self.img.ellipse(shape, fill=theColor)  
    

    def addHorizontalRowOfHoles(self):
        theColor = self.colors[random.randint(0,len(self.colors)-1)]
        for i in range(int(self.config["horizontalrowofholes"]["number"])):
            x1, y1 = self.getRandomStartpoint()
        
            x2 = x1 + 10
            y2 = y1 + 10 

            for i2 in range(int(self.config["horizontalrowofholes"]["steps"])):
                x1 = x1 + 30
                x2 = x2 + 30
                shape = [x1,y1,x2,y2] 
                self.img.ellipse(shape, fill=theColor)  
        


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--config", "-c" , default="config.ini", help="The config file")
    parser.add_argument("--outputfolder", "-o", default=".", help = "The folder where the displacement maps will be saved")
    parser.add_argument("--amount", "-a", default = 1, help="The number of displacements maps to generate")
    
    args = parser.parse_args()
    print("Config file: ", args.config)
    print("Output folder: ", args.outputfolder)
    print("Number of displacement maps to create: ", args.amount)

    config = configparser.ConfigParser()
    config.read(args.config)

    now = datetime.now()

    dis = displacement(config)
    
    for i in range(int(args.amount)):
        dis.newImage()
        dis.addRectangulars()
        dis.addCircle()
        dis.addVertLine()
        dis.addHorLine()
        dis.addHorizontalRadiator()
        dis.addVerticalRadiator()
        dis.addVerticalRowOfHoles()
        dis.addHorizontalRowOfHoles()

        filename = args.outputfolder.rstrip("/") + "/" +  now.strftime("%d-%m-%Y_%H-%M-%S") + "_" + str(i) + ".png"

        dis.saveImageToFile(filename)
        print("File saved ", filename)

    print("Done.")
   