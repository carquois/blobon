# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Comment.author'
        db.add_column('blogs_comment', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='Comment_author', null=True, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Comment.author'
        db.delete_column('blogs_comment', 'author_id')


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
            'block_css': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_footer': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_header': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_left': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_middle': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_navbar': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_other_1': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_other_2': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_other_3': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_right': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_right_bottom': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_right_middle_1': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_right_middle_2': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_right_top': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_single_left': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_subscribe_button': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_subscribe_text': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'block_title': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'custom_domain': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'has_template': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_online': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_open': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'moderator_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
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
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Comment_author'", 'null': 'True', 'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Blog']", 'null': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'comment_status': ('django.db.models.fields.CharField', [], {'default': "'pe'", 'max_length': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'notify_me': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Post']", 'null': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'})
        },
        'blogs.info_email': {
            'Meta': {'object_name': 'Info_email'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Blog']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'frequency': ('django.db.models.fields.CharField', [], {'default': "'We'", 'max_length': '2', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'subject': ('django.db.models.fields.TextField', [], {'max_length': '100', 'blank': 'True'}),
            'subscribers': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '2', 'null': 'True'})
        },
        'blogs.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'language_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
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
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['blogs.Category']", 'null': 'True', 'blank': 'True'}),
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
            'is_ready': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_top': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'karma': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'layout_type': ('django.db.models.fields.CharField', [], {'default': "'s'", 'max_length': '1'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
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
            'text': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'translated_content': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'translated_title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'youtube_url': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'})
        },
        'blogs.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Blog']", 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_new': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
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
        'blogs.translation': {
            'Meta': {'object_name': 'Translation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'origin_blog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Translation_origin_blog'", 'null': 'True', 'to': "orm['blogs.Blog']"}),
            'translated_blog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Translation_translated_blog'", 'null': 'True', 'to': "orm['blogs.Blog']"})
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