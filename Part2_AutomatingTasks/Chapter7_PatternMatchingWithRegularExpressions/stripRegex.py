#! python3

#stripRegex.py - Regex Version of the strip()

import re

def regex_strip(text, char=None):
    
    if not char:
        strip_left = re.compile(r'^\s +') #string starting with whitespace
        strip_right = re.compile(r'\s+$') #string ending with whitespace

        s = re.sub(strip_left, "", text) #replacing strip_left with "" in string s
        s = re.sub(strip_right, "", text) #replacing strip_right with "" in string s

    else:
        strip_char = re.compile(char)
        text = re.sub(strip_char, "", text)
    return text

if __name__ == '__main__':
    string_to_be_stripped = input("Enter string to be stripped: ")
    char_to_be_removed = input("Enter character to be removed, if none press enter: ")
    print(regex_strip(string_to_be_stripped, char_to_be_removed))
    
