from importlib import reload
import libvis.modules.installed as modules
import libvis_mods

from pathlib import Path

def test_install():
    global modules
    mocks = Path(__file__).parent / 'mocks'

    pyfile, webfle = mocks/'module.py', mocks/'blah.coffee'

    try:
        libvis_mods.install('Test', pyfile, webfle)
        modules = reload(modules)

        _ = modules.Test()
    finally:
        libvis_mods.uninstall('Test')

    try:
        pyfile, webfle = mocks/'BirModule'/'back', mocks/'BirModule'/'front'

        libvis_mods.install('BirModule', pyfile, webfle)
        modules = reload(modules)

        m = modules.BirModule(count=5)
        m.serial()
        m = None
    finally:
        libvis_mods.uninstall('BirModule')

if __name__ == '__main__':
    test_install()
