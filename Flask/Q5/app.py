from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/set_session', methods=['POST'])
def set_session():
    user_input = request.form['user_input']
    session['user_data'] = user_input
    return redirect(url_for('display_session'))

@app.route('/display_session')
def display_session():
    user_data = session.get('user_data', 'No data stored in the session.')
    return f'User Data: {user_data}'

@app.route('/clear_session')
def clear_session():
    session.pop('user_data', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
