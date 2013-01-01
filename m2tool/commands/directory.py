#encoding: utf-8
from alchemytools.context import managed
from clint.textui import puts, columns
from modargs import args
from m2tool.db import Session
from m2tool.db.directory import Directory

def directory_command(arglist):
    '''
    --base=PATH --indexfile=NAME
    --defaultctype=MIMETYPE --cachettl=BOOLEAN
    '''

    subcommand, params = args.parse(arglist)

    if subcommand in globals():
        globals()[subcommand](**params)
    else:
        print "Subcommand {0} not found".format(subcommand)



def add(base=None, indexfile='index.html', defaultctype='text/html', cachettl=False):
    print "Adding Directory: BASE={0}, INDEX_FILE={1}".format(base, indexfile)
    print base

    if not base or base == True:
        print "Please verify parameter --base"
        return False
    with managed(Session) as session:

        directory = Directory(base=base, index_file=indexfile, default_ctype=defaultctype, cache_ttl=cachettl)

        session.add(directory)


def remove(id):
    with managed(Session) as session:
        directory = session.query(Directory).get(id)
        if directory:
            session.query(Directory).filter_by(id=id).delete()
            session.commit()
            print 'Directory ID [{0}] was removed with success.'.format(directory.id)
        else:
            print 'Directory not found.'

def list():
    with managed(Session) as session:
        dirs = session.query(Directory).all()
        if dirs:
            puts(columns(['ID', 4], ['BASE', 30], ["INDEX_FILE", 12], ['DEFAULT_CTYPE', 15], ["CACHE_TTL", 10]))

        for dir in dirs:
            puts(columns([str(dir.id), 4], [dir.base, 30], [dir.index_file, 12], [dir.default_ctype, 15], [str(dir.cache_ttl), 10]))
