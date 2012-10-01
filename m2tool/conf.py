import os

DIRNAME = '.m2tool'
CFGDIR = os.path.join(os.path.expanduser('~'), DIRNAME)

M2_DB_ENV = 'M2_DB'
M2_DEFAULT_DB_NAME = 'config.sqlite'

M2_DEFAULT_DB_PATH = os.path.join(os.getcwd(), M2_DEFAULT_DB_NAME)
