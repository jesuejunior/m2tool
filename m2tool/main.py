from modargs import args
import sys
import os
import m2tool.commands
from m2tool.conf import M2_DB_ENV, M2_DEFAULT_DB_PATH
import komandr


def main():
    _,params = args.parse(sys.argv[2:])
    os.environ.setdefault(M2_DB_ENV, params.get('m2db', M2_DEFAULT_DB_PATH))
    print "Using DB {0}".format(os.environ.get(M2_DB_ENV))

    komandr.main()


#    if command not in all_commands:
#        print "Command {0} not found!".format(command)
#
#    else:
#        f = args.function_for(m2tool.commands, command)
#        f(sys.argv[2:])
#
#    sys.exit(0)

main()