from modargs import args
import sys
import os

import m2tool.commands
from m2tool.conf import M2_DB_ENV, M2_DEFAULT_DB_PATH

def main():
    command, params = args.parse(sys.argv[1:])
    all_commands = args.available_commands(m2tool.commands)
    print M2_DB_ENV
    os.environ.setdefault(M2_DB_ENV, params.get('m2db', M2_DEFAULT_DB_PATH))

    print "Using DB {0}".format(os.environ.get(M2_DB_ENV))

    print params
    if command not in all_commands:
        print "Command {0} not found!".format(command)

    else:
        print "Running {0}".format(command)
        f = args.function_for(m2tool.commands, command)
        f(**params)

    sys.exit(0)
