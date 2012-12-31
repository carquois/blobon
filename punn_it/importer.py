from httplib2 import Http
from urllib import urlencode
import string, os, sys, getopt
from xml.dom import minidom

dom = minidom.parse("gab.xml")
for node in dom.getElementsByTagName('item'):
  print node.getElementsByTagName('title')[0].firstChild.data
  for meta in node.getElementsByTagName('wp:postmeta'):
    if meta.getElementsByTagName('wp:meta_key')[0].firstChild.data == "via":
      try: 
        print meta.getElementsByTagName('wp:meta_value')[0].firstChild.data
      except AttributeError:
        print "Pas de source, pas grave"
    if meta.getElementsByTagName('wp:meta_key')[0].firstChild.data == "image":
      try: 
        print meta.getElementsByTagName('wp:meta_value')[0].firstChild.data
      except AttributeError:
        print "Pas d'image, on laisse faire"
    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(urllib2.urlopen(meta.getElementsByTagName('wp:meta_value')[0].firstChild.data).read())
    img_temp.flush()
    filename = urlparse(meta.getElementsByTagName('wp:meta_value')[0].firstChild.data).path.split('/')[-1]
    ext = filename.split('.')[-1]
    prefix = new_punn.base62id
    filename = "%s.%s" % (prefix, ext)
    new_punn.pic.save(filename, File(img_temp))
#if meta.getElementsByTagName('wp:meta_key')[0].firstChild.data == "image":
#      print "image"
