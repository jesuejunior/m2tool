from modargs import args
import sys
import os
import m2tool.commands
from m2tool.conf import M2_DB_ENV, M2_DEFAULT_DB_PATH

def main():
    command = sys.argv[1:2]
    command = command[0]
    option,params = args.parse(sys.argv[2:])

    all_commands = args.available_commands(m2tool.commands)

    os.environ.setdefault(M2_DB_ENV, params.get('m2db', M2_DEFAULT_DB_PATH))

    print "Using DB {0}".format(os.environ.get(M2_DB_ENV))

    print params
    print command
    print option
    if command not in all_commands:
        print "Command {0} not found!".format(command)

    else:
        #print func
        print "Running {0}".format(command)
        f = args.function_for(m2tool.commands, command)
        f(option,**params)

    sys.exit(0)
