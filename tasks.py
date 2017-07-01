from invoke import Collection

import misc
from misc import get_project_root
from weibo_crawler import create_app

_project_root = get_project_root(__file__)

_conf_file = '{}/conf/dev.py'.format(_project_root)
_app = create_app(_conf_file)

ns = Collection.from_module(misc)
ns.configure({'config': _app.config, 'conf_file': _conf_file, 'project_root': _project_root})
