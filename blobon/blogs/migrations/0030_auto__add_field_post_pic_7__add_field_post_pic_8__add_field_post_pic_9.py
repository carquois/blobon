# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.pic_7'
        db.add_column('blogs_post', 'pic_7',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_8'
        db.add_column('blogs_post', 'pic_8',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_9'
        db.add_column('blogs_post', 'pic_9',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_10'
        db.add_column('blogs_post', 'pic_10',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_11'
        db.add_column('blogs_post', 'pic_11',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_12'
        db.add_column('blogs_post', 'pic_12',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_13'
        db.add_column('blogs_post', 'pic_13',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_14'
        db.add_column('blogs_post', 'pic_14',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_15'
        db.add_column('blogs_post', 'pic_15',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_16'
        db.add_column('blogs_post', 'pic_16',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_17'
        db.add_column('blogs_post', 'pic_17',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_18'
        db.add_column('blogs_post', 'pic_18',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_19'
        db.add_column('blogs_post', 'pic_19',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_20'
        db.add_column('blogs_post', 'pic_20',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_21'
        db.add_column('blogs_post', 'pic_21',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_22'
        db.add_column('blogs_post', 'pic_22',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_23'
        db.add_column('blogs_post', 'pic_23',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.pic_24'
        db.add_column('blogs_post', 'pic_24',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.layout_type'
        db.add_column('blogs_post', 'layout_type',
                      self.gf('django.db.models.fields.CharField')(default='s', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.pic_7'
        db.delete_column('blogs_post', 'pic_7')

        # Deleting field 'Post.pic_8'
        db.delete_column('blogs_post', 'pic_8')

        # Deleting field 'Post.pic_9'
        db.delete_column('blogs_post', 'pic_9')

        # Deleting field 'Post.pic_10'
        db.delete_column('blogs_post', 'pic_10')

        # Deleting field 'Post.pic_11'
        db.delete_column('blogs_post', 'pic_11')

        # Deleting field 'Post.pic_12'
        db.delete_column('blogs_post', 'pic_12')

        # Deleting field 'Post.pic_13'
        db.delete_column('blogs_post', 'pic_13')

        # Deleting field 'Post.pic_14'
        db.delete_column('blogs_post', 'pic_14')

        # Deleting field 'Post.pic_15'
        db.delete_column('blogs_post', 'pic_15')

        # Deleting field 'Post.pic_16'
        db.delete_column('blogs_post', 'pic_16')

        # Deleting field 'Post.pic_17'
        db.delete_column('blogs_post', 'pic_17')

        # Deleting field 'Post.pic_18'
        db.delete_column('blogs_post', 'pic_18')

        # Deleting field 'Post.pic_19'
        db.delete_column('blogs_post', 'pic_19')

        # Deleting field 'Post.pic_20'
        db.delete_column('blogs_post', 'pic_20')

        # Deleting field 'Post.pic_21'
        db.delete_column('blogs_post', 'pic_21')

        # Deleting field 'Post.pic_22'
        db.delete_column('blogs_post', 'pic_22')

        # Deleting field 'Post.pic_23'
        db.delete_column('blogs_post', 'pic_23')

        # Deleting field 'Post.pic_24'
        db.delete_column('blogs_post', 'pic_24')

        # Deleting field 'Post.layout_type'
        db.delete_column('blogs_post', 'layout_type')


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
        'blogs.blog': {
            'Meta': {'object_name': 'Blog'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'custom_domain': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_open': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'translation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Blog']", 'null': 'True', 'blank': 'True'})
        },
        'blogs.category': {
            'Meta': {'object_name': 'Category'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Blog']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '140'}),
            'top_level_cat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Category']", 'null': 'True', 'blank': 'True'})
        },
        'blogs.comment': {
            'Meta': {'object_name': 'Comment'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Blog']", 'null': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'notify_me': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Post']", 'null': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'})
        },
        'blogs.page': {
            'Meta': {'object_name': 'Page'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Blog']", 'null': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'})
        },
        'blogs.post': {
            'Meta': {'object_name': 'Post'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'base62id': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Blog']", 'null': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Category']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'content_0': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'content_01': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'content_1': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'content_2': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'content_3': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'content_4': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'content_5': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'content_6': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'content_video': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_top': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'karma': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'layout_type': ('django.db.models.fields.CharField', [], {'default': "'s'", 'max_length': '1'}),
            'pic': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_0': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_04': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_1': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_10': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_11': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_12': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_13': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_14': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_15': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_16': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_17': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_18': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_19': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_2': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_20': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_21': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_22': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_23': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_24': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_3': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_4': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_5': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_6': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_7': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_8': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pic_9': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'publish_on_facebook': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '140', 'blank': 'True'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '2', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'translated_title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'youtube_url': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'})
        },
        'blogs.tag': {
            'Meta': {'object_name': 'Tag'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Blog']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '140'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blogs']