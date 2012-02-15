

from m2tool.conf import CFGDIR
import os

class Cli(object):

    def init(self):
        if not os.path.exists(CFGDIR):
            os.mkdir(CFGDIR)

