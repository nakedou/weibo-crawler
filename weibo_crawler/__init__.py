import os

from flask import Flask


def _register_blueprints(app):
    from weibo_crawler.views import bp as root
    from weibo_crawler.api import bp as api

    app.register_blueprint(root, url_prefix=None)
    app.register_blueprint(api, url_prefix='/api')


def create_app(conf_file=None):
    app = Flask(__name__)
    if conf_file:
        app.config.from_pyfile(conf_file)
    elif os.environ.get('CONF') is not None:
        app.config.from_envvar('CONF')

    _register_blueprints(app)
    return app
