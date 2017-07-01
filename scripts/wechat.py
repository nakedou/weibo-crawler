import requests
from flask.globals import current_app


def send(title, content):
    with current_app.app_context():
        request_url = 'http://sc.ftqq.com/{}.send'.format(current_app.config['WECHAT_KEY'])
        requests.get(request_url, params={'text': title, 'desp': content})
