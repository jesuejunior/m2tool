#coding: utf-8
from uuid import uuid4
from modargs import args
from alchemytools.context import managed
from clint.textui import columns, puts

from m2tool.db import Session
import sys
from m2tool.db.server import Server
import komandr


_server = komandr.prog()


@komandr.command
@komandr.arg('cmd', 'cmd', choices=['add', 'remove', 'list'])
def server(cmd):
    _server.execute(sys.argv[2:])


@_server.command
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

@_server.command
@_server.arg('id', '--id')
def remove(id):
    with managed(Session) as session:
        server = session.query(Server).get(id)
        if server:
            server_name = server.name
            session.query(Server).filter_by(id=id).delete()
            session.commit()
            print 'Server [{0}] was removed with success.'.format(server_name)
        else:
            print 'Server not found.'

@_server.command
def list():
    """
    Lis all registered mongrel2 servers
    """
    with managed(Session) as session:
        servers = session.query(Server).all()
        if servers:
            puts(columns(["id", 10], ['Name', 32], ['Port', 5], ['Uuid', 10]))
        else:
            print "Servers not found"
        for server in servers:
            puts(columns([str(server.id), 10], [server.name, 32], [str(server.port), 5], [server.uuid, 40]))

