#!/bin/python
#
# mass image downloader for *chans

import subprocess
import os
import urllib.request
import argparse
import time
from html.parser import HTMLParser
from urllib.parse import urlparse
from sys import argv

class Parser4(HTMLParser):
    def __init__(self):
        self.links = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                   base = 'https://media.8ch'
                   if base in value[:len(base)]:
                       self.links.append(value)

class Parser8(HTMLParser):
    def __init__(self):
        self.links = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                   base = 'https://media.8ch'
                   if base in value[:len(base)]:
                       self.links.append(value)

class ParserLain(HTMLParser):
    def __init__(self):
        self.links = []
        self.base = "https://lainchan.org"
        super().__init__()

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
            if len(attrs) > 1 and attrs[1] == ('target','_blank'):
                fragment = attrs[0][1]
                if fragment[:4] != 'http':
                    self.links.append(self.base+fragment)
            #for name, value in attrs:
            #    if name == "target" and value == "_blank":
            #        try:
            #            print(attrs)
            #            self.links.append(value)
            #        except:
            #            pass

class ParserGeneric(HTMLParser):
    def __init__(self):
        self.links = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if 'img' in tag:
            print(tag, attrs)

def main():
    thread = ""
    directory = c_time = time.strftime("%H%M%S")
    i = 0
    while os.path.isdir(c_time):
        directory = c_time + '_' + i
    info = "image downloader for 4chan, 8chan, and lainchan"
    parser = argparse.ArgumentParser(description=info)
    parser.add_argument('-d', '--directory',
                        help='directory for the images',
                        action='store')
    parser.add_argument('thread',
                        help='directory for the images',
                        action='store')
    args = parser.parse_args()
    thread = args.thread
    if args.directory:
        directory = args.directory
        print("Found directory: ", directory)
    links = parse(thread)
    download(links, directory)

def parse(thread):
    "parse and return list of links"
    parser = None
    parsed_uri = urlparse(thread)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    if "lainchan" in domain:
        print("using Lainchan parser")
        parser = ParserLain()
    elif "8ch" in domain:
        print("using 8chan parser")
        parser = Parser8()
    elif "4chan" in domain:
        print("using 4chan parser")
        parser = Parser4()
    else:
        print("Unknown thread. Using generic parser")
        parser = ParserGeneric()
    page = proper_request(thread)
    parser.feed(str(page))
    return parser.links

def download(links, directory):
    for url in links:
        print("Downloading " + url + " to " + directory)
        # DEBUGGING. UNCOMMENT LATER
        # subprocess.call(["wget","-q","-P",directory,url])
        
def proper_request(url):
    "spoofs agent, as to not be declined by the site"
    print("Requesting HTML... ")
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    if data:
        print("Recieved response")
    return data

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard Interupt found. Exiting...")
        exit()
