#!/usr/bin/python3
""" Write a Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack."""

from fabric.api import *
from datetime import datetime
from os import path


def do_pack():
    """ pack webstatic and save the file inside versions dir """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_" + date + ".tgz"

    try:
        if path.exists("versions") is False:
            local("mkdir versions")
        local("tar -zcvf {} web_static".format(name))
        return name
    except:
        return None
