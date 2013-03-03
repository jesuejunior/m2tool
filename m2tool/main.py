from modargs import args
import sys
import os
import m2tool.commands
from m2tool.conf import M2_DB_ENV, M2_DEFAULT_DB_PATH
import komandr


def main():
    # _,params = args.parse(sys.argv[2:])
    os.environ.setdefault(M2_DB_ENV, {}.get('m2db', M2_DEFAULT_DB_PATH))
    print "Using DB {0}".format(os.environ.get(M2_DB_ENV))

    komandr.main.execute(sys.argv[1:3])
