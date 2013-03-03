#encoding: utf-8
import unittest
from alchemytools.context import managed

from m2tool.db import Metadata, Session
from m2tool.db.server import Server
from m2tool.commands.server import add, remove

class ServerCommandTest(unittest.TestCase):

    def setUp(self):
        Metadata.drop_all()
        Metadata.create_all()

    def test_create_new_server_add(self):
        session = Session()
        self.assertEquals(0, len(session.query(Server).all()))

        add('localhost-full', 80, '/var/m2', '0.0.0.0', '/run/pid.1', 'jj.com', '/logs/access.log',
            '/logs/error.log', True, '12e4-abcd-5678-efgh')

        servers = session.query(Server).all()
        self.assertEquals(1, len(servers))
        self.assertEquals('localhost-full', servers[0].name)
        self.assertEquals(80, servers[0].port)
        self.assertEquals('/var/m2', servers[0].chroot)
        self.assertEquals('0.0.0.0', servers[0].bind_addr)
        self.assertEquals('/run/pid.1', servers[0].pid_File)
        self.assertEquals('jj.com', servers[0].default_host)
        self.assertEquals('/logs/access.log', servers[0].access_log)
        self.assertEquals('/logs/error.log', servers[0].error_log)
        self.assertTrue(servers[0].use_ssl)
        self.assertEquals('12e4-abcd-5678-efgh', servers[0].uuid)

    def test_port_duplicate(self):
        session = Session()

        add('localhost', 80, '/var/m2')
        server_port = session.query(Server).filter_by(port=80).all()
        self.assertEquals(1, len(server_port))

        add('localhost', 80, '/var/m2')
        server2_port = session.query(Server).filter_by(port=80).all()
        self.assertEquals(1, len(server2_port))

    def test_uuid_duplicate(self):
        session = Session()

        add('localhost', 81, '/var/m2', uuid='1234-abcd-5678-efgh')
        server_uuid = session.query(Server).filter_by(uuid='1234-abcd-5678-efgh').all()
        self.assertEquals(1, len(server_uuid))

        add('localhost2', 80, '/var/m2', uuid='1234-abcd-5678-efgh')
        server2_uuid = session.query(Server).filter_by(uuid='1234-abcd-5678-efgh').all()
        self.assertEquals(1, len(server2_uuid))

    def test_remove_one_server(self):
        remove_server_id = None
        with managed(Session) as session:
            add('teste-remove', 80, '/var/m2', uuid='1234-abcd-5678-efgh')
            server_remove = session.query(Server).filter_by(uuid='1234-abcd-5678-efgh').one()
            self.assertIsNotNone(server_remove)
            remove_server_id = server_remove.id

        remove(id=[remove_server_id])

        with managed(Session) as session:
            server2_rem = session.query(Server).filter_by(uuid='1234-abcd-5678-efgh').all()
            self.assertEquals(0, len(server2_rem))

    def test_remove_more_than_one_server(self):
        with managed(Session) as session:
            session.add(Server(id=1, name='server80', port=80))
            session.add(Server(id=2, name='server81', port=81))
            session.add(Server(id=3, name='server82', port=82))

        remove(id=[1, 2])

        with managed(Session) as session:
            servers = session.query(Server).all()
            self.assertEquals(1, len(servers))
            self.assertEquals(3, servers[0].id)

    def test_remove_server_none(self):
        session = Session()
        server2_qtd = session.query(Server).all()
        remove(id=[200])
        server2_none = session.query(Server).all()
        self.assertEquals(len(server2_qtd), len(server2_none))
