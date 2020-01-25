import libvis
from importlib import reload
import time
import importlib
from watchdog import observers, events
from types import ModuleType
import libvis.modules.installed as modules
from loguru import logger as log

def rreload(module):
    """Recursively reload modules."""
    print('reload', module)
    if 'libvis' not in module.__file__:
        return
    reload(module)
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if type(attribute) is ModuleType:
            rreload(attribute)
    return module

class ModHotReload(events.PatternMatchingEventHandler):
    @log.catch
    def __init__(self, modname, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.modname = modname
        print(modules)
        rreload(modules)
        print(modules.__dict__.keys())
        Mod = getattr(modules, self.modname)
        print('hot reloading module:', Mod)
        self._cls_name = self.modname
        self.module = importlib.import_module(Mod.__name__)

        self.vis = libvis.Vis()
        self.test_data = {}
        self.vis.start()
        self.set_testmod()
        self._last_event = time.time()
        self._timedelta = .5

    def set_testmod(self):
        m = self._init_mod()
        self.vis.vars.test = m

    def on_any_event(self, event):
        if time.time() - self._last_event > self._timedelta:
            print('Module changed', event)
            with log.catch():
                self.module = rreload(self.module)
            self.set_testmod()
            self._last_event = time.time()

    def _init_mod(self):
        Mod = getattr(self.module, self._cls_name)
        print("Module dict:", Mod.__dict__)
        with log.catch():
            m = Mod.test_object()
            return m
            #print('Fix the module, save the file, libvis will reload it for you.')

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
