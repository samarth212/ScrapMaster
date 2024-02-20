import requests
from bs4 import BeautifulSoup

url = input("enter url:")
element = input("enter target element:")

response = requests.get(url)

if response.status_code == 200:
    print("success!")
    soup = BeautifulSoup(response.content, 'html.parser')

    result = soup.find_all(element)
    print(result)

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)