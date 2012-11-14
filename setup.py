import codecs
import os
from distutils.core import setup

import hipchat as distmeta


if os.path.exists("README.md"):
	long_description = codecs.open("README.md", "r", "utf-8").read()
else:
	long_description = "See http://ryanbalfanz.github.com/django-sendgrid/"

setup(
	name="python-hipchat",
	version=distmeta.__version__,
	description=distmeta.__doc__,
	author=distmeta.__author__,
	author_email=distmeta.__contact__,
	url=distmeta.__homepage__,
	platforms=["any"],
	# license="BSD",
	packages=["hipchat"],
	package_dir={"hipchat": "hipchat"},
	data_files=[],
	scripts=["bin/hc"],
	long_description=long_description,
)
