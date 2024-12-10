## What are Displacement Maps?

Displacement maps are a intelligent way to add three dimensional texture to low poly three dimensional objects. Adding a grey tone bitmap as texture to the object, the different grey tones are interpreted as different heights of parts of the surface:

|     |  |
| -------- | ------- |
| ![Grey tone bitmap](app/static/rectangulars.png) | ![Rendered](/app/static/rectangulars_rendered.png)|
| Grey tone bitmap | Rendered object (Blender)     |

## Quickstart

For creating a displacement map in a 3D software like Blender, you need grey tone bitmaps. These can be created with this litte app: common forms like rectangulars, circles etc. are placed randomly on a bitmap which can then be loaded as texture into a 3D software.

To create your first displacement map, go to the start page and click "Render":

![Grey tone bitmap](app/static/screenshots/sc1.png)

On the left you can see the created grey tone bitmap, maybe its a little bit chaotic becuase it displays too many elements. To start with a blank bitmap, click "All to Zero" which will set all the "Number" sliders of the different forms to zero. Clicking now "Render" again will result in an empty image:

![Grey tone bitmap](app/static/screenshots/sc2.png)

Now, add some rectangulars: on the "Rectangulars" tab below the buttons, forward the slider "Number of rectangulars" to 20 and click "Render" again:

![Grey tone bitmap](app/static/screenshots/sc3.png)

As the rectangulars are placed by a random order and also their color is created randomly, your result will be different than the one above. Nevertheless, you can now save the image (right mouse click) into a "*png" file and use that file as displacement map in your 3D software (here done with Blender):

![Grey tone bitmap](app/static/screenshots/example_rectangulars_rendered.png)

<img src="app/static/screenshots/example_rectangulars_rendered.png" width=200 />