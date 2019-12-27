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
    wm.install_mod(back, front, modname)

@cli.command()
@name
@files
def develop(modname, back, front):
    """ Run the web server in development mode """
    wm.develop(back, front, modname)

@cli.command('list')
def list_():
    """ list installed modules """
    ms = wm.installed()
    print("\n".join(ms))

@cli.command()
@name
def uninstall(modname):
    wm.uninstall_mod(modname)

if __name__ == '__main__':
    cli()
