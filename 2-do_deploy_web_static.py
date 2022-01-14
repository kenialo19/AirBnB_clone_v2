#!/usr/bin/python3
""" Write a Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack."""

from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['54.198.184.242', '35.190.181.149']


def do_deploy(archive_path):
    """ Deploy the file in specific folders in the servers """
    if path.isfile(archive_path) is False:
        return False
    filetgz = archive_path.split("/")[-1]
    filename = filetgz.replace('.tgz', '')

    newdir = "/data/web_static/releases/" + filename

    try:
        put(archive_path, "/tmp/")
        run("mkdir {}/".format(newdir))
        run("tar -xzf /tmp/{} -C {}/".format(filetgz, newdir))
        run("rm /tmp/{}".format(filetgz))
        run("mv {}/web_static/* {}/".format(newdir, newdir))
        run("rm -rf {}/web_static".format(newdir))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(newdir))
        return True
    except:
        return False
