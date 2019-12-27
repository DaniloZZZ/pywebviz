from os import makedirs
from shutil import rmtree as rmdir
import webvis_mods, webvis
from pathlib import Path

from . import utils
from .imports import (
      index_import_py , root_import_py
    , index_import_js , root_import_js
)

# Sources
manager_path = Path(webvis_mods.__file__).parent
web_src = manager_path / 'web'
web_user_mods = web_src /'src'/ 'modules' / 'presenters' / 'installed'

# Target
vis_dir = Path(webvis.__file__).parent
build_dir = vis_dir / 'front_build'
python_user_mods = vis_dir / 'modules' / 'installed'

def _prepare_dir_struct(src, usr_mods, modname):
    """
    :arg src: source directory of module
    :arg usr_mods: a root directory of modules installed
    :arg modname: module name
    """
    moddir = usr_mods / modname
    makedirs(moddir, exist_ok=True)
    utils.copy(src, moddir)
    return moddir
def _prepare_dir_struct_dev(src, usr_mods, modname):
    """
    :arg src: source directory of module
    :arg usr_mods: a root directory of modules installed
    :arg modname: module name
    """
    moddir = usr_mods / modname
    makedirs(usr_mods, exist_ok=True)
    if src.is_file():
        makedirs(moddir, exist_ok=True)
    utils.ln(src.absolute(), moddir)
    return moddir

def _update_imports():
    index_import_py(python_user_mods)
    index_import_js(web_user_mods)

def init_mod(name, path='~/webvis_modules/'):
    path = Path(path)
    mod_path = path / name
    makedirs(mod_path / 'back', exist_ok=True)
    makedirs(mod_path / 'front', exist_ok=True)

def develop(back_src, front_src, modname):
    back_src, front_src = Path(back_src), Path(front_src)
    back_moddir = _prepare_dir_struct_dev(back_src, python_user_mods, modname)
    if back_src.is_file():
        root_import_py(back_src, back_moddir)

    front_moddir = _prepare_dir_struct_dev(front_src, web_user_mods, modname)
    if front_src.is_file():
        root_import_js(front_src, front_moddir)
    _update_imports()

    print(f"Running devolopment server from {web_src}...")
    utils.run_cmd([manager_path/'develop.sh', web_src])

def install_mod(back_src, front_src, modname):
    back_src, front_src = Path(back_src), Path(front_src)

    # Back src
    back_moddir = _prepare_dir_struct(back_src, python_user_mods, modname)
    if back_src.is_file():
        root_import_py(back_src, back_moddir)

    # Front src 
    front_moddir = _prepare_dir_struct(front_src, web_user_mods, modname)
    if front_src.is_file():
        root_import_js(front_src, front_moddir)

    _update_imports()

    ## Build the front and copy dist
    print(f"Building the app from {web_src}...")
    utils.run_cmd([manager_path/'build.sh', web_src])
    utils.run_cmd(['rsync', '-r', web_src/'dist', build_dir])
    print(f"Successfully installed module {modname}")

def uninstall_mod(modname):
    utils.rm(python_user_mods / modname)
    utils.rm(web_user_mods / modname)
    _update_imports()
    print(f"Successfully uninstalled module {modname}")

def installed():
    import webvis.modules.installed as installed
    return [x for x in installed.__dir__() if x[0] != '_']
