from webvis_mods import install_mod, uninstall_mod, installed, develop
import sys

usage = """\
Usage: python -m webvis_mods.cli <command> [MODULE_NAME [BACK [FRONT]]]
Commands:
    install         Requires BACK and FRONT parametens.
    list
    uninstall
        """

def install():
    try:
        modname = sys.argv[2]
        back = sys.argv[3]
        front = sys.argv[4]
    except IndexError:
        print(usage)

    install_mod(back, front, modname)

def list_():
    ms = installed()
    print("\n".join(ms))

def uninstall():
    try:
        modname = sys.argv[2]
    except IndexError:
        print(usage)

    uninstall_mod(modname)

def main():
    cmd = None
    try:
        cmd = sys.argv[1]
    except IndexError:
        print(usage)
        return
    if cmd == 'install':
        install()
    elif cmd == 'uninstall':
        uninstall()
    elif cmd == 'list':
        list_()
    elif cmd == 'develop':
        develop(sys.argv[3], sys.argv[4], sys.argv[2])
    else:
        print(usage)

if __name__ == '__main__':
    main()
