import click
import webvis_mods as wm

class CatchAllExceptions(click.Group):
    def __call__(self, *args, **kwargs):
        try:
            return self.main(*args, **kwargs)
        except Exception as exc:
            click.echo('Error:\n%s' % exc)

@click.group(cls = CatchAllExceptions)
def cli():
    pass

name = click.argument('modname')#, help='Name of module')
back = click.argument('back')#, help='Directory or file with backend code')
front = click.argument('front')#, help='Directory or file with backend code')

files = lambda x: back( front(x) )

@cli.command()
@name
@files
def install(modname, back, front):
    """ Install a module from directory """
    wm.install(modname, back, front)

@cli.command()
@name
@files
def develop(modname, back, front):
    """ Run the web server in development mode """
    wm.develop(modname, back, front)

@cli.command('list')
def list_():
    """ list installed modules """
    ms = wm.installed()
    print("\n".join(ms))

@cli.command()
@name
def uninstall(modname):
    wm.uninstall(modname)

@cli.command()
@click.option('-o', '--output-dir', 'output_dir', default='.')
@name
def init_file(modname, output_dir):
    wm.init_file(modname, output_dir=output_dir)

if __name__ == '__main__':
    cli()
