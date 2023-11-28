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


#This function loads the image and prints it to the main
def loadImage():
    try:
        # Open the image file using the Pillow library
        with Image.open('WilliamsGroupPicture.jpeg') as img:
            # Display the image
            picture = img.show()
            #Returning the show() result
            return picture         
    except FileNotFoundError:
         # Handle the case where the image file is not found
        print('Image not found')

