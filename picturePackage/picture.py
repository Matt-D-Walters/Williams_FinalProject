#===============================================================================
'''Someone add our documentation''' 
#===============================================================================

#picture.py

from PIL import Image
#===============================================================================
'''Someone add the correct documentation for a function''' 
#===============================================================================


def loadImage():
    try:
        with Image.open('WilliamsGroupPicture.jpeg') as img:
            picture = img.show()
            return picture         
    except FileNotFoundError:
        print('Image not found')

