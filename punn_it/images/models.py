from django.db import models
from sorl.thumbnail import ImageField

class Image(models.Model):
    image = ImageField(upload_to='whatever')


