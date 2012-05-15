# coding: utf-8
from os.path import join, dirname, pardir
import subprocess


BOOTSTRAP = dirname(__file__)
ROOT_DIR  = join(BOOTSTRAP, pardir)
WITH_VENV = join(BOOTSTRAP, 'with_venv.sh')


def with_venv(*args):
    """
    Runs the given command inside virtualenv.
    """
    cmd = list(args)
    cmd.insert(0, WITH_VENV)
    return subprocess.call(cmd)


def after_install(options, home_dir):
    with_venv('pip', 'install', '-r', join(ROOT_DIR,'requirements.txt'))
    print "Done! Activate your virtualenv: source bin/activate"

