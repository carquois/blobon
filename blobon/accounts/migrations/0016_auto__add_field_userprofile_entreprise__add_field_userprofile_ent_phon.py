# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserProfile.entreprise'
        db.add_column('accounts_userprofile', 'entreprise',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.ent_phone'
        db.add_column('accounts_userprofile', 'ent_phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.ent_street_adress'
        db.add_column('accounts_userprofile', 'ent_street_adress',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.ent_city'
        db.add_column('accounts_userprofile', 'ent_city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.ent_postal_code'
        db.add_column('accounts_userprofile', 'ent_postal_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.ent_country'
        db.add_column('accounts_userprofile', 'ent_country',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.ent_state'
        db.add_column('accounts_userprofile', 'ent_state',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.ent_first_name'
        db.add_column('accounts_userprofile', 'ent_first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.ent_last_name'
        db.add_column('accounts_userprofile', 'ent_last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserProfile.entreprise'
        db.delete_column('accounts_userprofile', 'entreprise')

        # Deleting field 'UserProfile.ent_phone'
        db.delete_column('accounts_userprofile', 'ent_phone')

        # Deleting field 'UserProfile.ent_street_adress'
        db.delete_column('accounts_userprofile', 'ent_street_adress')

        # Deleting field 'UserProfile.ent_city'
        db.delete_column('accounts_userprofile', 'ent_city')

        # Deleting field 'UserProfile.ent_postal_code'
        db.delete_column('accounts_userprofile', 'ent_postal_code')

        # Deleting field 'UserProfile.ent_country'
        db.delete_column('accounts_userprofile', 'ent_country')

        # Deleting field 'UserProfile.ent_state'
        db.delete_column('accounts_userprofile', 'ent_state')

        # Deleting field 'UserProfile.ent_first_name'
        db.delete_column('accounts_userprofile', 'ent_first_name')

        # Deleting field 'UserProfile.ent_last_name'
        db.delete_column('accounts_userprofile', 'ent_last_name')


    models = {
        'accounts.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'analytics_account': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created_with_provider': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'display_type': ('django.db.models.fields.CharField', [], {'default': "'th'", 'max_length': '2'}),
            'domain': ('django.db.models.fields.URLField', [], {'max_length': '50', 'blank': 'True'}),
            'ent_city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ent_country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ent_first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ent_last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ent_phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ent_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ent_state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ent_street_adress': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'entreprise': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'facebook_link': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'fan_page_access_token': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            'fb_avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fb_friends': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fb_likes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fr_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'french_related_user'", 'null': 'True', 'to': "orm['auth.User']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_new_from_social': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_obox_client': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'main_blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Blog']", 'null': 'True', 'blank': 'True'}),
            'pro_user': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publication_frequency': ('django.db.models.fields.CharField', [], {'default': "'30m'", 'max_length': '3'}),
            'twitter_link': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'twitter_oauth_token': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'twitter_oauth_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
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
            'draft_notice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'facebook_link': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'has_artists': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'header_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_bootblog': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_online': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_open': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '7', 'blank': 'True'}),
            'main_color': ('django.db.models.fields.CharField', [], {'default': "'#ff7f00'", 'max_length': '10'}),
            'moderator_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Template']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'translation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blogs.Blog']", 'null': 'True', 'blank': 'True'}),
            'twitter_link': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'twitter_oauth_token': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'twitter_oauth_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'blogs.template': {
            'Meta': {'object_name': 'Template'},
            'archives': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'base': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'category': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'single': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['accounts']