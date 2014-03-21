# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UserProfile.link_color'
        db.delete_column('accounts_userprofile', 'link_color')

        # Deleting field 'UserProfile.twitter_profile'
        db.delete_column('accounts_userprofile', 'twitter_profile')

        # Deleting field 'UserProfile.sites'
        db.delete_column('accounts_userprofile', 'sites_id')

        # Deleting field 'UserProfile.well_color'
        db.delete_column('accounts_userprofile', 'well_color')

        # Deleting field 'UserProfile.facebook_profile'
        db.delete_column('accounts_userprofile', 'facebook_profile')

        # Deleting field 'UserProfile.font_color'
        db.delete_column('accounts_userprofile', 'font_color')

        # Deleting field 'UserProfile.background_color'
        db.delete_column('accounts_userprofile', 'background_color')

        # Adding field 'UserProfile.site'
        db.add_column('accounts_userprofile', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'UserProfile.link_color'
        db.add_column('accounts_userprofile', 'link_color',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=6, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.twitter_profile'
        db.add_column('accounts_userprofile', 'twitter_profile',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=300, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.sites'
        db.add_column('accounts_userprofile', 'sites',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.well_color'
        db.add_column('accounts_userprofile', 'well_color',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=6, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.facebook_profile'
        db.add_column('accounts_userprofile', 'facebook_profile',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=300, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.font_color'
        db.add_column('accounts_userprofile', 'font_color',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=6, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.background_color'
        db.add_column('accounts_userprofile', 'background_color',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=6, blank=True),
                      keep_default=False)

        # Deleting field 'UserProfile.site'
        db.delete_column('accounts_userprofile', 'site_id')


    models = {
        'accounts.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'analytics_account': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '160', 'blank': 'True'}),
            'domain': ('django.db.models.fields.URLField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'pro_user': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['accounts']