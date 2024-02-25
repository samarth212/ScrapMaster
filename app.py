from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup
import validators

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



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        if not url:
            return redirect(url_for('index', alert='Please enter a URL'))
        elif not validators.url(url): 
            return redirect(url_for('index', alert='Invalid URL. Please enter a valid URL'))
        element = request.form['element']
        elemFilter = request.form['elemFilter']
        elemName = request.form['elemName']
        format = request.form['format']
        return redirect(url_for('result', url=url, element=element, elemFilter=elemFilter, elemName=elemName, format=format))
    else:
        alert = request.args.get('alert')
        return render_template('index.html', alert=alert)       
    
@app.route('/result')
def result():
    url = request.args.get('url')
    element = request.args.get('element')
    elemFilter = request.args.get('elemFilter')
    elemName = request.args.get('elemName')
    format = request.args.get('format')
    scraped_data = scraper(url, element, elemFilter, elemName, format)
    return render_template('result.html', scraped_data=scraped_data)



if __name__ == '__main__':
    app.run(debug=True)
