# Name: Matthew Walters, Deborah Tekle, Emma Wilson, Sam Moushey
# Email: waltemw@mail.uc.edu, tekledh@mail.uc.edu, wilso2ek@mail.uc.edu, moushesb@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This is a module where we will store all of our decryption for the json files & the text file
# Citations: N/A
# Anything else that's relevant: This is our final! 
# function.py

import json

def decryptJson():
    '''
    Get our teams key and value pairs that come with it from EncryptedGroupHint Fall 2023 json -MW
    @param: none
    @return: the values associated within our 'Williams' key 
    ''' 
    # Read the encrypted JSON file
    with open('EncryptedGroupHints Fall 2023 Section 001.json') as x:
        teamData = json.load(x)['Williams']
    return teamData

def stripTextFile(teamData):
    '''
    strips english-2.txt by extracting words based on line numbers provided in teamData. -MW
    @param: teamData
    @return: a decrypted string that provides a location where we will take our group picture 
    ''' 
    with open('english-2.txt') as x:
        english_txt = x.read().split() 
    #strip the line numbers that are in teamData by indicies then return our words that are in our teamData list - MW
    stripedStr = ' '.join(english_txt[int(num)].strip() for num in teamData)
    return stripedStr


def getAESString():
    '''
    Get our teams AES string from the TeamsAndEncryptedMessagesForDistribution 
    @param: none
    @return: the data associated within our 'Williams' dictionary key 
    ''' 
    # Read the encrypted JSON file
    with open('TeamsAndEncryptedMessagesForDistribution.json') as x:
        AESWilliams = json.load(x)['Williams']
    return AESWilliams






























    







