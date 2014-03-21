from django import template
from django.template.defaultfilters import stringfilter
import os
import Image
register = template.Library()

@register.filter
def is_animated_gif(file):
    gif= Image.open(file.path)
    try:
        gif.seek(1)
    except EOFError:
        is_animated= False
    else:
        is_animated= True

    return is_animated

@register.filter
def filetype(file):
    name, extension = os.path.splitext(file.path)
    return extension[1:].lower()