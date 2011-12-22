m2tool
------

m2tool is (will be) a command line tool to manage mongrel2 instances. It will provide simple commands to manipulate all mongrel2 config tables: server, routes, handler, directories, etc.

Since m2tool will be written using Django, it will be possible to run it with mongrel2 and control your instances from web.

There are no plans to build any sort of "user interface", all interactions will be done through an API.


Why Django ?
------------

I choosed Django mainly because of its ORM and also because I have plans to run m2tool behind a mongrel2 instance, so I will be able to deploy new apps from my command line.



Dalton Barreto <daltonmatos@gmail.com>

http://daltonmatos.com
