import os
from flask import Flask, render_template, session, redirect, url_for, request

try:
    import msal
except ImportError:  # pragma: no cover
    msal = None

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET', 'change_me')

CLIENT_ID = os.getenv('AZURE_CLIENT_ID')
CLIENT_SECRET = os.getenv('AZURE_CLIENT_SECRET')
AUTHORITY = os.getenv('AZURE_AUTHORITY', 'https://login.microsoftonline.com/common')
REDIRECT_PATH = os.getenv('AZURE_REDIRECT_PATH', '/getAToken')
SCOPE = ['User.Read']


def _build_msal_app(cache=None, authority=None):
    if not msal:
        raise RuntimeError('MSAL library is not installed')
    return msal.ConfidentialClientApplication(
        CLIENT_ID, authority=authority or AUTHORITY,
        client_credential=CLIENT_SECRET, token_cache=cache)


def _build_auth_url():
    return _build_msal_app().get_authorization_request_url(
        SCOPE,
        redirect_uri=url_for('authorized', _external=True))


@app.route('/')
def hello_world():
    pod_name = os.getenv('HOSTNAME', 'localhost')
    user = session.get('user')
    return render_template('index.html', title='Hello from flask in kubernetes', pod_name=pod_name, user=user)


@app.route('/login')
def login():
    if not msal or not CLIENT_ID or not CLIENT_SECRET:
        return 'Azure AD authentication is not configured.', 500
    return redirect(_build_auth_url())


@app.route(REDIRECT_PATH)
def authorized():
    if 'code' in request.args:
        result = _build_msal_app().acquire_token_by_authorization_code(
            request.args['code'],
            scopes=SCOPE,
            redirect_uri=url_for('authorized', _external=True))
        if 'error' in result:
            return result.get('error_description'), 500
        session['user'] = result.get('id_token_claims')
    return redirect(url_for('hello_world'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(
        'https://login.microsoftonline.com/common/oauth2/v2.0/logout?post_logout_redirect_uri='
        + url_for('hello_world', _external=True))
