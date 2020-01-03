import urllib.request
import re

""" Install BeautifulSoup4 on Windows 10/Python3.7
    > py -m pip install beautifulsoup4
"""


""" PRIMERA FORMA """
def get_page():
    open_file = open('scraper.html', 'w')
    html_file = urllib.request.urlopen('https://docs.python.org/3/howto/urllib2.html')
    html_file = html_file.read()

    open_file.write(html_file.decode('utf8'))
    open_file.close()

def get_value():
    open_file = open('scraper.html', 'r')
    regex = '<span class="kn">'
    regex_end = '</span>'

    for line in open_file.readlines():
        sentence = line.strip('\n')
        if regex in sentence:
            initial_pos = sentence.find(regex) + len(regex)
            final_pos = sentence.find(regex_end)
            print(sentence[initial_pos:final_pos])

"""SEGUNDA FORMA"""

def get_page2():
    html_file = urllib.request.urlopen('https://docs.python.org/3/howto/urllib2.html')
    html_file = html_file.read().decode('utf8')
    
    regex = '<span class="kn">(.+?)</span>'

    find_list = re.findall(regex, html_file)
    for item in find_list:
        print(item)



if __name__ == '__main__':
    # get_page()
    # get_value()
    get_page2()

