import unittest
from m2tool.commands.directory import add, remove
from m2tool.db import Metadata, Session
from m2tool.db.directory import Directory

class DirectoryCommandTest(unittest.TestCase):

    def setUp(self):
        Metadata.drop_all()
        Metadata.create_all()

    def test_create_new_directory(self):
        session = Session()
        self.assertEquals(0, len(session.query(Directory).all()))

        add("static/", 'index.html', 'text/html', True)
        dir = session.query(Directory).all()
        self.assertEquals(1, len(dir))
        self.assertEquals("static/", dir[0].base)
        self.assertEquals('index.html', dir[0].index_file)
        self.assertEquals('text/html', dir[0].default_ctype)
        self.assertTrue(dir[0].cache_ttl)

    def test_remove_directory(self):
        session = Session()
        dir = session.query(Directory).all()
        self.assertEquals(0, len(dir))

        add("static/", 'index.html', 'text/html', True)
        dir2 = session.query(Directory).filter_by(base="static/").all()
        self.assertEquals(1, len(dir2))

        remove(id=dir2[0].id)
        dir3 = session.query(Directory).all()
        self.assertEquals(0, len(dir3))

    def test_base_isnull(self):
        session =Session()
        self.assertEquals(0, len(session.query(Directory).all()))
        add(None, 'index.html', 'text/html', False)
        self.assertEquals(0, len(session.query(Directory).all()))

    def test_base_istrue(self):
        session =Session()
        self.assertEquals(0, len(session.query(Directory).all()))
        add(True, 'index.html', 'text/html', False)
        self.assertEquals(0, len(session.query(Directory).all()))