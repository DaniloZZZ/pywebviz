import mock
#from webvis_mods.webvis_dist import setup

def test_setup(capsys):
    args = ['python', 'install', '--user']
    with mock.patch('sys.argv', args):

        from webvis_mods.webvis_dist import hook_setup
        setup = hook_setup( pre_install=lambda: print('FooBar') )

        setup(
            name='spam',
            version='0',
            packages = ['mocks']
        )
        out, err = capsys.readouterr()
        assert 'FooBar' in  out

if __name__ =='__main__':
    test_setup()
