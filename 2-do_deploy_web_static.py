#!/usr/bin/python3
""" distributes an archive to your web servers, using the function """

from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['54.198.184.242', '35.190.181.149']
env.user = "ubuntu"


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
        print("New version deployed!")
        return True
    except:
        return False
