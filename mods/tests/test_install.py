import webvis_mods
from pathlib import Path

mocks = Path(__file__).parent / 'mocks'

pyfile, webfle = mocks/'module.py', mocks/'blah.coffee'

webvis_mods.install_mod(pyfile, webfle, 'Test')
