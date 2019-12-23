from os import makedirs
import webvis_mods
import webvis
from pathlib import Path
from loguru import logger as log

from imports import (
    import_str_python
    , import_str_js
    , generate_index
)

from .utils import run_cmd, copy, write_to

# Sources
manager_path = Path(webvis_mods.__file__).parent
web_src = manager_path / 'web'
web_mods = web_src /'src'/ 'modules'/'presenters'
web_user_mods = web_mods / 'installed'

# Target
vis_dir = Path(webvis.__file__).parent
build_dir = vis_dir / 'front_build'
python_mods_dir = vis_dir / 'modules'
python_user_mods = python_mods_dir / 'installed'

def init_mod(name, path='~/webvis_modules/'):
    path = Path(path)
    mod_path = path / name
    makedirs(mod_path / 'back', exist_ok=True)
    makedirs(mod_path / 'front', exist_ok=True)


def install_mod(back_src, front_src, modname):
    back_src = Path(back_src)
    front_src = Path(front_src)
    makedirs(web_user_mods, exist_ok=True)
    makedirs(python_user_mods, exist_ok=True)
    log.debug("Web modules path: {}", web_src)


    back_moddir = python_user_mods / modname
    front_moddir = web_user_mods / modname
    # Install module
    makedirs(back_moddir, exist_ok=True)
    makedirs(front_moddir, exist_ok=True)

    ## Copy files
    copy(back_src, back_moddir)
    copy(front_src, front_moddir)

    ## Set up import of module
    if back_src.is_file():
        write_to(f"from .{back_src.stem} import {modname} ",
                 back_moddir/'__init__.py')

    # Update index imports
    index_py = generate_index(import_str_python, python_user_mods)
    write_to(index_py, python_user_mods/'__init__.py')

    if front_src.is_file():
        imp = f"import {{default as {modname}}} from './{front_src.name}'; export default {modname}"

        write_to(imp, front_moddir/'index.js')
    index_js = generate_index(import_str_js, web_user_mods)
    write_to(index_js, web_user_mods/'index.js')

    ## Build the front and copy dist
    run_cmd([manager_path/'build.sh', web_src])
    run_cmd(['rsync', '-r', web_src/'dist', build_dir])
