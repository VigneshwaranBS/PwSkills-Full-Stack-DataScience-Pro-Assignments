from flask import Flask, render_template
import requests

app = Flask(__name__)

# Function to fetch data from the "REST Countries" API
def get_external_data():
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)
    data = response.json()
    return data

# Route to display external data
@app.route('/')
def index():
    data = get_external_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
