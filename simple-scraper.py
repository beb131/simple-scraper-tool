import requests
from bs4 import BeautifulSoup

url = raw_input('What is the URL you are scraping?\n')

if not 'http' in url:
    url = 'http://' + url

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    selector = raw_input('What CSS Selector are you looking for?\n')

    data = soup.findAll(selector)

    print("\nHere's a list of elements matching the selector '" + selector + "':\n")
    print(data)
else:
    print(response.status_code)
