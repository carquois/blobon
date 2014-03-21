from sorl.thumbnail.base import ThumbnailBackend
from os.path import basename
from django.conf import settings
from sorl.thumbnail.helpers import tokey, serialize

class PunnItThumbnailBackend(ThumbnailBackend):
    def _get_thumbnail_filename(self, source, geometry_string, options):
        key = tokey(source.key, geometry_string, serialize(options))
        return 't/%s/%s' % (geometry_string, basename(source.name))