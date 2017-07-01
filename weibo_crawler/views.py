from datetime import datetime

from flask.blueprints import Blueprint
from flask.globals import request, current_app
from flask.templating import render_template
from werkzeug.utils import redirect

# from scripts import wechat_server
from scripts import wechat
from weibo_crawler.authorization import get_authorize_url, get_access_token

bp = Blueprint('root', __name__)


@bp.route('/')
def index():
    wechat.send('Sina Weibo Crawler', datetime.now())
    return render_template('index.html', message='Welcome to Sina Weibo Crawler!')


@bp.route('/auth', methods=['GET'])
def auth():
    return redirect(get_authorize_url())


@bp.route('/login', methods=['GET'])
def login():
    auth_code = request.args.get('code')
    access_token = get_access_token(auth_code)
    if access_token is None:
        return 'sorry, the server is gone'
    # wechat_server.run_server()
    current_app.config['token'] = access_token
    return redirect('/')


@bp.route('/logout', methods=['GET'])
def logout():
    uid = request.args.get('uid')
    auth_end = request.args.get('auth_end')
    return render_template('index.html', message='{}, you have logout at {}, bye bye!'.format(uid, auth_end))
