from distutils.command.install import install as distutils_install
from distutils.command.sdist import sdist as distutils_sdist

from setuptools import setup

from .hooked_cmdclass import get_class as hooked_distutils_class
from webvis_mods import install as mods_install
from webvis_mods.config_gen import with_webvis_config
from functools import partial



@with_webvis_config
def install_message(**config):
   print("Webvis Module {modname} installing".format(**config))

default_pre = install_message
default_post = with_webvis_config(mods_install)

def hooked_install_class(
    pre=default_pre, post=default_post):
    return hooked_distutils_class(
        distutils_install, pre=pre, post=post
    )


def webvis_setup(*args, **kwargs):
    #pre = kwargs.get('webvis_pre_hook', install_message)
    #post = kwargs.get('webvis_post_hook', with_webvis_config(mods_install))

    defaults = {
        'cmdclass':{
            'install':hooked_distutils_class(distutils_install),
            #'sdist':hooked_distutils_class(distutils_sdist)
        }
    }
    defaults.update(kwargs)
    setup(*args, **defaults)

noop = lambda *x, **y: None

def hook_setup(
    install=noop, pre_install=noop,
    sdist=noop, pre_sdist=noop
):
    def setup(*args, **kwargs):
        defaults = {
            'cmdclass':{
                'install':hooked_distutils_class(
                    distutils_install,pre=pre_install, post=install
                ),
                'sdist':hooked_distutils_class(
                    distutils_sdist, pre=pre_sdist, post=sdist)
            }
        }
        defaults.update(kwargs)
        webvis_setup(*args, **defaults)
    return setup


