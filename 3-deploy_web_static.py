#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy:
"""
from fabric.api import env, local, put, run
from os.path import exists, isdir
from datetime import datetime

env.hosts = ['54.158.200.125', '54.146.86.109']


def do_pack():
    """a tgz archive generator"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        fn = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fn))
        return fn
    except:
        return None


def do_deploy(archive_path):
    """deploys to the servers"""
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp')
        run('mkdir -p {}{}/'.format(path, ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, ext))
        run('rm -rf {}{}/web_static'.format(path, ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, ext))
        return True
    except OSError as e:
        print(f"Error during deployment: {e}")
        return False
    except fabric.exceptions.NetworkError as e:
        print(f"Network error during deployment: {e}")
        return False


def deploy():
    """send compressed files to the servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
