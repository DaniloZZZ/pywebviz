import webvis
from importlib import reload
import time
import importlib
from watchdog import observers, events
from types import ModuleType
import webvis.modules.installed as modules
from loguru import logger as log

def rreload(module):
    """Recursively reload modules."""
    reload(module)
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if type(attribute) is ModuleType:
            rreload(attribute)
    return module

class ModHotReload(events.PatternMatchingEventHandler):
    def __init__(self, modname, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.modname = modname
        print(modules)
        Mod = getattr(modules, self.modname)
        self.module = importlib.import_module(Mod.__module__)
        self.vis = webvis.Vis()
        self.test_data = {}
        self.vis.start()
        self.set_testmod()

    def _init_mod(self):
        Mod = getattr(self.module, self.modname)
        print("Module dict:", Mod.__dict__)
        with log.catch():
            m = Mod(self.test_data)
            return m
            #print('Fix the module, save the file, webvis will reload it for you.')

    def set_testmod(self):
        m = self._init_mod()
        self.vis.vars.test = m

    def on_any_event(self, event):
        print('Module changed', event)
        time.sleep(.05)
        with log.catch():
            self.module = rreload(self.module)
        self.set_testmod()

def python_dev_server(modname, path):
    observer = observers.Observer()
    if path.is_file():
        handler = ModHotReload(modname, patterns=['*.py'])
        print(f"Watching {path.parent}")
        observer.schedule(handler, str(path.parent), recursive=False)
    else:
        handler = ModHotReload(modname)
        observer.schedule(handler, str(path), recursive=True)
    observer.start()


