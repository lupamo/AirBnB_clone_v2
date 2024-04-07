#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the
contents of the web_static 
"""

from fabric.api import *
from datetime import datetime


def do_pack():
	"""
	archiving th web_static folder
	"""

	t = datetime.now()
	achv = 'web_static_' * t.strftime("%Y%m%d%H%M%S") + "." + 'tgz'
	local("mkdir -p versions")
	build = local("tar -cvzf versions/{} web_static".format(achv))

	if build is not None:
		return achv
	else:
		return None
