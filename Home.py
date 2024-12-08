import streamlit as st
import pandas as pd
import displacementmaps
import configparser
from datetime import datetime
import random
import string
import os


if __name__ == "__main__":
    st.set_page_config(layout="wide")

    st.title("Displacement Maps")

    st.write(f"streamlit version: {st.__version__}")


    col1, col2 = st.columns([0.3,0.7], gap="small", vertical_alignment="top")


    
    with col1:
        imageLocation = st.empty()
        if "imagename" in st.session_state and os.path.exists(st.session_state["imagename"]):
            imageLocation.image(st.session_state["imagename"])

        else:
            imageLocation.image("gui.png")

        rectNumber = 0
    
    with col2:

        b1, b2, b3 = st.columns([0.08 , 0.08, 0.9])
        with b1:
            if st.button("Render"):
                config = configparser.ConfigParser()
                config["imagesettings"] = {"width": "500", "height": "500", "numberofcolors": "10"}
                config["rectangulars"] = {"number": st.session_state["26"], "width": st.session_state["27"], "height": st.session_state["28"]}
                config["circles"] = {"number": st.session_state["1"], "width": st.session_state["3"], "height": st.session_state["2"]}
                config["vertlines"] = {"number": st.session_state["4"], "length": st.session_state["5"]}
                config["horlines"] = {"number": st.session_state["6"], "length": st.session_state["7"]}
                config["horizontalradiator"] = {"number": st.session_state["8"], "steps": st.session_state["9"], "distance": st.session_state["10"], "height": st.session_state["11"], "width": st.session_state["12"]}
                config["verticalradiator"] = {"number": st.session_state["13"], "steps": st.session_state["14"], "distance": st.session_state["15"], "height": st.session_state["16"], "width": st.session_state["17"]}
                config["verticalrowofholes"] = {"number": st.session_state["18"], "steps": st.session_state["19"], "distance": st.session_state["20"], "height": st.session_state["21"]}
                config["horizontalrowofholes"] = {"number": st.session_state["22"], "steps": st.session_state["23"], "distance": st.session_state["24"], "height": st.session_state["25"]}

                with open("gui_config.ini", "w") as f:
                    config.write(f)

                dis = displacementmaps.displacement(config)
                dis.newImage()
                dis.addRectangulars()
                dis.addCircle()
                dis.addVertLine()
                dis.addHorLine()
                dis.addHorizontalRadiator()
                dis.addVerticalRadiator()
                dis.addVerticalRowOfHoles()
                dis.addHorizontalRowOfHoles()

                if "imagename" in st.session_state:
                    filename = st.session_state["imagename"]
                else:
                    now = datetime.now()
                    st.session_state["imagename"] = "output/" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=20)) + ".png"
                    filename = st.session_state["imagename"]
                    
                dis.saveImageToFile(filename)
                imageLocation.image(filename)

        with b2:
            if st.button("Reset"):
                st.session_state["26"] = 30
                st.session_state["27"] = 50
                st.session_state["28"] = 50
                st.session_state["1"] = 30
                st.session_state["2"] = 50
                st.session_state["3"] = 50
                st.session_state["4"] = 30
                st.session_state["5"] = 50
                st.session_state["6"] = 30
                st.session_state["7"] = 50
                st.session_state["8"] = 30
                st.session_state["9"] = 30
                st.session_state["10"] = 30
                st.session_state["11"] = 50
                st.session_state["12"] = 50
                st.session_state["13"] = 30
                st.session_state["14"] = 30
                st.session_state["15"] = 30
                st.session_state["16"] = 50
                st.session_state["17"] = 50
        
        with b3:
            if st.button("All to Zero"):
                st.session_state["26"] = 0                
                st.session_state["1"] = 0
                st.session_state["4"] = 0
                st.session_state["6"] = 0
                st.session_state["8"] = 0
                st.session_state["13"] = 0
                st.session_state["18"] = 0
                st.session_state["22"] = 0


        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Rectangulars", "Circles", "Vert. Lines", "Hor. Lines", "Hor. Radiator", "Vert. Radiator", "Vert. Holes", "Hor.Holes"])

        with tab1:
            st.header("Rectangular")

            rectNumber = st.slider("Number of rectangulars: ", 0, 100, value=30, key=26)
            rectHeight = st.slider("Height", 0, 100,value=50, key=27)
            rectWidth = st.slider("Width", 0, 100, value=50, key=28)

        with tab2:
            st.header("Circles")

            cirNumber = st.slider("Number of circles: ", 0, 100, value=30, key=1)
            cirHeight = st.slider("Height", 0, 100, value=50, key=2)
            cirWidth = st.slider("Width", 0, 100, value=50, key=3)
        with tab3:
            st.header("Vertical Lines")
            verlNumber = st.slider("Number of vertical lines: ", 0, 100, value=30, key=4)
            verlHeight = st.slider("Height", 0,  100, value=50, key=5)

        with tab4:
            st.header("Horizontal Lines")
            horlNumber = st.slider("Number of horitontal: ", 0, 100, value=30, key=6)
            horlHeight = st.slider("Height", 0, 100, key=7)
        with tab5:
            st.header("Horizontal Radiator")
            horradNumber = st.slider("Number of horizontal radiators: ", 0, 100, value=30, key=8)
            horradSteps = st.slider("Steps: ", 0, 100, value=30, key=9)
            horradDistance = st.slider("Distance: ", 0, 100, value=30, key=10)
            horradHeight = st.slider("Height", 0, 100, key=11)
            horradWidth = st.slider("Width", 0, 100, key=12)
        with tab6:
            st.header("Vertical Radiator")
            verradNumber = st.slider("Number of vertical radiators: ", 0, 100, value=30, key=13)
            verradSteps = st.slider("Steps: ", 0, 100, value=30, key=14)
            verradDistance = st.slider("Distance: ", 0, 100, value=30, key=15)
            verradHeight = st.slider("Height", 0, 100, key=16)
            verradWidth = st.slider("Width", 0, 100, key=17)
        with tab7:
            st.header("Vertical Lines of Holes")
            verholesNumber = st.slider("Number of horizontal holes per line: ", 0, 100, value=30, key=18)
            verholesSteps = st.slider("Steps: ", 0, 100, value=30, key=19)
            verholesDistance = st.slider("Distance: ", 0, 100, value=30, key=20)
            verholesHeight = st.slider("Diameter", 0, 100, key=21)
        
        with tab8:
            st.header("Horizontal Lines of Holes")
            horholesNumber = st.slider("Number of horizontal holes per line: ", 0, 100, value=30, key=22)
            horholesSteps = st.slider("Steps: ", 0, 100, value=30, key=23)
            horholesDistance = st.slider("Distance: ", 0, 100, value=30, key=24)
            horholesHeight = st.slider("Diameter", 0, 100, key=25)

   
