"""
    @author: Yousaf Hassan
    @desc:  This is an open source scrapper for learning purposes.
    It scraps comments from stackoverflow posts and exports them in csv format.
"""

# Import the request package/library
import requests
# Import the beautiful soup
from bs4 import BeautifulSoup
# Export library
import pandas as pandaExport

# Importing path to handle file already open or exist cases 
import os.path
from os import path
# Lets take a sample URL 
TARGET_URL          =   "https://stackoverflow.com/questions/35860065/saving-users-profile-picture-from-facebook-api-php-sdk-v-5"
OUTPUT_FILE_NAME    =   'stackoverflow-comments.csv'

# Lets handle some expected exceptions
if path.exists(OUTPUT_FILE_NAME):
    try:
        os.rename(OUTPUT_FILE_NAME,OUTPUT_FILE_NAME) # Can't rename an open file so an error will be thrown
        print(F'WARNING: File {OUTPUT_FILE_NAME} already exists. Overwriting...')
    except:
        print('Error! Please close the file in order to generate a new one.')
        exit()

stackoverflowData   =   requests.get(TARGET_URL)
# Using beautiful soup library for parsing fetched data
soup                =   BeautifulSoup(stackoverflowData.text, 'html.parser')
answerComments      =   soup.find_all('div', attrs={'class':'js-comments-container'})
resultSet           =   []
for comment in answerComments:
    commentText     =   comment.find('span', attrs={'class':'comment-copy'})
    if commentText is not None:
        commentText =   commentText.text

    commentUser     =   comment.find('a', attrs={'class':'comment-user'})
    if commentUser is not None:
        commentUser =   commentUser.text
    else:
        commentUser =   ''

    commentUserUrl  =   comment.find('a', attrs={'class':'comment-user'})
    if commentUserUrl is not None:
        commentUserUrl =   'https://stackoverflow.com' + commentUserUrl['href']
    else:
        commentUserUrl =   ''

    commentDate     =   comment.find('span', attrs={'class':'relativetime-clean'})
    if commentDate is not None:
        commentDate =   commentDate.text
    else:
        commentDate =   ''
    resultSet.append((commentText, commentUser, commentUserUrl, commentDate))

dataFrame       =   pandaExport.DataFrame(resultSet, columns=['Comment','User','User Profile Url','Date'])
dataFrame.to_csv(OUTPUT_FILE_NAME, index = False, encoding='utf-8')
print("Data Exported successfully")