import requests
from bs4 import BeautifulSoup

url = 'https://samarthkol.com'

response = requests.get(url)

if response.status_code == 200:
    pass
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)