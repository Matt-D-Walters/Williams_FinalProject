# Name: Matthew Walters, Deborah Tekle, Emma Wilson, Sam Moushey
# Email: waltemw@mail.uc.edu, tekledh@mail.uc.edu, wilso2ek@mail.uc.edu, moushesb@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This is a module where we will load and display an image file
# Citations: N/A
# Anything else that's relevant: This is our final! 
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

