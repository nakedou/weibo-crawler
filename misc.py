import os

from invoke.tasks import task

from weibo_crawler import create_app


def get_project_root(path=__file__):
    directory = os.path.dirname(path)

    while directory != '/':
        p = os.path.join(directory, 'requirements.txt')
        if os.path.isfile(p):
            return directory
        else:
            directory = os.path.dirname(directory)

    return None


@task
def server(ctx):
    app = create_app(ctx['conf_file'])
    app.run(host='0.0.0.0', debug=True)
