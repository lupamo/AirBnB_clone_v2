#!/usr/bin/python3
"""
a script that distributes an archive to your web servers,
using the function do_deploy
"""

from datetime import datetime
import os
from fabric.api import env
from fabric.api import put
from fabric.api import run


"""web-01, web-02 IPs"""
env.hosts = ['54.158.200.125', '54.146.86.109']


def do_deploy(archive_path):
    """
    deploys archive files to the webservers
    """
    if not os.path.exists(archive_path):
        return False
    fn = archive_path.split('/')[-1]
    comp_file = '/data/web_static/releases/' + "{}".format(fn.split('.')[0])
    tmp = "/tmp/" + fn

    try:
        """uploading archive file to tmp folder on server"""
        put(archive_path, "/tmp/")
        """
        uncompress the file to the
        /data/web_static/releases on the server
        """
        run("mkdir -p {}/".format(comp_file))
        run("tar -xzf {} -C {}/".format(tmp, comp_file))
        run("mv {}/web_static/* {}/".format(comp_file, comp_file))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data//web_static/current".format(comp_file))
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
