import libvis_mods
#from threading import Thread
from multiprocessing import Process
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
        t = Process(target=dev)
        #t.daemon = True
        t.start()
        time.sleep(2)
        t.terminate()
        t.join()

    finally:
        libvis_mods.uninstall('BirModule')
