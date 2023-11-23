#===============================================================================
'''Someone add our documentation''' 
#===============================================================================


#aesDecrypt.py
#===============================================================================
'''This is works however, I think we need a better way of inputing the cipher instead of it being a string.
We get the cipher from the decryptAESjson in jsonFunctions Package. 
It returns the cipher value associated with the key "'Williams'" - our group

So someone should figure out a way to call that for the cipher instead of manual inputing the string.''' 

#===============================================================================




from cryptography.fernet import Fernet

# Add function documentation

def decrypt_message(cipher, key):
    x = Fernet(key)
    decrypt = x.decrypt(cipher.encode()).decode()
    
    return decrypt
cipher = 'gAAAAABlTNM6TGjW5Tsw2sZviokTYGpyIdV0Fet4EaopCXrk5DRnFGjYqqtVXfqx7h6OjBFeWNIkn0fvVnBETa3CkoZpR5NDLQ==' 
key = 'BQrousuHvfUBm2r6pJ4Q7od6IwoTVyHhnvgOEX3myl8='  
        
        
decrypted_message = decrypt_message(cipher, key)
        
