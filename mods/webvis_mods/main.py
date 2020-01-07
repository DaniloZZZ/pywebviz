from os import makedirs
from shutil import rmtree as rmdir
import webvis_mods, webvis
from pathlib import Path

from . import utils
from .imports import (
      index_import_py , root_import_py
    , index_import_js , root_import_js
)

from webvis_mods.paths_config import (
    manager_path,
    web_src, web_user_mods,
    build_dir, python_user_mods
)

def _prepare_dir_struct(src, usr_mods, modname, action):
    """
    :arg src: source directory of module
    :arg usr_mods: a root directory of modules installed
    :arg modname: module name
    :arg action: copy, link or whatever function that takes src and moddir
    """
    moddir = usr_mods / modname
    makedirs(usr_mods, exist_ok=True)
    if src.is_file():
        makedirs(moddir, exist_ok=True)
    action(src.absolute(), moddir)
    return moddir

def _update_imports():
    index_import_py(python_user_mods)
    index_import_js(web_user_mods)

def _process_py(modname, back_src, action=utils.copy):
    back_moddir = _prepare_dir_struct(back_src, python_user_mods, modname,
                                      action=action)
    if back_src.is_file():
        root_import_py(back_src, back_moddir)

def _process_js(modname, front_src, action=utils.copy):
    front_moddir = _prepare_dir_struct(front_src, web_user_mods, modname,
                                           action=action)
    if front_src.is_file():
        root_import_js(front_src, front_moddir)

## ## ## API ## ## ##  

def develop(modname, back_src, front_src):
    back_src, front_src = Path(back_src), Path(front_src)
    _process_py(modname, back_src, action=utils.ln)
    _process_js(modname, front_src, action=utils.ln)
    _update_imports()

    print(f"Running devolopment server from {web_src}...")
    utils.run_cmd([manager_path/'develop.sh', web_src])

def install(modname, back_src, front_src):
    back_src, front_src = Path(back_src), Path(front_src)
    _process_py(modname, back_src, action=utils.copy)
    _process_js(modname, front_src, action=utils.copy)
    _update_imports()

    ## Build the front and copy dist
    print(f"Building the app from {web_src}...")
    utils.run_cmd([manager_path/'build.sh', web_src])
    utils.run_cmd(['rsync', '-r', web_src/'dist', build_dir])
    print(f"Successfully installed module {modname}")

def uninstall(modname):
    utils.rm(python_user_mods / modname)
    utils.rm(web_user_mods / modname)
    _update_imports()
    print(f"Successfully uninstalled module {modname}")

def installed():
    import webvis.modules.installed as installed
    return [x for x in installed.__dir__() if x[0] != '_']
