from flask import Flask, render_template

app = Flask(__name__)

# Custom error handler for 404 - Not Found
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Custom error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

@app.route('/')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)
