import time
from datetime import datetime, timedelta
import os
from fabric.api import *
from contextlib import contextmanager as _contextmanager
from punn_it import local_settings as settings

env.use_ssh_config= True
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

"""
This should be in ~/.ssh/config

Host cdc-prod
    User root
    Hostname 66.175.208.206

Host cdc-dev
    User root
    Hostname 50.116.51.59

"""

@task
def dev():
    """
    Initialize staging environment variables
    """
    env.hosts = ['cdc-dev']
    env.directory = '/home/web/punn.it'
    env.project_root = os.path.join(env.directory, "punn_it")
    env.gunicorn_name = "punn_it"

@task
def prod():
    """
    Initialize staging environment variables
    """
    env.hosts = ['cdc-prod']
    env.directory = '/home/web/punn.it'
    env.project_root = os.path.join(env.directory, "punn_it")
    env.gunicorn_name = "punn_it"


@_contextmanager
def virtualenv():
    env.activate = 'source %s/bin/activate' % env.directory
    with cd(env.project_root):
        with prefix(env.activate):
            yield


@task
def get_db():
    """
    Will fetch the remote datase and load it localy, according to the project's local_settings.py

    TODO : add support for POSTGRES
    """
    msg = prompt("Are you sure you want to replace content of local database with the database from '%s'?" % env.hosts[0], default="y/n")
    if msg == "y":
        if settings.DATABASES['default']['ENGINE'] == "django.db.backends.mysql":
            get_mysql_db()
        else:
            raise Exception("Database engine not supported")


@task
def get_mysql_db():
    """
    Will fetch a mysql db
    """
    filename= time.strftime('%Y%m%d-%H%M%S')
    #dump remote file
    with virtualenv():
        run('python manage.py dbdump --compress=gzip --destination=/tmp --filename=%s.sql' % filename)
    #fetch the file
    get('/tmp/%s.sql.gz' % filename, '/tmp/%s.sql.gz' % filename)

    #load sql
    local('gunzip < /tmp/%(filename)s.sql.gz | mysql -u %(user)s -h %(host)s -p%(password)s %(database)s' % {
        'user' : settings.DATABASES['default']['USER'],
        'password' : settings.DATABASES['default']['PASSWORD'],
        'host' : settings.DATABASES['default']['HOST'],
        'password' : settings.DATABASES['default']['PASSWORD'],
        'database' : settings.DATABASES['default']['NAME'],
        'filename' : filename,
    })


@task
def get_all_media():
    """
    will fetch the media for remote project using rsync
    """
    remote_dir = os.path.join(env.project_root, "media")
    local_dir = os.path.join(PROJECT_DIR, "punn_it", "media")
    local("rsync -ave ssh root@%(host)s:/%(remote_dir)s/ %(local_dir)s/ --exclude \"cache\"" % {
        'host' : env.host,
        'remote_dir' : remote_dir,
        'local_dir' : local_dir,
    })


@task
def get_recent_media():
    """
    will fetch the media for remote project using rsync
    """
    remote_dir = os.path.join(env.project_root, "media")
    local_dir = os.path.join(PROJECT_DIR, "punn_it", "media")
    run("touch -d '%s' timestampfile" % (datetime.now()-timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'))
    local('ssh root@%(host)s "find %(remote_dir)s -maxdepth 1 -newer timestampfile -print0"  | rsync -av  --no-relative --files-from=- root@%(host)s:/  %(local_dir)s' % {
        'host' : env.host,
        'local_dir' : local_dir,
        'remote_dir' : remote_dir,
        
    })


@task
def update_local():
    """
    Will fetch db and media
    """
    execute(get_db)
    execute(get_recent_media)


@task
def deploy():
    """
    Deploys the current project : hg push, hg update, manage.py collectstatic, manage.py migrate and restart gunicorn
    """
    local("git push")

    with cd(env.project_root):
        run("git rev-parse HEAD")
        run("git pull")
    with virtualenv():
        with cd(env.directory):
            run('pip install -r requirements.txt')

        run('python manage.py collectstatic')
        run('python manage.py migrate')
        run('supervisorctl restart %s' % env.gunicorn_name)





