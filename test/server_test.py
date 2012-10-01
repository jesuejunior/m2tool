#encoding: utf-8

import unittest

from m2tool.db import Metadata

class ServerCommandTest(unittest.TestCase):

    def setUp(self):
        Metadata.drop_all()
        Metadata.create_all()

    def test_create_new_server(self):
        self.fail()