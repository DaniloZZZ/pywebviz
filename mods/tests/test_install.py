from importlib import reload
import webvis
import webvis_mods

from pathlib import Path

mocks = Path(__file__).parent / 'mocks'

pyfile, webfle = mocks/'module.py', mocks/'blah.coffee'

webvis_mods.install_mod(pyfile, webfle, 'Test')
from webvis.modules import Test
t = Test()
t = None
webvis_mods.uninstall_mod('Test')
webvis = reload(webvis)

pyfile, webfle = mocks/'BirModule'/'back', mocks/'BirModule'/'front'

webvis_mods.install_mod(pyfile, webfle, 'BirModule')
from webvis.modules import BirModule
m = BirModule(count=5)
m.serial()
webvis_mods.uninstall_mod('BirModule')
