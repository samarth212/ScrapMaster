import requests
from bs4 import BeautifulSoup

url = input("enter url:")

element = input("enter target element:")
elemFilter = input("filter by:")
if elemFilter == "class" or elemFilter == "id":
    elemName = input("class/id name:")
    

response = requests.get(url)

if response.status_code == 200:
    print("success!")
    soup = BeautifulSoup(response.content, 'html.parser')

    if elemFilter == "class":
        result = soup.find_all(element, class_ = elemName)
    elif elemFilter == "id":
        result = soup.find_all(id=elemName)
    else:
        result = soup.find_all(element)
    print(result)
    

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)