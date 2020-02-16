""" Cli interface for libvis modules and dev """
import click
import webvis_mods as wm

from webvis_mods.config_gen import with_webvis_config
from webvis_mods.publish import publish
from webvis_mods.utils import only_required_kwargs_call
from webvis_mods.download import repository

@click.group()
def cli(): pass

name = click.argument('modname', required=False)
back = click.argument('back_src'
                      , type=click.Path(exists=True), required=False)
front = click.argument('front_src'
                       , type=click.Path(exists=True), required=False)

files = lambda x: back( front(
    with_webvis_config(x)
))


@cli.command()
@name
@files
def install(*args, **kwargs):
    """ Install a module from directory """
    print('Arguments', kwargs)
    only_required_kwargs_call(
        wm.install, *args, **kwargs)

@cli.command()
@name
@files
def develop(*args, **kwargs):
    """ Run the web server in development mode with hot reload """
    print(args, kwargs)
    only_required_kwargs_call(
        wm.develop, *args, **kwargs)

@cli.command('list')
def list_():
    """ list installed modules """
    mods = wm.installed()
    print("\n".join(mods))

@cli.command()
@name
def uninstall(*args, **kwargs):
    wm.uninstall(kwargs['modname'])

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

@cli.command()
@click.option('-o', '--output-dir', 'output_dir', default='.')
@click.argument('source')
def download(source, output_dir):
    repository.determine_repo_dir(source, output_dir)

cli.command()(publish)

if __name__ == '__main__':
    cli()
