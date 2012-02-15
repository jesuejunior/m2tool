from django.db import models
import os

class Server(models.Model):
  uuid = models.TextField(unique=True)
  access_log = models.TextField()
  error_log = models.TextField()
  chroot = models.TextField(default="/var/www")
  pid_file = models.TextField()
  default_host = models.TextField()
  name = models.TextField()
  bind_addr = models.TextField(default="0.0.0.0")
  port = models.IntegerField()

  class Meta:
    db_table = "server"

  def __unicode__(self):
    return "%s %s:%s" % (self.uuid, self.bind_addr, self.port)


class Host(models.Model):
  server = models.ForeignKey(Server)
  maintenance = models.BooleanField()
  name = models.TextField()
  matching = models.TextField()

  class Meta:
    db_table = "host"

  def __unicode__(self):
    return self.name


class Handler(models.Model):
  class Meta:
    db_table = "handler"

  send_spec = models.TextField()
  send_ident = models.TextField()
  recv_spec = models.TextField()
  recv_ident = models.TextField()
  raw_payload = models.IntegerField(default=0)

  def __unicode__(self):
    return "recv: %s, send: %s" % (self.recv_spec, self.send_spec)

class Directory(models.Model):
  class Meta:
    db_table = "directory"

class Proxy(models.Model):
  class Meta:
    db_table = "diectoryr"


class BaseRoute(models.Model):
  path = models.TextField()
  reversed = models.BooleanField()
  host = models.ForeignKey(Host)
  target_type = models.TextField()
  
  class Meta:
    abstract = True

class HandlerRoute(BaseRoute):
    target = models.ForeignKey(Handler, related_name="target_id")
    
    class Meta:
      db_table = "route"

    def save(self, *args, **kwargs):
      self.target_type = "handler"
      return super(HandlerRoute, self).save(*args, **kwargs)


class DirRoute(BaseRoute):
    target = models.ForeignKey(Directory, related_name="target_id")
    
    class Meta:
      db_table = "route"

    def save(self, *args, **kwargs):
      self.target_type = "dir"
      return super(HandlerRoute, self).save(*args, **kwargs)

class ProxyRoute(BaseRoute):
    target = models.ForeignKey(Proxy, related_name="target_id")
    
    class Meta:
      db_table = "route"

    def save(self, *args, **kwargs):
      self.target_type = "proxy"
      return super(HandlerRoute, self).save(*args, **kwargs)
