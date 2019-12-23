from pathlib import Path
from . import utils

def generate_index(import_str, mod_dir):
    mod_dir = Path(mod_dir)
    mods = [x.name for x in mod_dir.iterdir() if x.is_dir()]
    x = '\n'.join(map(import_str, mods))
    return x

## Python

def import_str_python(modname):
    return f"from .{modname} import {modname}"

def root_import_py(src_file, moddir):
    modname = moddir.name
    utils.write_to(f"from .{src_file.stem} import {modname} ",
             moddir/'__init__.py')

## JS

def import_str_js(modname):
    return f"export {{default as {modname}}} from './{modname}'"

def root_import_js(src_file, moddir):
    modname = moddir.name
    x = f"import {{default as {modname}}} from './{src_file.name}';\
            export default {modname}"
    utils.write_to(x, moddir/'index.js')

