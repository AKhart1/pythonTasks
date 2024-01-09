import requests
from bs4 import BeautifulSoup
def webScraper(site):
    try:
        response = requests.get(site)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f'Headlines from website:')
        headlines = soup.find_all('h2')

        for headline in headlines:
            print(headline.text.strip())

    except Exception as ex:
        print(f"An error occured: {ex}")

webScraper('https://www.bbc.com/news')