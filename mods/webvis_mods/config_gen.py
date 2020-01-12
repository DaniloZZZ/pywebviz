import configparser

filename = 'webvis-mod.conf'

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
