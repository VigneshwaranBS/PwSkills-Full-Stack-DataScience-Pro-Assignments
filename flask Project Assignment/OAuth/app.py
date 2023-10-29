from flask import Flask, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from flask_dance.consumer import oauth_authorized, oauth_error

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Configure Google OAuth
google_bp = make_google_blueprint(client_id='447908045942-hfe9t0dn8dolgu237dbceb52b88a0khv.apps.googleusercontent.com',
                                   client_secret='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',
                                   redirect_to='google_login')
app.register_blueprint(google_bp, url_prefix='/google_login')


@app.route('/')
def home():
    if google.authorized:
        resp = google.get('/plus/v1/people/me')
        assert resp.ok, resp.text
        user_info = resp.json()
        return f'Hello, {user_info["displayName"]} (Google user)'


    return 'Welcome to the Flask OAuth2 Example!'

@app.route('/google-login')
def google_login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
