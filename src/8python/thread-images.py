#!/bin/python
#
# mass image downloader for *chans

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
        if 
        print(tag,attrs)

class Parser8(HTMLParser):
    def __init__(self):
        self.links = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        print(tag,attrs)

class ParserLain(HTMLParser):
    def __init__(self):
        self.links = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        print(tag,attrs)

class ParserGeneric(HTMLParser):
    def __init__(self):
        self.links = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        print(tag,attrs)

def main(argv):
    thread = ""
    directory = time.strftime("%H%M%S")
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
    parse(directory, thread)

def parse(directory, thread):
    "parse and download"
    parser = None
    parsed_uri = urlparse(thread)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    if "lainchan" in domain:
        parser = ParserLain()
    elif "8ch" in domain:
        parser = Parser8()
    elif "4chan" in domain:
        parser = Parser4()
    else:
        parser = ParserGeneric()
    try:
        print(thread)
        page = proper_request(thread)
        parser.feed(str(page.decode('utf-8')))
    except Exception as e:
        print("An exception has occurred: ", e.value)
        
def proper_request(url):
    "spoofs agent, as to not be declined by the site"
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data

if __name__ == '__main__':
    main(argv)
