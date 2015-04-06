import urllib.request
import os
from sys import argv,exit

def main():

    url = ""
    directory = ""
    
    if len(argv) == 2:
        url = argv[1]
    elif len(argv) == 3:
        directory == argv[2]
        url = argv[3]
    else:
        print("Incorrect format. see README")
        exit(1)
    
    raw_html = urllib.request.urlopen(url).read()
    for string in raw_html:
        print(string)

    # unfinished
