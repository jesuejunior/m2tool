


import unittest
from m2tool.cli import Cli
from m2tool.conf import CFGDIR
from mock import patch

class ConfigDirTest(unittest.TestCase):

    def setUp(self):
        self.cli = Cli()

    def test_create_config_dir(self):
        with patch('os.path.exists') as exist:
            with patch('os.mkdir') as mkdir:
                exist.return_value = False
                self.cli.init()
                exist.assert_called_with(CFGDIR)
                mkdir.assert_called_with(CFGDIR)
