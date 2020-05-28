import libvis_mods
from pathlib import Path
mocks = Path(__file__).parent / 'mocks'

def test_develop_installed():
    global modules
    try:
        pyfile, webfle = mocks/'BirModule'/'back', mocks/'BirModule'/'front'

        libvis_mods.install('BirModule', pyfile, webfle)
        libvis_mods.develop('BirModule', pyfile, webfle)

    finally:
        libvis_mods.uninstall('BirModule')




