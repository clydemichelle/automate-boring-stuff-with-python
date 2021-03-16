#! python3

""" socialOpener.py - Launches all social sites at a go
                      from a .txt file with various links """

import webbrowser

fhandle = open('socialMediaSites.txt')

for line in fhandle:
    line.rstrip()
    #print(line)
    pos = line.find('h')
    url = line [pos:]
    #print(pos)
    print(url)

    webbrowser.open(url)
