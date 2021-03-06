import requests
from flask.globals import current_app, session

from weibo_crawler.api import bp


def get_token_from_config():
    try:
        token = current_app.config['token']
    except KeyError:
        return None
    return token


def get_uid_from_session():
    try:
        uid = session['uid']
    except KeyError:
        return None
    return uid


@bp.route('/user-info', methods=['GET'])
def get_user_info():
    token = get_token_from_config()
    uid = get_uid_from_session()
    base_url = 'https://api.weibo.com/2/users/show.json'
    req_url = '{}?access_token={}&uid={}'.format(base_url, token, uid)
    response = requests.get(req_url)
    return response.text


@bp.route('/user-follows', methods=['GET'])
def get_user_follows():
    token = get_token_from_config()
    uid = get_uid_from_session()
    base_url = 'https://api.weibo.com/2/friendships/followers.json'
    req_url = '{}?access_token={}&uid={}&feature=1'.format(base_url, token, uid)
    response = requests.get(req_url)
    return response.text


@bp.route('/user-timeline', methods=['GET'])
def get_user_timeline():
    token = get_token_from_config()
    base_url = 'https://api.weibo.com/2/statuses/user_timeline.json'
    req_url = '{}?access_token={}&feature=1'.format(base_url, token)
    response = requests.get(req_url)
    return response.text


@bp.route('/bilateral-timeline', methods=['GET'])
def get_bilateral_timeline():
    token = get_token_from_config()
    base_url = 'https://api.weibo.com/2/statuses/bilateral_timeline.json'
    req_url = '{}?access_token={}&feature=1'.format(base_url, token)
    response = requests.get(req_url)
    return response.text


@bp.route('/home-timeline', methods=['GET'])
def get_home_timeline():
    token = get_token_from_config()
    base_url = 'https://api.weibo.com/2/statuses/home_timeline.json'
    req_url = '{}?access_token={}&feature=1'.format(base_url, token)
    response = requests.get(req_url)
    return response.text


@bp.route('/public-timeline', methods=['GET'])
def get_public_timeline():
    token = get_token_from_config()
    base_url = 'https://api.weibo.com/2/statuses/public_timeline.json'
    req_url = '{}?access_token={}'.format(base_url, token)
    response = requests.get(req_url)
    return response.text


@bp.route('/timeline-batch', methods=['GET'])
def get_timeline_batch():
    token = get_token_from_config()
    base_url = 'https://api.weibo.com/2/statuses/timeline_batch.json'
    req_url = '{}?access_token={}&uids={}&feature=1'.format(base_url, token, '1727721727')
    response = requests.get(req_url)
    return response.text
