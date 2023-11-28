# Name: Matthew Walters, Deborah Tekle, Emma Wilson, Sam Moushey
# Email: waltemw@mail.uc.edu, tekledh@mail.uc.edu, wilso2ek@mail.uc.edu, moushesb@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This is us being Python experts to solve a scavenger hunt  
# Citations: N/A
# Anything else that's relevant: 
# main.py
from jsonPackage.jsonFunctions import *
from aesPackage.aesDecrypt import *
from picturePackage.picture import *


if __name__ == '__main__':
    # Decrypt the JSON file and retrieve the location
    location = stripTextFile(decryptJson())
    # Print the location of the picture
    print('Location of our picture: '+ location)
    
    
    # Set the key for AES decryption
    key = 'BQrousuHvfUBm2r6pJ4Q7od6IwoTVyHhnvgOEX3myl8='
    #Decrypt the AES-encrypted message from the JSON file
    cipher = str(getAESString())
    decrypted_message = decrypt_message(cipher, key)
    #Print the decrypted movie name
    print('Our movie is: ' + decrypted_message)
    
    
    #Load and display the image
    loadImage()
    
    
        

    
    
    

        





    

