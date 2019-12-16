import inspect
import hosta
import webvis_mods
from pathlib import Path
from loguru import logger as log

_path = Path(webvis_mods.__file__)
web_src = _path.parent / 'web' / 'src'

def install_mod(pyfile, webfile):
    log.debug("Web source path: {}", web_src)


