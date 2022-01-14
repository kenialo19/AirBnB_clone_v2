#!/usr/bin/python3
""" Write a Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack."""


from ast import Try
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['54.198.184.242', '35.190.181.149']

def do_pack():
    """ pack webstatic and save the file inside versions dir """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        name = "versions/web_static_" + date + ".tgz"
        return name
    except:
        return None

def do_deploy(archive_path):
    """ Deploy the file in specific folders in the servers """
  
    try:
        newdir = "/data/web_static/releases/"
        filetgz = archive_path.split("/")[-1]
        filename = filetgz.replace('.tgz', '')
        put(archive_path, "/tmp/")
        run("mkdir {}/".format(newdir, filename))
        run("tar -xzf /tmp/{} -C {}/".format(filetgz, newdir))
        run("rm /tmp/{}".format(filetgz))
        run("mv {}/web_static/* {}/".format(newdir, filename, newdir, filename))
        run("rm -rf {}/web_static".format(newdir, filename))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(newdir, filename))
        return True
    except:
        return False
