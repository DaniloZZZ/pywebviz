from pathlib import Path
import os
import shutil
from loguru import logger as log

import sys
from webvis_mods.utils import run_cmd, safe_copy
from webvis_mods.webvis_dist import webvis_setup
from webvis_mods.config_gen import read_config

setup_file = webvis_setup.__file__

def publish(path='.'):
    path = Path(path)
    config = read_config(path)
    log.info('Module config {}', config)

    try:
        # Create a temp dir for setup
        setup_dir = path / '.webvis_publish'
        setup_dir.mkdir(exist_ok=True)

        print('copy setup file')
        shutil.copy(setup_file, setup_dir)
        try:
            os.symlink(path.absolute(), (setup_dir/config['modname']).absolute())
        except: pass

        safe_copy(path.absolute()/'webvis-mod.conf', setup_dir.absolute()/'webvis-mod.conf')
        safe_copy(path.absolute()/'MANIFEST.in', setup_dir.absolute()/'MANIFEST.in')

        os.chdir(setup_dir)

        run_cmd([sys.executable, 'webvis_setup.py', 'sdist'])
        upload()
        print("Successfully published module")
    except Exception as e:
        print("Failed to publish\n",e)
    finally:
        os.chdir(path.absolute())

def upload():
    upload_ = [sys.executable, '-m', 'twine', 'upload']
    upload_ += ['--repository-url', 'http://webvis.dev/legacy/']
    upload_ += ['-u', 'foobar39', '-p', 'FooBar39FooBa']
    upload_ += ['dist/*']
    run_cmd(upload_)
