from importlib import reload
import webvis.modules.installed as modules
import webvis_mods

from pathlib import Path

mocks = Path(__file__).parent / 'mocks'

pyfile, webfle = mocks/'module.py', mocks/'blah.coffee'

webvis_mods.install('Test', pyfile, webfle)
modules = reload(modules)

t = modules.Test()
t = None
webvis_mods.uninstall('Test')

pyfile, webfle = mocks/'BirModule'/'back', mocks/'BirModule'/'front'

webvis_mods.install('BirModule', pyfile, webfle)
modules = reload(modules)

m = modules.BirModule(count=5)
m.serial()
m = None
webvis_mods.uninstall('BirModule')
