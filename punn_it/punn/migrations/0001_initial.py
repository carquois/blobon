# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('punn_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=160, blank=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('domain', self.gf('django.db.models.fields.URLField')(max_length=50, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('sites', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(default='en', max_length=2)),
            ('background_color', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('well_color', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('font_color', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('link_color', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('facebook_profile', self.gf('django.db.models.fields.URLField')(max_length=300, blank=True)),
            ('twitter_profile', self.gf('django.db.models.fields.URLField')(max_length=300, blank=True)),
            ('analytics_account', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('punn', ['UserProfile'])

        # Adding model 'Tag'
        db.create_table('punn_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('punn', ['Tag'])

        # Adding model 'Punn'
        db.create_table('punn_punn', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('base62id', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('karma', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('source', self.gf('django.db.models.fields.URLField')(max_length=300, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('original_punn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['punn.Punn'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=300, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.URLField')(max_length=300, blank=True)),
            ('facebook_publication_link', self.gf('django.db.models.fields.URLField')(max_length=300, blank=True)),
            ('tweet_link', self.gf('django.db.models.fields.URLField')(max_length=300, blank=True)),
            ('reddit_link', self.gf('django.db.models.fields.URLField')(max_length=300, blank=True)),
        ))
        db.send_create_signal('punn', ['Punn'])

        # Adding M2M table for field tags on 'Punn'
        db.create_table('punn_punn_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('punn', models.ForeignKey(orm['punn.punn'], null=False)),
            ('tag', models.ForeignKey(orm['punn.tag'], null=False))
        ))
        db.create_unique('punn_punn_tags', ['punn_id', 'tag_id'])

        # Adding model 'Comment'
        db.create_table('punn_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('base62id', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('punn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['punn.Punn'])),
            ('karma', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['punn.Comment'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal('punn', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('punn_userprofile')

        # Deleting model 'Tag'
        db.delete_table('punn_tag')

        # Deleting model 'Punn'
        db.delete_table('punn_punn')

        # Removing M2M table for field tags on 'Punn'
        db.delete_table('punn_punn_tags')

        # Deleting model 'Comment'
        db.delete_table('punn_comment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'punn.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'base62id': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'karma': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['punn.Comment']", 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'punn': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['punn.Punn']"})
        },
        'punn.punn': {
            'Meta': {'object_name': 'Punn'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'base62id': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'facebook_publication_link': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'}),
            'karma': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'original_punn': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['punn.Punn']", 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'reddit_link': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['punn.Tag']", 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'tweet_link': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'})
        },
        'punn.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'punn.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'analytics_account': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'background_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'domain': ('django.db.models.fields.URLField', [], {'max_length': '50', 'blank': 'True'}),
            'facebook_profile': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'}),
            'font_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'link_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'twitter_profile': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'well_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['punn']