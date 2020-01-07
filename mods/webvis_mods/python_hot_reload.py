import webvis
from importlib import reload
import importlib
import time
from watchdog import observers, events

def reload_module(full_module_name):
    """
        Assuming the folder `full_module_name` is a folder inside some
        folder on the python sys.path, for example, sys.path as `C:/`, and
        you are inside the folder `C:/Path With Spaces` on the file 
        `C:/Path With Spaces/main.py` and want to re-import some files on
        the folder `C:/Path With Spaces/tests`

        @param full_module_name   the relative full path to the module file
                                  you want to reload from a folder on the
                                  python `sys.path`
    """
    import imp
    import sys
    import importlib

    if full_module_name in sys.modules:
        module_object = sys.modules[full_module_name]
        module_object = imp.reload( module_object )

    else:
        importlib.import_module( full_module_name )

class ModHotReload(events.PatternMatchingEventHandler):
    def __init__(self, modname, *args, **kwargs):
        super().__init__(*args, **kwargs)

        import webvis.modules.installed as modules
        self.modname = modname
        self.vis = webvis.Vis()
        self.Mod = importlib.import_module(
            f"webvis.modules.installed.{modname}")
        self.test_data = {}
        self.vis.start()
        self.set_testmod()

    def set_testmod(self):
        m = self.Mod(self.test_data)
        self.vis.vars.test = m

    def on_any_event(self, event):
        print('mod changed', event)
        self.Mod = reload(self.Mod)
        self.set_testmod()

def python_dev_server(modname, path):
    observer = observers.Observer()
    if path.is_file():
        handler = ModHotReload(modname, patterns=['*.py'])
        print(f"watching {path.parent} pattern {path.name}")
        observer.schedule(handler, str(path.parent), recursive=False)
    else:
        handler = ModHotReload(modname)
        observer.schedule(handler, str(path), recursive=True)
    observer.start()


