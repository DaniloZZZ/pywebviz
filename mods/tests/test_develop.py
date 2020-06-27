import libvis_mods
from threading import Thread
from pathlib import Path
import time
mocks = Path(__file__).parent / 'mocks'

def test_develop_installed():
    global modules
    try:
        pyfile, webfle = mocks/'BirModule'/'back', mocks/'BirModule'/'front'

        libvis_mods.install('BirModule', pyfile, webfle)
        def dev():
            libvis_mods.develop('BirModule', pyfile, webfle)
        t = Thread(target=dev)
        t.daemon = True
        t.start()
        time.sleep(1)

    finally:
        libvis_mods.uninstall('BirModule')
