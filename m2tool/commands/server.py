#coding: utf-8
from uuid import uuid4
from alchemytools.context import managed
from clint.textui import columns, puts
from m2tool.conf import DEFAULT_CHROOT, DEFAULT_BIND_ADDR, DEFAULT_PIDFILE, DEFAULT_ACCESS_LOG_FILE, DEFAULT_ERROR_LOG_FILE, DEFAULT_SSL

from m2tool.db import Session
from m2tool import __projectname__
import sys
from m2tool.db.server import Server
import komandr

UUID_ARG_HELP = "Sets the server's unique UUID. This is what is used by mongrel2 when starting/stopping the server. Default: Auto generated"

SSL_ARG_HELP = "Choose if this server will use SSL or not. Default: {0}".format(DEFAULT_SSL)

ERROR_LOG_ARG_HELP = "Where the server will create the error logs. This is relative to the chroot. Default: {0}".format(
    DEFAULT_ERROR_LOG_FILE)

ACCESS_LOG_ARG_HELP = "Where the server will create the access logs. This is relative to the chroot. Default: {0}".format(
    DEFAULT_ACCESS_LOG_FILE)

DEFAULT_HOST_ARG_HELP = "The *name* of the host this server will deliver the request if it does no match any other hosts."

PIDFILE_ARG_HELP = "Where the server will create the pidfile. This is relative to chroot. Default: {0}".format(DEFAULT_PIDFILE)

BINDADDR_ARG_HELP = "Which address your server will use. Default: {0}".format(DEFAULT_BIND_ADDR)

CHROOT_ARG_HELP = "Where your server will chroot before accepting connections. Default: {0}".format(DEFAULT_CHROOT)

PORT_ARG_HELP = "Port on which your server will listen to connections."

NAME_ARG_HELP = "The name of your server. This is just an internal name, choose what you like more."

_server = komandr.prog(prog='{0} server'.format(__projectname__))


@komandr.command
@komandr.arg('cmd', 'cmd', choices=['add', 'remove', 'list', 'update'], help="Available server subcommands. Use <subcommand> -h to see more.")
def server(cmd):
    _server.execute(sys.argv[2:])


@_server.command
@_server.arg('name', required=True, type=str, help=NAME_ARG_HELP)
@_server.arg('port', required=True, type=int, help=PORT_ARG_HELP)
@_server.arg('chroot', required=False, type=str, help=CHROOT_ARG_HELP)
@_server.arg('bindaddr', required=False, type=str, help=BINDADDR_ARG_HELP)
@_server.arg('pidfile', required=False, type=str, help=PIDFILE_ARG_HELP)
@_server.arg('defaulthost', required=False, type=str, help=DEFAULT_HOST_ARG_HELP)
@_server.arg('accesslog', required=False, type=str, help=ACCESS_LOG_ARG_HELP)
@_server.arg('errorlog', required=False, type=str, help=ERROR_LOG_ARG_HELP)
@_server.arg('ssl', required=False, type=bool, default=False, const=True, nargs='?', help=SSL_ARG_HELP)
@_server.arg('uuid', required=False, type=str, help=UUID_ARG_HELP)
def add(name=None, port=None, chroot=DEFAULT_CHROOT, bindaddr=DEFAULT_BIND_ADDR, pidfile=DEFAULT_PIDFILE,
        defaulthost=None, accesslog=DEFAULT_ACCESS_LOG_FILE, errorlog=DEFAULT_ERROR_LOG_FILE, ssl=DEFAULT_SSL,
        uuid=None):
    print "Adding Server: name={0}, port={1}, ssl={2}".format(name, port, ssl)
    if not uuid:
        uuid = str(uuid4())

    with managed(Session) as session:
        uuid_verify = session.query(Server).filter_by(uuid=uuid).count()

        if uuid_verify:
            print 'UUID [{0}] already exists, please check.'.format(uuid)
            return False

        port_verify = session.query(Server).filter_by(port=port).count()
        if port_verify:
            print 'Porta [{0}] já está em uso, por favor tente outra'.format(port)
            return False

        if not port or not name:
            print "Please verify parameters --port or --name"
            return False
        else:
            server = Server(name=name, port=port, chroot=chroot,  bind_addr=bindaddr, pid_File=pidfile,
                            default_host=defaulthost, access_log=accesslog, error_log=errorlog, use_ssl=ssl,
                            uuid=uuid)

            session.add(server)

    print 'Congratulations! Server [{0}] added successfully.'.format(name)


def _new_value_for_field(value, default):
    if value is not None:
        return value
    return default

@_server.command
@_server.arg("id", "--id", required=True, type=int)
@_server.arg('name', type=str, help=NAME_ARG_HELP)
@_server.arg('port', type=int, help=PORT_ARG_HELP)
@_server.arg('chroot', type=str, help=CHROOT_ARG_HELP)
@_server.arg('bindaddr', type=str, help=BINDADDR_ARG_HELP)
@_server.arg('pidfile', type=str, help=PIDFILE_ARG_HELP)
@_server.arg('defaulthost',type=str, help=DEFAULT_HOST_ARG_HELP)
@_server.arg('accesslog',type=str, help=ACCESS_LOG_ARG_HELP)
@_server.arg('errorlog',type=str, help=ERROR_LOG_ARG_HELP)
@_server.arg('ssl', type=bool, default=False, const=True, nargs='?', help=SSL_ARG_HELP)
@_server.arg('uuid', type=str, help=UUID_ARG_HELP)
def update(id, name=None, port=None, chroot=None, bindaddr=None, pidfile=None,
           defaulthost=None, accesslog=None, errorlog=None, ssl=None, uuid=None):

    with managed(Session) as session:
        server = session.query(Server).get(id)
        if not server:
            print "Server not found! id={0}".format(id)
            return False

        port_verify = session.query(Server).filter_by(port=port).all()
        if port_verify:
            print 'You cannot have two servers on the same port. Server id={id} already uses port {port}'.format(id=port_verify[0].id, port=port)
            return False

        uuid_verify = session.query(Server).filter_by(uuid=uuid).all()
        if uuid_verify:
            print 'You cannot have two servers with the same uuid. Server id={id} already uses uuid {uuid}'.format(id=uuid_verify[0].id, uuid=uuid)
            return False

        server.uuid = _new_value_for_field(uuid, server.uuid)
        server.port = _new_value_for_field(port, server.port)
        server.name = _new_value_for_field(name, server.name)
        server.chroot = _new_value_for_field(chroot, server.chroot)
        server.bind_addr = _new_value_for_field(bindaddr, server.bind_addr)
        server.pid_File = _new_value_for_field(pidfile, server.pid_File)
        server.default_host = _new_value_for_field(defaulthost, server.default_host)
        server.access_log = _new_value_for_field(accesslog, server.access_log)
        server.error_log = _new_value_for_field(errorlog, server.error_log)
        server.use_ssl = _new_value_for_field(ssl, server.use_ssl)

    return "update"

@_server.command
@_server.arg('id', '--id', required=True, type=int, nargs='+', help="Id(s) of the server(s) to be removed.")
def remove(id):
    with managed(Session) as session:
        for server_id in id:
            server = session.query(Server).get(server_id)
            if server:
                server_name = server.name
                session.query(Server).filter_by(id=server_id).delete()
                session.commit()
                print 'Server [{0}] was removed with success.'.format(server_name)
            else:
                print 'Server not found. id={0}'.format(server_id)

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

