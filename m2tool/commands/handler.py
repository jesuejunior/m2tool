#coding: utf-8
from uuid import uuid4
from clint.textui import columns, puts
from modargs import args
from alchemytools.context import managed

from m2tool.db import Session
from m2tool.db.handler import Handler


def handler_command(arglist):
    '''
    --sendident=UUID --recvident=UUID
    --sendspec=IP:PORT --recvspec=IP:PORT
    --raw_payload=number --protocol=NAME
    '''

    subcommand, params = args.parse(arglist)

    if subcommand in globals():
        globals()[subcommand](**params)
    else:
        print "Subcommand {0} not found".format(subcommand)

def add(sendident=None, sendspec=None, recvident=None,  recvspec=None, rawpayload=0, protocol='json'):
    print "Adding Handler: SEND_SPEC={0},SEND_IDENT={1}, RECV_SPEC={2}, RECV_IDENT={3}".format(sendspec, sendident, recvspec, recvident)

    if not sendspec or not recvspec:
        print "Please verify parameters --sendspec or --recvspec"
        return False

    if not sendident:
        sendident = str(uuid4())
    if not recvident:
        recvident = str(uuid4())
    with managed(Session) as session:

        #verify if exist send_spec and recv_spec
        sendspec_exist = session.query(Handler).filter_by(send_spec=sendspec).count()
        recvspec_exist = session.query(Handler).filter_by(recv_spec=recvspec).count()

        if sendspec_exist:
            print 'SEND_SPEC [{0}] already exists, please check and try another port.'.format(sendspec)
            return False
        if recvspec_exist:
            print 'RECV_SPEC [{0}] already exists, please check and try another port.'.format(recvspec)
            return False

        #verify identity of send and recv
        sendident_verify = session.query(Handler).filter_by(send_ident=sendident).count()
        recvident_verify = session.query(Handler).filter_by(recv_ident=recvident).count()

        if sendident_verify:
            print 'SEND_IDENT [{0}] already exists, please check.'.format(sendident)
            return False
        if recvident_verify:
            print 'RECV_IDENT [{0}] already exists, please check.'.format(recvident)
            return False
        else:
            handler = Handler(send_ident=sendident, recv_ident=recvident, send_spec=sendspec, recv_spec=recvspec,
                raw_payload=rawpayload, protocol=protocol)
        session.add(handler)

def remove(id):
    with managed(Session) as session:
        handler = session.query(Handler).get(id)
        if handler:
            session.query(Handler).filter_by(id=id).delete()
            session.commit()
            print 'Handler ID [{0}] was removed with success.'.format(handler.id)
        else:
            print 'Handler not found.'

def list():
    with managed(Session) as session:
        handlers = session.query(Handler).all()
        if handlers:
            puts(columns(['ID', 4], ['SEND_SPEC', 26], ["SEND_IDENT", 38], ['RECV_SPEC', 26], ["RECV_IDENT", 38],
                ['raw_payload', 12], ['Protocol', 10]))

        for handler in handlers:
            puts(columns([str(handler.id), 4], [handler.send_spec, 26], [handler.send_ident, 38], [handler.recv_spec, 26],
                [handler.send_ident, 38], [str(handler.raw_payload), 12], [handler.protocol, 8]))
