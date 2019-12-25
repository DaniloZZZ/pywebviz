from importlib import reload
import webvis.modules as modules
import webvis
import webvis_mods

from pathlib import Path

mocks = Path(__file__).parent / 'mocks'

pyfile, webfle = mocks/'module.py', mocks/'blah.coffee'

webvis_mods.install_mod(pyfile, webfle, 'Test')
modules = reload(modules)
reload(webvis)

t = modules.Test()
t = None
webvis_mods.uninstall_mod('Test')

pyfile, webfle = mocks/'BirModule'/'back', mocks/'BirModule'/'front'

webvis_mods.install_mod(pyfile, webfle, 'BirModule')
modules = reload(modules)
reload(webvis)

m = modules.BirModule(count=5)
m.serial()
m = None
webvis_mods.uninstall_mod('BirModule')
