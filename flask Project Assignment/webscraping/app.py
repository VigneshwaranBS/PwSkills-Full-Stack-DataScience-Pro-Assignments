from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Web scraping function
def scrape_quotes():
    url = 'http://quotes.toscrape.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []

    for quote in soup.find_all('span', class_='text'):
        quotes.append(quote.get_text())

    return quotes

# Route to display scraped quotes
@app.route('/')
def index():
    quotes = scrape_quotes()
    return render_template('index.html', quotes=quotes)

if __name__ == '__main__':
    app.run(debug=True)
