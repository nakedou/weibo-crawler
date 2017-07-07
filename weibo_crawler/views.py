from datetime import datetime

from flask.blueprints import Blueprint
from flask.globals import request, current_app
from flask.templating import render_template
from werkzeug.utils import redirect

# from scripts import wechat_server
from scripts import wechat
from weibo_crawler.api.weibo import get_uid_from_config
from weibo_crawler.authorization import get_authorize_url, get_access_token, get_access_uid

bp = Blueprint('root', __name__)


@bp.route('/')
def index():
    uid = get_uid_from_config()
    if uid is None:
        msg = datetime.now()
    else:
        msg = '{} --- visit at --- {}'.format(uid, datetime.now())
    wechat.send('Weibo Crawler', msg)
    return render_template('index.html', uid=uid, message='Welcome to Sina Weibo Crawler!')


@bp.route('/auth', methods=['GET'])
def auth():
    return redirect(get_authorize_url())


@bp.route('/login', methods=['GET'])
def login():
    auth_code = request.args.get('code')
    access_token = get_access_token(auth_code)
    if access_token is None:
        return 'oh my god, the server is going to die...'
    # wechat_server.run_server()
    uid = get_access_uid(access_token)
    current_app.config['token'] = access_token
    current_app.config['uid'] = uid
    return redirect('/')


@bp.route('/logout', methods=['GET'])
def logout():
    uid = request.args.get('uid')
    auth_end = request.args.get('auth_end')
    return render_template('index.html', message='{}, you have logout at {}, bye bye!'.format(uid, auth_end))
