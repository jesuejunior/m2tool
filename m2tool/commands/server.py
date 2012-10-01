from uuid import uuid4

def server_command(name, port, chroot=None,  bindaddr=None, pidfile=None,
                   defaulthost=None, accesslog=None, errorlog=None, ssl=None,uuid=None ):
    '''
    --uuid=UUID --accesslog=FILE --errorlog=FILE
    --chroot=PATH --pidfile=FILE --name=NAME
    --bindaddr=IP --port=PORT --ssl
    --defaulthost=HOSTNAME
    '''
    if not uuid:
        uuid = str(uuid4())

    if not chroot:
        chroot = '/var/mongrel2'

    if not bindaddr:
    #Accept connection from any host
        bindaddr = '0.0.0.0'


    print uuid
    print "command_server"
    print "Adicionando servidor {0} porta {1}".format(name, port)