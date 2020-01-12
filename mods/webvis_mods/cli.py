import click
from pathlib import Path
import webvis_mods as wm
from .config_gen import read_config, write_config

class CatchAllExceptions(click.Group):
    def __call__(self, *args, **kwargs):
        try:
            return self.main(*args, **kwargs)
        except Exception as exc:
            click.echo('Error:\n%s' % exc)

@click.group(cls = CatchAllExceptions)
def cli():
    pass

name = click.argument('modname', required=False)#, help='Name of module')
back = click.argument('back_src', type=click.Path(exists=True),
                      required=False) #, help='Directory or file with backend code')
front = click.argument('front_src', type=click.Path(exists=True),
                       required=False)#, help='Directory or file with backend code')

files = lambda x: back( front(x) )

def command_wrapper(cmd):
    def ncmd(*args, **kwargs):
        config = dict(read_config(Path('.')))
        print('config', config)
        for key, value in kwargs.items():
            if value is not None:
                config[key] = value
        return cmd(*args, **config)
    ncmd.__name__ = cmd.__name__
    ncmd.__doc__ = cmd.__doc__
    return ncmd

@cli.command()
@name
@files
@command_wrapper
def install(*args, **kwargs):
    """ Install a module from directory """
    print('wn', kwargs)
    wm.install(*args, **kwargs)

@cli.command()
@name
@files
@command_wrapper
def develop(*args, **kwargs):
    """ Run the web server in development mode with hot reload """
    wm.develop(*args, **kwargs)

@cli.command('list')
def list_():
    """ list installed modules """
    ms = wm.installed()
    print("\n".join(ms))

@cli.command()
@name
@command_wrapper
def uninstall(*args, **kwargs):
    wm.uninstall(*args, **kwargs)

@cli.command()
@click.option('-o', '--output-dir', 'output_dir', default='.')
@name
def init_file(modname, output_dir):
    wm.init_file(modname, output_dir=output_dir)

@cli.command()
@click.option('-o', '--output-dir', 'output_dir', default='.')
@name
def init_dir(modname, output_dir):
    wm.init_dir(modname, output_dir=output_dir)

if __name__ == '__main__':
    cli()
