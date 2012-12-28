#coding: utf-8
from uuid import uuid4
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

    if not sendident:
        sendident = str(uuid4())
    if not recvident:
        recvident = str(uuid4())
    with managed(Session) as session:

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

def remove():
    return None