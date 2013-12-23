from django.db import models
from django.contrib.auth.models import User
from blogs.models import Blog

class Category(models.Model):
    author = models.ForeignKey(User)
    blog = models.ForeignKey(Blog, null=True)
    slug = models.SlugField(max_length=140, unique=True)
    created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    top_level_cat = models.ForeignKey('self',  null=True, blank=True)
    def __unicode__(self):
        return self.slug
