# coding: utf-8
from os.path import join, dirname, pardir, abspath
import subprocess


BOOTSTRAP = abspath(dirname(__file__))
ROOT = abspath(join(BOOTSTRAP, pardir))

# Path where venv will be created. It's imported by bootstrapX.Y.py
VIRTUALENV = abspath(join(BOOTSTRAP, pardir))

ACTIVATE  = join(VIRTUALENV, 'bin', 'activate_this.py')
WITH_VENV = join(BOOTSTRAP, 'with_venv.sh')


def with_venv(*args):
    """
    Runs the given command inside virtualenv.
    """
    cmd = list(args)
    cmd.insert(0, WITH_VENV)
    return subprocess.call(cmd)


def after_install(options, home_dir):
    with_venv('pip', 'install', '-r', join(ROOT, 'requirements.txt'))
    print "Done! Activate your virtualenv: source bin/activate"

