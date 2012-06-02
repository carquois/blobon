# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Image.base62id'
        db.add_column('images_image', 'base62id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=140, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Image.base62id'
        db.delete_column('images_image', 'base62id')


    models = {
        'images.image': {
            'Meta': {'object_name': 'Image'},
            'base62id': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['images']