import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('https://imagevars.gulfnews.com/2019/08/22/India-Economy-lead_16cb9c8b639_large.jpg').read()
fhand = open('D:/cover3.jpg', 'wb')
fhand.write(img)
fhand.close()


