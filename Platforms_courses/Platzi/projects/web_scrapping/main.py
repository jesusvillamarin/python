import requests
from bs4 import BeautifulSoup
import urllib
import sys
import getopt
import time
import schedule
import os
import shutil


URL = 'https://xkcd.com/'
DOWNLOAD_FOLDER = './downloads/'
MAX_IMAGES = 1
CLEAR_FOLDER = False
INDEX_TO_START = 1


def find_image(markup_content = None):
    if markup_content is None: raise ValueError('The request response not should be None')

    soup = BeautifulSoup(markup=markup_content, features='html.parser')

    comic_container = soup.find(name='div', attrs= {'id': 'comic'}) # The find method return a bs4.element.Tag
    img_tag = comic_container.find('img') # the find method is part of bs4 module
    # print(type(img_tag))

    img_url = 'https:' + img_tag.get('src')
    img_title = img_tag.get('title')
    img_name = img_url.split('/')[-1]

    return img_name, img_url, soup.title.string

def get_argv():
    argsv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argsv,'d', ['max-images=', 'path-folder=', 'clear-folder', 'start-from='])
        for key, value in opts:
            if key == '--max-images':
                global MAX_IMAGES
                MAX_IMAGES = int(value)
            elif key == '--path-folder':
                global DOWNLOAD_FOLDER
                DOWNLOAD_FOLDER = value
            elif key == '--clear-folder':
                global CLEAR_FOLDER
                CLEAR_FOLDER = True
            elif key == '--start-from':
                global INDEX_TO_START
                MAX_IMAGES = int(MAX_IMAGES+int(value))
                INDEX_TO_START = int(value)
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        sys.exit(2)


def initalize_var_and_directory():
    """
        Method that creates a directory to place downloaded images
    """
    get_argv()
    if CLEAR_FOLDER:
        try:
            shutil.rmtree(DOWNLOAD_FOLDER)
        except FileNotFoundError as err:
            print('The directory {} not exists in path, but don\'t worry, we will create for you'.format(DOWNLOAD_FOLDER.split('\\')[-1]))
    # how validate if a folder exist on path 
        # if not os.path.exists(DOWNLOAD_FOLDER): ...
    try:
        os.mkdir(DOWNLOAD_FOLDER)
    except FileExistsError as err:
        print(err)


def move_downloads(*args):
    img_name, img_url, page_title = args
    print(img_url)
    print(f'Downloading image from {page_title}...')
    if not os.path.exists('{}\{}'.format(DOWNLOAD_FOLDER, img_name)):
        urllib.request.urlretrieve(img_url, img_name) # To Download the image
        shutil.move(img_name, DOWNLOAD_FOLDER)



def run():
    """
        This method download all image from https://xkcd.com
    """
    initalize_var_and_directory()
    for i in range(INDEX_TO_START, MAX_IMAGES+1):
        response = requests.get(URL + str(i))
        if response.status_code == 200:
            try:
                img_name, img_url, page_title = find_image(markup_content= response.content)
            except ValueError as e:
                print(e)
            else:
                move_downloads(img_name, img_url, page_title)
            finally:
                pass
        else:
            print(response.status_code)
    print('Download completed')

if __name__ == '__main__':
    run()
