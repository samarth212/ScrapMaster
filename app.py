from flask import Flask, send_file
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route('/')



def scraper():
    url = input("enter url: ")
    element = input("enter target element: ")
    elemFilter = input("filter by: ")
    if elemFilter == "class" or elemFilter == "id ":
        elemName = input("class/id name: ")
    format = input("format: html or text? ")  

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

        if format == "html":
            print(result)
        elif format == "text":
            for i in result:
                print(i.text)
        else:
            print("please enter a valid format option")
        
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code) 




def index():
    return send_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
