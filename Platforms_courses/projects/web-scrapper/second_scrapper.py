from bs4 import BeautifulSoup
import requests

# WARNING: The script chardetect.exe is installed in
# 'C:\Users\jvill\AppData\Local\Programs\Python\Python37-32\Scripts' which is not on PATH.
# Consider adding this directory to PATH or,
# if you prefer to suppress this warning, use --no-warn-script-location.


GOOGLE_NEWS_URL = 'https://news.google.com/?hl=es-419&gl=MX&ceid=MX:es-419'
def scrapping_site():
    re = requests.get(GOOGLE_NEWS_URL)
    if (re.status_code):
        soup = BeautifulSoup(re.text, 'html.parser')
        if soup is not None:
            news = soup.find_all('h3', {'class' : 'ipQwMb ekueJc RD0gLb'})
            for new in news:
                title_new = new.find('a', {'class' : 'DY5T1d'}).getText()
                url = new.find('a').get('href')
                print(title_new, ' ', url)


if __name__ == '__main__':
    scrapping_site()