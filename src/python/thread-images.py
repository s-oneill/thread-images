#!/usr/bin/python

import urllib.request
import os
import time
from sys import argv,exit

IMG_MARKER = "href=\"//i.4cdn.org/"
URL_START  = "\"//";

def extractURL(str_input):
    extracted_url = ""
    index = str_input.find(URL_START) + len(URL_START);
    for i in range(index, len(str_input) - 1):
        extracted_url += (str_input[i])
    return extracted_url

def dupe(str_input, imgs):
    for i in range(0,len(imgs)):
        if (str_input == imgs[i]):
            return true
    return False

def process(fragment, imgs):
    if IMG_MARKER in fragment:
        if not dupe(fragment,imgs):
            imgs.append(extractURL(fragment))

def main():

    url = ""
    directory = ""
    imgs = []

    if len(argv) == 2:
        url = argv[1]
        directory = time.strftime("%H:%M:%S")
    elif len(argv) == 3:
        directory == argv[2]
        url = argv[3]
    else:
        print("Incorrect format. see README")
        exit(1)
    
    html = urllib.request.urlopen(url).read().decode().split()
    for fragment in html:
        if IMG_MARKER in fragment:
            process(fragment,imgs)
    
    print(imgs)

if __name__ == "__main__":
    main()
