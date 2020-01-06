from bs4 import BeautifulSoup
import requests
import urllib.request
import time
textf = open("linksource.txt")
url = textf.read()
print('source url:\n\t'+url)

# get contents from url
content = requests.get(url).content
# get soup
soup = BeautifulSoup(content,'lxml') # choose lxml parser
# find the tag : <img ... >
image_tags = soup.findAll('img')
# print out image urls
print("image source list")
for image_tag in image_tags:
    print(image_tag.get('src'))

# download image
for image_tag in image_tags:
    urllib.request.urlretrieve(image_tag.get('src'), str(time.time())+'.jpg')