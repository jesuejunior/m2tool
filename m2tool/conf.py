import os

DIRNAME = '.m2tool'
CFGDIR = os.path.join(os.path.expanduser('~'), DIRNAME)

M2_DB_ENV = 'M2_DB'
M2_DEFAULT_DB_NAME = 'config.sqlite'

M2_DEFAULT_DB_PATH = os.path.join(os.getcwd(), M2_DEFAULT_DB_NAME)


# Defaults for Server model
DEFAULT_CHROOT = "/var/mongrel2"
DEFAULT_BIND_ADDR = "0.0.0.0"
DEFAULT_PIDFILE = "/run/mongrel2.pid"
DEFAULT_ACCESS_LOG_FILE = "/logs/access.log"
DEFAULT_ERROR_LOG_FILE = "/logs/error.log"
DEFAULT_SSL = False
