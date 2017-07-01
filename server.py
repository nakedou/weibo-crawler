from misc import get_project_root
from weibo_crawler import create_app

project_root = get_project_root()
conf_file = '{}/conf/dev.py'.format(project_root)

if __name__ == '__main__':
    app = create_app(conf_file)
    app.run(host='0.0.0.0')
