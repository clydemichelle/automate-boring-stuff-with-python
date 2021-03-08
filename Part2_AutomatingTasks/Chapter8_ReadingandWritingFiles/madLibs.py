#! python3

""" madLibs.py - Creates a file that user substitutes adjective,noun, adverb or verb
               with respective user input """

#Import necessary modules 
import re

#Display contents of original file to user to user
originalFile = open('originalFile.txt')
print('This is the original text replace the text in uppercase with appropriate words')
content = originalFile.read()
print(content)


#Loop through the content and replace the words using regex to find which characters will be replaced
replaceRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
for token in replaceRegex.findall(content):
    word = input('Enter a/an ' + token.lower() + ': ')
    content = content.replace(token, word, 1)

print('Content after your input:\n ' + content)
madLibsFile = open('madLibsFile.txt','w')
madLibsFile.write(content)

originalFile.close()
madLibsFile.close()

    

    
        
        

