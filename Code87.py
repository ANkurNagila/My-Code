# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
count=int(input("Enter count:"))
position=int(input("Enter position:"))
print("Retrieving:",url)
while count!=0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    p=0
    for tag in tags:
        p+=1
        if p==position:
            url=tag.get("href",None)
            print("Retrieving:",tag.get("href",None))
            break

    count=count-1
    if count==0:
        print(tag.contents[0])
