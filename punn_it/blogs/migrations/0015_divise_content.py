# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."

        gab = orm['auth.User'].objects.get(username="gab")

        b = orm.Blog(is_open=True, slug="rockandpics", title="Rock and Pics", custom_domain="rockandpics.com", creator=gab)
        b.save()

        for post in orm['blogs.Post'].filter(author__username="gabrieldancause"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="furfurfurfur"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="SocialHighlights"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="rockandpics"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="h.ford"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="misterhistory"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="Dali"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="JohnnyGadgets"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="LittleFurBall"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="FamousQuotes"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="AlbumCover"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="ExplosionAndDestruction"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="adrenaline"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="Friendzoned"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="AbandonedPlaces"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="LegoMaster"):
          post.blog = b 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="ArtOfAllKinds"):
          post.blog = b 
          post.save()

        c = orm.Blog(is_open=True, slug="qqpart", title="Quelque part", custom_domain="qqpart.com", creator=gab)
        c.save()
        
        for post in orm['blogs.Post'].filter(author__username="qqpart_old"):
          post.blog = c 
          post.save()

        for post in orm['blogs.Post'].filter(author__username="qqpart"):
          post.blog = c 
          post.save()

        d = orm.Blog(is_open=True, slug="somewr", title="Somewhere", custom_domain="somewr.com", creator=gab)
        d.save()

        for post in orm['blogs.Post'].filter(author__username="somewr"):
          post.blog = d 
          post.save()

        e = orm.Blog(is_open=True, slug="gab", title="Gabriel Dancause", custom_domain="gabrieldancause.com", creator=gab)
        e.save()

        for post in orm['blogs.Post'].filter(author__username="gab"):
          post.blog = e 
          post.save()

    def backwards(self, orm):
        "Write your backwards methods here."

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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_open': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'blogs.category': {
            'Meta': {'object_name': 'Category'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Blog']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
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
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'base62id': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Blog']", 'null': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_top': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_video': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'karma': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'pic': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'publish_on_facebook': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '140', 'blank': 'True'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '2', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'translated_title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'blogs.tag': {
            'Meta': {'object_name': 'Tag'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Blog']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '140'})
        },
        'comments.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'base62id': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'karma': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['comments.Comment']", 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'punn': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['punns.Punn']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'punns.album': {
            'Meta': {'object_name': 'Album'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'base62id': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        'punns.cat': {
            'Meta': {'object_name': 'Cat'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_top_level': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '140'}),
            'top_level_cat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['punns.Cat']", 'null': 'True', 'blank': 'True'})
        },
        'punns.favorite': {
            'Meta': {'object_name': 'Favorite'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'punn': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['punns.Punn']"})
        },
        'punns.link': {
            'Meta': {'object_name': 'Link'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['punns.Album']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'punn': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['punns.Punn']"})
        },
        'punns.punn': {
            'Meta': {'object_name': 'Punn'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'base62id': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'cat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['punns.Cat']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_top': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_video': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'karma': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'original_punn': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['punns.Punn']", 'null': 'True', 'blank': 'True'}),
            'pic': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'publish_on_facebook': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '140', 'blank': 'True'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['punns.Tags']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'translated_title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'punns.reblog': {
            'Meta': {'object_name': 'Reblog'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['punns.Punn']"})
        },
        'punns.tags': {
            'Meta': {'object_name': 'Tags'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['punns', 'auth', 'comments', 'blogs']
    symmetrical = True
