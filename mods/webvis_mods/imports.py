from pathlib import Path

def import_str_python(modname):
    return f"from .{modname} import {modname}"
def import_str_js(modname):
    return f"export {{default as {modname}}} from './{modname}'"

def generate_index(import_str, mod_dir):
    mod_dir = Path(mod_dir)
    mods = [x.name for x in mod_dir.iterdir() if x.is_dir()]
    return '\n'.join(map(import_str, mods))
