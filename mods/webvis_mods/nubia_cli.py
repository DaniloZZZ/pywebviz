import socket
import sys
import nubiac
import typing
import os

from termcolor import cprint
from nubia import Nubia, Options
from nubia import argument, command, context


if __name__ == "__main__":
    shell = Nubia(
        name="nubia_example",
        command_pkgs=nubiac,
    )
    sys.exit(shell.run())
