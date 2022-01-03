import urllib.request, urllib.response, urllib.error
import re


def urlOpen(url):
    try:
        oUrl = urllib.request.urlopen(url)
        return oUrl
    except:
        print('Cannot read this url: ', url)
        quit()


# http://data.pr4e.org/romeo.txt
# http://data.pr4e.org/romeo-full.txt

url = input('Enter the url: ')
oUrl = urlOpen(url)
counter = 0
nline = list()

for line in oUrl:
    words = line.decode().split()
    for word in words:
        for char in word:
            counter += 1
            nline.append(char)
print(nline[:3001])
print(counter)
