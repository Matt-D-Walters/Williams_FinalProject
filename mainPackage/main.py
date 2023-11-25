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

#===============================================================================
'''Someone add some comments for our code''' 
#===============================================================================

if __name__ == '__main__':
    location = decryptTextFile(decryptJson())
    print('Location of our picture: '+ location)
    loadImage()
    
    key = 'BQrousuHvfUBm2r6pJ4Q7od6IwoTVyHhnvgOEX3myl8='
    cipher = str(decryptAESjson())
    decrypted_message = decrypt_message(cipher, key)
    print('Our movie is: ' + decrypted_message)
    
    
    
        

    
    
    

        





    

