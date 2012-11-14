import fabric
from fabric.api import task


@task
def release():
	fabric.operations.local("python setup.py sdist register upload")
