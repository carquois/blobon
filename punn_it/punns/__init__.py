from cStringIO import StringIO

try:
    from PIL import Image, ImageFile, ImageDraw
except ImportError:
    import Image, ImageFile, ImageDraw
    
from sorl.thumbnail.engines.pil_engine import Engine

def my_get_raw_data(self, image, format_, quality, progressive=False):
    ImageFile.MAXBLOCK = 1024 * 1024 * 10
    buf = StringIO()
    params = {
        'format': format_,
        'quality': quality,
        'optimize': 1,
    }
    if format_ == 'JPEG' and progressive:
        params['progressive'] = True
    try:
        image.save(buf, **params)
    except IOError:
        params.pop('optimize')
        image.save(buf, **params)
    raw_data = buf.getvalue()
    buf.close()
    return raw_data

Engine._get_raw_data = my_get_raw_data