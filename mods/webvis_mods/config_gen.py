import configparser
from pathlib import Path
from webvis_mods.utils import only_required_kwargs_call

filename = 'webvis-mod.conf'

def with_webvis_config(cmd, path='.'):
    def ncmd(*args, **kwargs):
        config = dict(read_config(Path(path)))
        for key, value in kwargs.items():
            if value is not None:
                config[key] = value
        return only_required_kwargs_call(cmd, *args, **config)
    ncmd.__name__ = cmd.__name__
    ncmd.__doc__ = cmd.__doc__
    return ncmd

def read_config(path):
    config=configparser.ConfigParser()
    config.read(path / filename)
    if 'Module' in config.sections():
        mod = config['Module']
        return mod
    else: return {}

def write_config(conf_dict, path):
    config=configparser.ConfigParser()
    config['Module'] = conf_dict
    with open(path / filename, 'w') as f:
        config.write(f)
