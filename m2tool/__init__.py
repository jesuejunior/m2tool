
__projectname__ = 'm2tool'

all = ['__projectname__']

from m2tool.conf import CFGDIR
import os

if not os.path.exists(CFGDIR):
    os.mkdir(CFGDIR)
