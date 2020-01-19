import pprint as pp
pprint = pp.pprint

def entry(config, path, funcs):
    print(f'Config: {pp.pformat(config)}')
    print(f'Path {path}')
    #descent(config, path, funcs)
    traverse(config, path, funcs)


# One way
def descent(config, path, funcs):
    print(f'Current path: {path}')
    fname = path.pop(0)
    config.update(config.get(fname, {}))
    f = funcs.get(fname)
    if isinstance(f, dict):
        funcs.update(f)
        descent(config, path, funcs)
    elif hasattr(f, '__call__'):
        config[fname] = '<<Entered deleted>>'
        del config[fname]
        leaf(funcs[fname], config)
        if len(path):
            descent(config, path, funcs)
    else:
        raise Exception(f'callspec[{fname}] is {f}')

## Another way
def traverse(config, path, funcs):
    while len(path) > 0:
        this_config = config.copy()
        this_funcs = funcs.copy()
        print(f'Current path: {path}')
        fname = path[0]
        this_config.update(config.get(fname, {}))
        f = this_funcs.get(fname)
        if f is None: break

        if isinstance(f, dict):
            path.pop(0)
            traverse(this_config, path, f)

        if hasattr(f, '__call__'):
            path.pop(0)
            leaf(f, this_config)
            traverse(this_config, path, this_funcs)
        print(f'Renurned traverse, path: {path}')

def leaf(func, config):
    func(**config)
