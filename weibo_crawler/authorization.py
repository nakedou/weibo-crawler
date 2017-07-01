import requests
from flask.globals import current_app


def get_authorize_url():
    with current_app.app_context():
        auth_url = 'https://api.weibo.com/oauth2/authorize'
        return '{}?client_id={}&redirect_uri={}'\
            .format(auth_url, current_app.config['CLIENT_ID'], current_app.config['CALLBACK_URL'])


def get_access_token(code):
    with current_app.app_context():
        access_token_url = 'https://api.weibo.com/oauth2/access_token'
        response = requests.post(access_token_url,
                                 data={
                                     'client_id': current_app.config['CLIENT_ID'],
                                     'client_secret': current_app.config['CLIENT_SECRET'],
                                     'grant_type': 'authorization_code',
                                     'code': code,
                                     'redirect_uri': current_app.config['CALLBACK_URL']
                                 })

        if response.status_code != 200:
            return None

        return response.json().get('access_token')
