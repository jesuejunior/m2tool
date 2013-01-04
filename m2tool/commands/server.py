#coding: utf-8
from uuid import uuid4
from modargs import args
from alchemytools.context import managed
from clint.textui import columns, puts

from m2tool.db import Session
from m2tool.db.server import Server


def server_command(arglist):
    '''
    --uuid=UUID --accesslog=FILE --errorlog=FILE
    --chroot=PATH --pidfile=FILE --name=NAME
    --bindaddr=IP --port=PORT --ssl
    --defaulthost=HOSTNAME
    '''

    subcommand, params = args.parse(arglist)

    if subcommand in globals():
        globals()[subcommand](**params)
    else:
        print "Subcommand {0} not found".format(subcommand)


def add(name=None, port=None, chroot="/var/mongrel2", bindaddr="0.0.0.0", pidfile="/run/mongrel2.pid",
        defaulthost=None, accesslog='/logs/access.log', errorlog='/logs/error.log', ssl=False, uuid=None):
    print "Adding Server: name={0}, port={1}, ssl={2}".format(name, port, ssl)
    if not uuid:
        uuid = str(uuid4())

    with managed(Session) as session:
        uuid_verify = session.query(Server).filter_by(uuid=uuid).count()

        if uuid_verify:
            print 'UUID [{0}] already exists, please check.'.format(uuid)
            return False

        port_verify = session.query(Server).filter_by(port=port).count()
        if port_verify :
            print 'Porta [{0}] já está em uso, por favor tente outra'.format(port)
            return False

        if isinstance(port, bool) or not isinstance(name, str):
            print "Please verify parameters --port or --name"
            return False
        else:
            server = Server(name=name, port=port, chroot=chroot,  bind_addr=bindaddr, pid_File=pidfile,
                default_host=defaulthost, access_log=accesslog, error_log=errorlog, use_ssl=ssl, uuid=uuid )

            session.add(server)

    print 'Congratulations! Server [{0}] adding with success.'.format(name)


def remove(id):
    with managed(Session) as session:
        server = session.query(Server).get(id)
        if server:
            session.query(Server).filter_by(id=id).delete()
            session.commit()
            print 'Server [{0}] was removed with success.'.format(server.name)
        else:
            print 'Server not found.'

def list():
    with managed(Session) as session:
        servers = session.query(Server).all()
        if servers:
            puts(columns(['Name', 32], ['Port', 5], ['Uuid', 35]))
        else:
            print "Servers not found"
        for server in servers:
            puts(columns([server.name, 32], [str(server.port), 5], [server.uuid, 35]))

