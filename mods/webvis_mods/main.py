from os import makedirs
import webvis_mods
import webvis
from pathlib import Path
from loguru import logger as log

from imports import (
    generate_index
    , import_str_python
    , root_import_py
    , import_str_js
    , root_import_js
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

def _dir_struct(src, usr_mods, modname):
    """
    Put `src` into `usr_mods/modname` directory.
    Create if does not exist

    Returns
    -------
    moddir: pathlib.Path
        the root of files copied from `src` directory
    """
    moddir = usr_mods / modname
    makedirs(moddir, exist_ok=True)
    copy(src, moddir)
    return moddir

def init_mod(name, path='~/webvis_modules/'):
    path = Path(path)
    mod_path = path / name
    makedirs(mod_path / 'back', exist_ok=True)
    makedirs(mod_path / 'front', exist_ok=True)

def install_mod(back_src, front_src, modname):
    back_src, front_src = Path(back_src), Path(front_src)
    #Back
    back_moddir = _dir_struct(back_src, python_user_mods, modname)

    if back_src.is_file():
        root_import_py(back_src, back_moddir)

    index_py = generate_index(import_str_python, python_user_mods)
    write_to(index_py, python_user_mods/'__init__.py')

    # Front
    log.debug("Web modules path: {}", web_src)
    front_moddir = _dir_struct(front_src, web_user_mods, modname)

    if front_src.is_file():
        root_import_js(front_src, front_moddir)
    index_js = generate_index(import_str_js, web_user_mods)
    write_to(index_js, web_user_mods/'index.js')

    ## Build the front and copy dist
    print(f"Building the app from {web_src}...")
    run_cmd([manager_path/'build.sh', web_src])
    run_cmd(['rsync', '-r', web_src/'dist', build_dir])
