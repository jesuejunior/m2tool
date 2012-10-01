#encoding: utf-8

import unittest

from m2tool.db import Metadata, Session
from m2tool.db.models import Server
from m2tool.commands.server import server_command

class ServerCommandTest(unittest.TestCase):

    def setUp(self):
        Metadata.drop_all()
        Metadata.create_all()

    def test_create_new_server(self):
        session = Session()
        self.assertEquals(0, len(session.query(Server).all()))

        server_command('localhost', 80, '/var/m2')

        servers = session.query(Server).all()
        self.assertEquals(1, len(servers))
        self.assertEquals('localhost', servers[0].name)
        self.assertEquals(80, servers[0].port)
        self.assertEquals('/var/m2', servers[0].chroot)

    def test_port_duplicate(self):
        session = Session()

        server_command('localhost', 80, '/var/m2')
        server = session.query(Server).filter_by(port=80).all()
        self.assertEquals(1, len(server))

        server_command('localhost', 80, '/var/m2')
        server2 = session.query(Server).filter_by(port=80).all()
        self.assertEquals(1, len(server2))



