# Name: Matthew Walters, Deborah Tekle, Emma Wilson, Sam Moushey
# Email: waltemw@mail.uc.edu, tekledh@mail.uc.edu, wilso2ek@mail.uc.edu, moushesb@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This is a module where we will use Fernet to decrypt a message using a shared key
# Citations: https://cryptography.io/en/latest/fernet/ - used to help decrypt using Fernet
# Anything else that's relevant: This is our final! 
#aesDecrypt.py


from cryptography.fernet import Fernet
from jsonPackage.jsonFunctions import *  # This import the decryptAESjson function


def decrypt_message(cipher, key):
    '''
    This function uses the Fernet module to decrypt our AES string.
    @param: Our team's AES cipher
    @param: Our team's decryption key
    @return: The movie title 
    ''' 
    # Create a Fernet object with the provided key
    x = Fernet(key)
    #Decrypt the cipher (which is expected to be a string), encode the result, and then decode it to a string
    decrypt = x.decrypt(cipher.encode()).decode()
    # Returns the decrypted message
    return decrypt

