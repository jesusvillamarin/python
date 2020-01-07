import requests
from bs4 import BeautifulSoup
import urllib
import sys
import getopt

URL = 'https://xkcd.com/'
max_images = 1

def run(max_images):
    """
        This method download all image from https://xkcd.com
    """
    for i in range(1, max_images+1):
        response = requests.get(URL + str(i))
        if response.status_code == 200:
            soup = BeautifulSoup(markup=response.content, features='html.parser')
            print(f'The page title: {soup.title.string}')
            comic_container = soup.find(name='div', attrs= {'id': 'comic'}) # The find method return a bs4.element.Tag
            img_tag = comic_container.find('img') # the find method is part of bs4 module
            # print(type(img_tag))

            img_url = 'https:' + img_tag.get('src')
            img_title = img_tag.get('title')
            img_name = img_url.split('/')[-1]
            urllib.request.urlretrieve(img_url, img_name) # To Download the image

            print(f'The URL for {img_title} is: {img_url}')

        else:
            print(response.status_code)

if __name__ == '__main__':
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args,'', ['max-images='])
        for key, value in opts:
            if key == '--max-images':
                max_images = int(value)

    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        sys.exit(2)

    run(max_images=max_images)

