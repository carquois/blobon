from django.db import models
from punns.models import Punn
from sorl.thumbnail import ImageField
from punns.utils import BASE10, BASE17, BASE62, baseconvert
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.punn.base62id
    filename = "%s.%s" % (prefix, ext)
    return os.path.join('i', filename)

class Image(models.Model):
    punn = models.OneToOneField(Punn)
    image = ImageField(upload_to=get_file_path, null=True, blank=True)
    def __unicode__(self):
        return str(self.id)


