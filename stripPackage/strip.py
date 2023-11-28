# Name: Matthew Walters, Deborah Tekle, Emma Wilson, Sam Moushey
# Email: waltemw@mail.uc.edu, tekledh@mail.uc.edu, wilso2ek@mail.uc.edu, moushesb@mail.uc.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This is a module where we will strip our given rows in the text file 
# Citations: N/A
# Anything else that's relevant: This is our final! 
# strip.py

from jsonPackage.jsonFunctions import *

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