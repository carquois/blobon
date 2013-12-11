# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blog'
        db.create_table('blogs_blog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=30)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
        ))
        db.send_create_signal('blogs', ['Blog'])


    def backwards(self, orm):
        # Deleting model 'Blog'
        db.delete_table('blogs_blog')


    models = {
        'blogs.blog': {
            'Meta': {'object_name': 'Blog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['blogs']