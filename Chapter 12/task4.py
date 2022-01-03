from bs4 import BeautifulSoup
import urllib.request


def urlOpen(url):
    try:
        return urllib.request.urlopen(url)
    except:
        print('Cannot read this url: ', url)
        quit()


url = input('Enter the url: ')
tag = input('Enter the tag: ')
html_doc = urlOpen(url)

soup = BeautifulSoup(html_doc, 'html.parser')
print(f"Number of <{tag}> tags: ", len(soup.find_all(tag)))
