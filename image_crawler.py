from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import re
import os

textf = open("linksource.txt")
global_count = 0

# Create target directory if don't exist
if not os.path.exists("images"):
    os.mkdir("images")
    print("Directory: images/ created ")
else:
    print("Directory: images/ already exists")


def crawl_snapshot():
    while True:
        url = textf.readline()
        if not url: break
        print('source url:\n\t'+url)

        # get contents from url
        content = requests.get(url).content
        # get soup
        soup = BeautifulSoup(content, 'html.parser')  # choose html.parser
        # find the tag : <img ... >
        image_tags = soup.findAll('img')

        # print out image urls
        print("image source list:\n\t")

        source_list = []
        for image_tag in image_tags:
            print(image_tag.get('src'))
            source_list.append(image_tag.get('src'))

        # download image
        for source in source_list:
            if source.endswith('.gif'):
                continue
            # remove non alphabetical and non numeric character
            file_name = re.sub("[^A-Za-z0-9]*", "", source)
            file_name = file_name[4:]  # remove http string
            urllib.request.urlretrieve(source, 'images/'+file_name+'.jpg')

        print(len(source_list), " images crawled")
        global_count += len(source_list);


def crawl_high_resolution_image():
    while True:
        url = textf.readline()
        if not url: break
        print('source url:\n\t'+url)

        # get contents from url
        content = requests.get(url).content
        # get soup
        soup = BeautifulSoup(content, 'html.parser')  # choose html.parser
        # image_tags= soup.select('div',{"class" : "rg_bx rg_di rg_el ivg-i"})
        a_tags = soup.select('a', {"jsname": "hSRGPd","class":"rg_l"})

        # find the tag : a tag with image link
        print("image source list:\n\t")
        source_list = []
        for a_tag in a_tags:
            print(a_tag)
            # image_content = requests.get(a_tag[0].attrs['href']).content
            # soup = BeautifulSoup(image_content, 'html.parser')
            # img_src = soup.find('img').get('src')
            # file_name = re.sub("[^A-Za-z0-9]*", "", img_src)
            # file_name = file_name[4:]  # remove http string
            # urllib.request.urlretrieve(img_src, 'images/'+file_name+'.jpg')
            # global_count+=1

#crawl_snapshot();
crawl_high_resolution_image();
textf.close();
print("total image count: ",global_count)
