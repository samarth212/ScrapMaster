from flask import Flask, send_file
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def scraper(url, element, elemFilter, elemName, format):
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
            return result
        elif format == "text":
            for i in result:
                return '\n'.join([i.text for i in result])
        else:
            return "please enter a valid format option"
        
    else:
        return "Failed to retrieve the webpage. Status code: " + str(response.status_code) 



@app.route('/')
def index():
    return send_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
