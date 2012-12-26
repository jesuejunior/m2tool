#encoding: utf-8
import unittest

from m2tool.db import Metadata, Session
from m2tool.db.handler import Handler
from m2tool.commands.handler import add, remove

class HandlerCommandTest(unittest.TestCase):

    def setUp(self):
        Metadata.drop_all()
        Metadata.create_all()

    def test_create_new_handler_add(self):
        session = Session()
        self.assertEquals(0, len(session.query(Handler).all()))

        add('12e4-abcd-5678-efgh', '12e4-abcd-5678-aaaa', 'tcp://127.0.0.1:5000', 'tcp://127.0.0.1:5001', 0, 'json')

        handlers = session.query(Handler).all()
        self.assertEquals(1, len(handlers))
        self.assertEquals('12e4-abcd-5678-efgh', handlers[0].send_ident)
        self.assertEquals('12e4-abcd-5678-aaaa', handlers[0].recv_ident)
        self.assertEquals('tcp://127.0.0.1:5000', handlers[0].send_spec)
        self.assertEquals('tcp://127.0.0.1:5001', handlers[0].recv_spec)
        self.assertEquals(0, handlers[0].raw_payload)
        self.assertEquals('json', handlers[0].protocol)

    def test_sendident_duplicate(self):
        session = Session()

        add('12e4-abcd-5678-efgh', 'tcp://127.0.0.1:5000', '12e4-abcd-5678-aaaa', 'tcp://127.0.0.1:5001')
        sendident1 = session.query(Handler).filter_by(send_ident='12e4-abcd-5678-efgh').all()
        self.assertEquals(1, len(sendident1))

        add('12e4-abcd-5678-efgh', 'tcp://127.0.0.1:5002', '12e4-abcd-5678-aaaf', 'tcp://127.0.0.1:5003')
        sendident2 = session.query(Handler).filter_by(send_ident='12e4-abcd-5678-efgh').all()
        self.assertEquals(1, len(sendident2))

    def test_recvident_duplicate(self):
        session = Session()

        add('12e4-abcd-5678-efg2', 'tcp://127.0.0.1:5000', '12e4-abcd-5678-aaa7', 'tcp://127.0.0.1:5001')
        recvident1 = session.query(Handler).filter_by(recv_ident='12e4-abcd-5678-aaa7').all()
        self.assertEquals(1, len(recvident1))

        add('12e4-abcd-5678-efgh', 'tcp://127.0.0.1:5002', '12e4-abcd-5678-aaa7', 'tcp://127.0.0.1:5003')
        recvident2 = session.query(Handler).filter_by(recv_ident='12e4-abcd-5678-aaa7').all()
        self.assertEquals(1, len(recvident2))
