# Name: Matthew Walters, Deborah Tekle, Emma Wilson, Sam Moushey
# Email: waltemw@mail.uc.edu, tekledh@mail.uc.edu, wilso2ek@mail.uc.edu, moushesb@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This is a module where we will store all of our functions that will be called to in the main
# Citations: N/A
# Anything else that's relevant: This is our final! 
# function.py

import json

def decryptJson():
    '''
    Get our teams key and value pairs that come with it
    @param: none
    @return: the data associated within our 'Williams' key 
    ''' 
    # Read the encrypted JSON file
    with open('EncryptedGroupHints Fall 2023 Section 001.json') as x:
        teamData = json.load(x)['Williams']
    return teamData

def decryptTextFile(teamData):
    '''
    Decrypts english-2.txt by extracting words based on line numbers provided in teamData.
    @param: teamData
    @return: a decrypted string that provides a location where we will take our group picture 
    ''' 
    with open('english-2.txt') as x:
        english_txt = x.read().split() 
    #strip the line numbers that are in teamData by indicies then return our words that are in our teamData list - MW
    decryptedStr = ' '.join(english_txt[int(num)].strip() for num in teamData)
    return decryptedStr

# Need a function to decrypt (TeamsAndEncryptedMessagesForDistribution) AES messages


# Need a function that will load our image 






























    







