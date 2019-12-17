import inspect
from shutil import copy as copyfile
import subprocess
import hosta
import webvis_mods
try:
    import webvis
except ImportError:
    raise
    print("You need to install webvis")
from pathlib import Path
from loguru import logger as log

# Sources
manager_path = Path(webvis_mods.__file__).parent
web_src = manager_path / 'web'
web_mods_dir = web_src /'src'/ 'modules'/'presenters'/'custom'

# Target
vis_dir = Path(webvis.__file__).parent
build_dir = vis_dir / 'front_build'
python_mods_dir = vis_dir / 'modules'

def install_mod(pyfile, webfile, modname):
    log.debug("Web source path: {}", web_src)

    ## Copy files
    copyfile(pyfile, python_mods_dir)
    copyfile(webfile, web_mods_dir)

    ## Build the app and copy dist
    def run(cmds):
        try:
            subprocess.run(' '.join([str(x) for x in cmds]),
                       check=True,
                       shell=True,
                       capture_output=True
                      )
        except subprocess.CalledProcessError as e:
            print(e.cmd, e.output, e.stderr)
            raise

    run([web_mods_dir.parent/'import_string.sh',
         modname,
         'custom/'+ webfile.split('/')[-1],
         '>>',
         web_mods_dir.parent/'index.js'
        ])
    run([manager_path/'build.sh', web_src])
    run(['rsync', '-r','--ignore-existing', web_src/'dist', build_dir])
