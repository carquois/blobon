#!/usr/bin/env python
# -*- coding: utf-8 -*-

###IMPORTS###
#Django
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.utils.safestring import mark_safe 
from django.conf.global_settings import LANGUAGES
from punns.utils import BASE10, BASE62, baseconvert

import uuid
import os
from random import choice
from sorl.thumbnail import ImageField

from blogs.utils import unique_slugify

PRIVACY = (
    ('Pu', 'Public'),
    ('Pr', 'Private'),
)

STATUS = (
    ('P', 'Publish'),
    ('D', 'Draft'),
)
FREQUENCY = (
    ('Da', 'Daily'),
    ('We', 'Weekly'),
    ('Mo', 'Monthly'),
    ('Ep', 'After each post'),
)
SUBSCRIBERS = (
    ('A', 'All'),
    ('N', 'New'),
)


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    filename = "%s.%s" % (prefix, ext)
    return os.path.join('', filename)

def get_file_path_0(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('0')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_1(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('1')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_2(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('2')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_3(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('3')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_4(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('4')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_04(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('04')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_5(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('5')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_6(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('6')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_7(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('7')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_8(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('8')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_9(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('9')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_10(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('10')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_11(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('11')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_12(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('12')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_13(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('13')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_14(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('14')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_15(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('15')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_16(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('16')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_17(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('17')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_18(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('18')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_19(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('19')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_20(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('20')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_21(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('21')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_22(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('22')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_23(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('23')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_24(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('24')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_25(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('25')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_26(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('26')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_27(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('27')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_28(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('28')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_29(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('29')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_30(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('30')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_31(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('31')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_32(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('32')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_33(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.base62id
    variable = ('33')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_main(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.id
    variable = ('main')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_cat(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.id
    variable = ('cat')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_cat_email(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.id
    variable = ('email')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_cat_fb(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.id
    variable = ('fb')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_cat_tw(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.id
    variable = ('tw')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_cat_pint(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.id
    variable = ('pint')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_cat_caret(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.id
    variable = ('caret')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_cat_left(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.id
    variable = ('left')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_cat_right(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.id
    variable = ('right')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

def get_file_path_cat_close(instance, filename):
    ext = filename.split('.')[-1]
    prefix = instance.id
    variable = ('close')
    filename = "%s_%s.%s" % (prefix, variable, ext)
    return os.path.join('', filename)

class Template(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=60)
    base = models.TextField(verbose_name=_("Base"), max_length=10000, blank=True)
    single = models.TextField(verbose_name=_("Single"), max_length=10000, blank=True)
    category = models.TextField(verbose_name=_("Category"), max_length=10000, blank=True)
    archives = models.TextField(verbose_name=_("Archives"), max_length=10000, blank=True) 
    def __unicode__(self):
        return self.name

class Blog(models.Model):
    creator = models.ForeignKey(User, null=True)
    moderator_email = models.EmailField(verbose_name=_("Moderator email"),blank=True, null=True)
    is_open = models.BooleanField(default=True)
    slug = models.SlugField(verbose_name=_("URL"), max_length=30, unique=True)
    title = models.CharField(verbose_name=_("Title"), max_length=240)
    facebook_link = models.URLField(max_length=100, blank=True)
    twitter_link = models.URLField(max_length=100, blank=True)
    pinterest_link = models.URLField(max_length=100, blank=True)
    twitter_oauth_token = models.CharField(max_length=100, blank=True)
    twitter_oauth_token_secret = models.CharField(max_length=100, blank=True)
    header_image = ImageField(verbose_name=_("Main image"), upload_to=get_file_path_main, null=True, blank=True)
    main_color = models.CharField(verbose_name=_("Main color"),max_length=10, default="#ff7f00", blank=False)
    language = models.CharField(max_length=7, choices=LANGUAGES,blank=True)
    password = models.CharField(verbose_name=_("Password"), max_length=140, blank=True)
    custom_domain = models.CharField(verbose_name=_("Custom domain"), max_length=300, blank=True)
    description = models.CharField(verbose_name=_("Description"), max_length=500, blank=True)
    translation = models.ForeignKey('self',  null=True, blank=True)
    is_online = models.BooleanField(default=True)
    is_bootblog = models.BooleanField(default=True)
    has_artists = models.BooleanField(default=False)
    short_description = models.CharField(verbose_name=_("Short description"), max_length=140, blank=True)
    draft_notice = models.BooleanField(default=False)
    template = models.ForeignKey(Template, null=True, blank=True)
    def __unicode__(self):
        return self.title



class Rss(models.Model):
    feed_url = models.URLField(verbose_name=_("Feed url"), max_length=300, blank=True)
    blog = models.ForeignKey(Blog, related_name="Blog_rss", null=True)
    def __unicode__(self):
        return self.feed_url


class Page(models.Model):
    blog = models.ForeignKey(Blog, related_name="Blog_page", null=True)
    author = models.ForeignKey(User, null=True)
    status = models.CharField(max_length=2, choices=STATUS)
    title = models.CharField(verbose_name=_("Title"), max_length=140, blank=True)
    content = models.TextField(verbose_name=_("Content"),max_length=10000, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    pub_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    last_modified = models.DateTimeField(auto_now = True,  null=True, blank=True)
    slug = models.SlugField(max_length=140, blank=True)
    def __unicode__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.title)
        super(Page, self).save(*args, **kwargs)


class Info_email(models.Model):
    blog = models.ForeignKey(Blog, null=True)
    author = models.ForeignKey(User, null=True)
    status = models.CharField(max_length=2, choices=STATUS)
    name = models.CharField(verbose_name=_("Title"), max_length=140, blank=True)
    message = models.TextField(verbose_name=_("Message"),max_length=10000, blank=True)
    subject = models.TextField(verbose_name=_("Subject"), max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    frequency = models.CharField(max_length=2, choices=FREQUENCY, default="We", null=True)
    subscribers = models.CharField(max_length=2, choices=SUBSCRIBERS, default="A", null=True)
    def __unicode__(self):
        return self.name

class Category(models.Model):
    author = models.ForeignKey(User)
    blog = models.ForeignKey(Blog, related_name="Blog_category", null=True)
    name = models.CharField(verbose_name=_("Name"), max_length=140, null=True, blank=True)
    description = models.CharField(verbose_name=_("Description"), max_length=1000, null=True, blank=True)
    slug = models.SlugField(max_length=140, blank=True)
    created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    color = models.CharField(verbose_name=_("Main color"),max_length=10, default="#000000", blank=False)
    parent_category = models.ForeignKey('self',  null=True, blank=True, related_name='child_category')
    cat_image = ImageField(verbose_name=_("Cat image"), upload_to=get_file_path_cat, null=True, blank=True)
    cat_image_email = ImageField(verbose_name=_("Cat email image"), upload_to=get_file_path_cat_email, null=True, blank=True)
    cat_image_fb = ImageField(verbose_name=_("Cat fb image"), upload_to=get_file_path_cat_fb, null=True, blank=True)
    cat_image_tw = ImageField(verbose_name=_("Cat tw image"), upload_to=get_file_path_cat_tw, null=True, blank=True)
    cat_image_pint = ImageField(verbose_name=_("Cat pint image"), upload_to=get_file_path_cat_pint, null=True, blank=True)
    cat_image_caret = ImageField(verbose_name=_("Cat caret image"), upload_to=get_file_path_cat_caret, null=True, blank=True)     
    cat_image_left = ImageField(verbose_name=_("Cat caret left"), upload_to=get_file_path_cat_left, null=True, blank=True)
    cat_image_right = ImageField(verbose_name=_("Cat caret right"), upload_to=get_file_path_cat_right, null=True, blank=True)
    cat_image_close = ImageField(verbose_name=_("Cat close"), upload_to=get_file_path_cat_close, null=True, blank=True)    
    def __unicode__(self):
        if self.parent_category:
          return u'%s -  %s' % (self.parent_category, self.name)
        else:
          return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
	    unique_slugify(self, self.name)
        super(Category, self).save(*args, **kwargs)

class Menu(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=40)
    blog = models.ForeignKey(Blog, related_name="Blog_menu", null=True)
    is_main = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=40, blank=True)
    menu = models.ForeignKey(Menu, null=True)
    page = models.ForeignKey(Page, blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    external_link = models.URLField(max_length=140, blank=True)
    position = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return self.title

class Tag(models.Model):
    author = models.ForeignKey(User)
    blog = models.ForeignKey(Blog, related_name="Blog_tag", null=True)
    name = models.CharField(verbose_name=_("Name"), max_length=140, null=True, blank=True)
    description = models.CharField(verbose_name=_("Description"), max_length=1000, null=True, blank=True)
    slug = models.SlugField(max_length=140, unique=True)
    created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    def __unicode__(self):
        return self.slug 
    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.name)
        super(Tag, self).save(*args, **kwargs)



class Post(models.Model):
    author = models.ForeignKey(User, null=True)
    created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True,  null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    base62id = models.CharField(max_length=140, blank=True)
    blog = models.ForeignKey(Blog, null=True)
    title = models.CharField(verbose_name=_("Title"), max_length=140, blank=True)
    status = models.CharField(max_length=2, choices=STATUS, default="P", null=True)
    translated_title = models.CharField(verbose_name=_("Titre traduit"), max_length=140, blank=True)
    slug = models.SlugField(max_length=140, blank=True)
    karma = models.IntegerField(default=0)
    views = models.IntegerField(default=0, blank=True)
    source = models.URLField(verbose_name=_("Source"), max_length=300, blank=True)
    content = models.TextField(verbose_name=_("Contenu"),max_length=10000, blank=True)
    is_top = models.BooleanField(default=False)
    is_sticky = models.BooleanField(default=False)
    is_discarded = models.BooleanField(default=False)
    publish_on_facebook = models.BooleanField(default=False)
    youtube_id = models.CharField(max_length=50, null=True, blank=True)
    vimeo_id = models.CharField(max_length=50, null=True, blank=True)
    vimeo_thumb_url = models.URLField(verbose_name=_("Vimeo thumb URL"), max_length=300, blank=True)
    soundcloud_id = models.CharField(max_length=500, null=True, blank=True) 
    video = models.FileField(verbose_name=_("Video"), upload_to=get_file_path, null=True, blank=True)
    video_ogg = models.FileField(verbose_name=_("Video"), upload_to=get_file_path, null=True, blank=True)
    pic = ImageField(verbose_name=_("Image"), upload_to=get_file_path, null=True, blank=True)
    pic_0 = ImageField(verbose_name=_("Image_0"), upload_to=get_file_path_0, null=True, blank=True)
    pic_1 = ImageField(verbose_name=_("Image_1"), upload_to=get_file_path_1, null=True, blank=True)
    pic_2 = ImageField(verbose_name=_("Image_2"), upload_to=get_file_path_2, null=True, blank=True)
    pic_3 = ImageField(verbose_name=_("Image_3"), upload_to=get_file_path_3, null=True, blank=True)
    pic_4 = ImageField(verbose_name=_("Image_4"), upload_to=get_file_path_4, null=True, blank=True)
    pic_5 = ImageField(verbose_name=_("Image_5"), upload_to=get_file_path_5, null=True, blank=True)
    pic_6 = ImageField(verbose_name=_("Image_6"), upload_to=get_file_path_6, null=True, blank=True)
    pic_7 = ImageField(verbose_name=_("Image_7"), upload_to=get_file_path_7, null=True, blank=True)
    pic_8 = ImageField(verbose_name=_("Image_8"), upload_to=get_file_path_8, null=True, blank=True)
    pic_9 = ImageField(verbose_name=_("Image_9"), upload_to=get_file_path_9, null=True, blank=True)
    pic_10 = ImageField(verbose_name=_("Image_10"), upload_to=get_file_path_10, null=True, blank=True)
    pic_11 = ImageField(verbose_name=_("Image_11"), upload_to=get_file_path_11, null=True, blank=True)
    pic_12 = ImageField(verbose_name=_("Image_12"), upload_to=get_file_path_12, null=True, blank=True)
    pic_13 = ImageField(verbose_name=_("Image_13"), upload_to=get_file_path_13, null=True, blank=True)
    pic_14 = ImageField(verbose_name=_("Image_14"), upload_to=get_file_path_14, null=True, blank=True)
    pic_15 = ImageField(verbose_name=_("Image_15"), upload_to=get_file_path_15, null=True, blank=True)
    pic_16 = ImageField(verbose_name=_("Image_16"), upload_to=get_file_path_16, null=True, blank=True)
    pic_17 = ImageField(verbose_name=_("Image_17"), upload_to=get_file_path_17, null=True, blank=True)
    pic_18 = ImageField(verbose_name=_("Image_18"), upload_to=get_file_path_18, null=True, blank=True)
    pic_19 = ImageField(verbose_name=_("Image_19"), upload_to=get_file_path_19, null=True, blank=True)
    pic_20 = ImageField(verbose_name=_("Image_20"), upload_to=get_file_path_20, null=True, blank=True)
    pic_21 = ImageField(verbose_name=_("Image_21"), upload_to=get_file_path_21, null=True, blank=True)
    pic_22 = ImageField(verbose_name=_("Image_22"), upload_to=get_file_path_22, null=True, blank=True)
    pic_23 = ImageField(verbose_name=_("Image_23"), upload_to=get_file_path_23, null=True, blank=True)
    pic_24 = ImageField(verbose_name=_("Image_24"), upload_to=get_file_path_24, null=True, blank=True)
    pic_25 = ImageField(verbose_name=_("Image_25"), upload_to=get_file_path_25, null=True, blank=True)
    pic_26 = ImageField(verbose_name=_("Image_26"), upload_to=get_file_path_26, null=True, blank=True)
    pic_27 = ImageField(verbose_name=_("Image_27"), upload_to=get_file_path_27, null=True, blank=True)
    pic_28 = ImageField(verbose_name=_("Image_28"), upload_to=get_file_path_28, null=True, blank=True)
    pic_29 = ImageField(verbose_name=_("Image_29"), upload_to=get_file_path_29, null=True, blank=True)
    pic_30 = ImageField(verbose_name=_("Image_30"), upload_to=get_file_path_30, null=True, blank=True)
    pic_31 = ImageField(verbose_name=_("Image_31"), upload_to=get_file_path_31, null=True, blank=True)
    pic_32 = ImageField(verbose_name=_("Image_32"), upload_to=get_file_path_32, null=True, blank=True)
    pic_33 = ImageField(verbose_name=_("Image_33"), upload_to=get_file_path_33, null=True, blank=True)
    pic_04 = ImageField(verbose_name=_("Image_04"), upload_to=get_file_path_04, null=True, blank=True)
    text = models.TextField(verbose_name=_("Text"),max_length=10000, blank=True)
    translated_content = models.TextField(verbose_name=_("Contenu traduit"),max_length=10000, blank=True)
    is_ready = models.BooleanField(default=True)
    message = models.TextField(verbose_name=_("Message"),max_length=10000, blank=True)
    content_0 = models.TextField(verbose_name=_("Content_0"),max_length=10000, blank=True)
    content_01 = models.TextField(verbose_name=_("Content_01"),max_length=10000, blank=True)
    content_1 = models.TextField(verbose_name=_("Content_1"),max_length=10000, blank=True)
    content_2 = models.TextField(verbose_name=_("Content_2"),max_length=10000, blank=True)
    content_3 = models.TextField(verbose_name=_("Content_3"),max_length=10000, blank=True)
    content_4 = models.TextField(verbose_name=_("Content_4"),max_length=10000, blank=True)
    content_5 = models.TextField(verbose_name=_("Content_5"),max_length=10000, blank=True)
    content_6 = models.TextField(verbose_name=_("Content_6"),max_length=10000, blank=True)
    content_video = models.TextField(verbose_name=_("Content_video"),max_length=10000, blank=True)
    video_url = models.URLField(verbose_name=_("Video URL"), max_length=300, blank=True)
    soundcloud_url = models.URLField(verbose_name=_("Soundcloud URL"), max_length=300, blank=True) 
    category = models.ManyToManyField(Category, null=True, blank=True)
    tag = models.ManyToManyField(Tag, null=True, blank=True)
    artist = models.CharField(verbose_name=_("Artist"), max_length=140, blank=True)
    LAYOUT_CHOICES = (
        ('s', 'Single'),
        ('v', 'Vertical'),
        ('h', 'Horizontal'),
        ('g', 'Grid'),
    )
    layout_type = models.CharField(default="s", max_length=1, choices=LAYOUT_CHOICES)
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.base62id:
            self.base62id = Post.generate_unique_id()
        return super(Post, self).save(*args, **kwargs)

    def file_extension(self):
        basename, extension = os.path.splitext(self.pic.name) 
        return extension

    def file_extension_0(self):
        basename, extension = os.path.splitext(self.pic_0.name)
        return extension

    def file_extension_1(self):
        basename, extension = os.path.splitext(self.pic_1.name)
        return extension

    def file_extension_2(self):
        basename, extension = os.path.splitext(self.pic_2.name)
        return extension

    def file_extension_3(self):
        basename, extension = os.path.splitext(self.pic_3.name)
        return extension

    def file_extension_4(self):
        basename, extension = os.path.splitext(self.pic_4.name)
        return extension

    def file_extension_5(self):
        basename, extension = os.path.splitext(self.pic_5.name)
        return extension

    def file_extension_6(self):
        basename, extension = os.path.splitext(self.pic_6.name)
        return extension

    def file_extension_7(self):
        basename, extension = os.path.splitext(self.pic_7.name)
        return extension

    def file_extension_8(self):
        basename, extension = os.path.splitext(self.pic_8.name)
        return extension

    def file_extension_9(self):
        basename, extension = os.path.splitext(self.pic_9.name)
        return extension

    def file_extension_10(self):
        basename, extension = os.path.splitext(self.pic_10.name)
        return extension

    def file_extension_11(self):
        basename, extension = os.path.splitext(self.pic_11.name)
        return extension

    def file_extension_12(self):
        basename, extension = os.path.splitext(self.pic_12.name)
        return extension

    def file_extension_13(self):
        basename, extension = os.path.splitext(self.pic_13.name)
        return extension

    def file_extension_14(self):
        basename, extension = os.path.splitext(self.pic_14.name)
        return extension

    def file_extension_15(self):
        basename, extension = os.path.splitext(self.pic_15.name)
        return extension

    def file_extension_16(self):
        basename, extension = os.path.splitext(self.pic_16.name)
        return extension

    def file_extension_17(self):
        basename, extension = os.path.splitext(self.pic_17.name)
        return extension

    def file_extension_18(self):
        basename, extension = os.path.splitext(self.pic_18.name)
        return extension

    def file_extension_19(self):
        basename, extension = os.path.splitext(self.pic_19.name)
        return extension

    def file_extension_20(self):
        basename, extension = os.path.splitext(self.pic_20.name)
        return extension

    def file_extension_21(self):
        basename, extension = os.path.splitext(self.pic_21.name)
        return extension

    def file_extension_22(self):
        basename, extension = os.path.splitext(self.pic_22.name)
        return extension

    def file_extension_23(self):
        basename, extension = os.path.splitext(self.pic_23.name)
        return extension

    def file_extension_24(self):
        basename, extension = os.path.splitext(self.pic_24.name)
        return extension

    def file_extension_25(self):
        basename, extension = os.path.splitext(self.pic_25.name)
        return extension

    def file_extension_26(self):
        basename, extension = os.path.splitext(self.pic_26.name)
        return extension

    def file_extension_27(self):
        basename, extension = os.path.splitext(self.pic_27.name)
        return extension

    def file_extension_28(self):
        basename, extension = os.path.splitext(self.pic_28.name)
        return extension

    def file_extension_29(self):
        basename, extension = os.path.splitext(self.pic_29.name)
        return extension

    def file_extension_30(self):
        basename, extension = os.path.splitext(self.pic_30.name)
        return extension

    def file_extension_31(self):
        basename, extension = os.path.splitext(self.pic_31.name)
        return extension

    def file_extension_32(self):
        basename, extension = os.path.splitext(self.pic_32.name)
        return extension

    def file_extension_33(self):
        basename, extension = os.path.splitext(self.pic_33.name)
        return extension

    @models.permalink
    def get_absolute_url(self):
        return ('blogs.views.single', [str(self.base62id)])

    @classmethod
    def generate_unique_id(cls):
        chars = ('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')
        id_exists = False
        while not id_exists:
            rnd_str=""
            for i in range(8):
                rnd_str = rnd_str + choice(chars)
            try:
                post = cls.objects.get(base62id=rnd_str)
                id_exists = True
            except cls.DoesNotExist:
                return rnd_str

class Comment(models.Model):
    post = models.ForeignKey(Post, null=True)
    blog = models.ForeignKey(Blog, null=True)
    comment = models.TextField(verbose_name=_("Content"),max_length=10000)
    email = models.EmailField(verbose_name=_("Email"))
    name = models.CharField(verbose_name=_("Name"), max_length=140)
    website = models.URLField(verbose_name=_("Website"), max_length=300, blank=True)
    author = models.ForeignKey(User, related_name='Comment_author',blank=True, null=True)
    notify_me = models.BooleanField(default=False)
    COMMENTS_CHOICES = (
        ('pe', 'Pending'),
        ('pu', 'Published'),
        ('sp', 'Spam'),
    )
    comment_status = models.CharField(default="pe", max_length=2, choices=COMMENTS_CHOICES)
    occupation = models.CharField(verbose_name=_("Occupation"), max_length=50,blank=True, null=True)
    def __unicode__(self):
        return self.comment


class Subscription(models.Model):
    blog = models.ForeignKey(Blog, null=True)
    email = models.EmailField(verbose_name=_("Email"))
    is_new = models.BooleanField(default=True)
    def __unicode__(self):
        return self.email

class Language(models.Model):
    language_name = models.CharField(verbose_name=_("Language_name"), max_length=40)
    language_code = models.CharField(verbose_name=_("Language_code"), max_length=5)
    def __unicode__(self):
        return self.language_name

class Translation(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=40)
    origin_blog = models.ForeignKey(Blog, related_name='Translation_origin_blog', null=True)
    translated_blog = models.ForeignKey(Blog, related_name='Translation_translated_blog', null=True)
    def __unicode__(self):
        return self.name

#class Video(Post):
#    video_title = models.CharField(verbose_name=_("Title"), max_length=140, blank=True)
#    content = models.TextField(verbose_name=_("Content"),max_length=10000, blank=True)
#    youtube_id = models.CharField(max_length=50, null=True, blank=True)
#    def __unicode__(self):
#        return str(self.id)
#
#class Album(Post):
#    title = models.CharField(verbose_name=_("Titre"), max_length=140)
#    content = models.TextField(verbose_name=_("Contenu"),max_length=10000, blank=True)
#    def __unicode__(self):
#        return str(self.id)
#
#class Link(models.Model):
#    image = models.ForeignKey(Image)
#    album = models.ForeignKey(Album)
#    order = models.PositiveIntegerField()
#    def __unicode__(self):
#        return str(self.id)
#

