# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Person.plusOneSwitch'
        db.alter_column(u'rsvp_person', 'plusOneSwitch', self.gf('django.db.models.fields.BooleanField')())

    def backwards(self, orm):

        # Changing field 'Person.plusOneSwitch'
        db.alter_column(u'rsvp_person', 'plusOneSwitch', self.gf('django.db.models.fields.NullBooleanField')(null=True))

    models = {
        u'rsvp.invitation': {
            'Meta': {'object_name': 'Invitation'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'helloGoodbyeInvite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'plusOne': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'responded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'rsvp.person': {
            'Meta': {'unique_together': "(('first_name', 'last_name', 'plusOneSwitch'),)", 'object_name': 'Person'},
            'attendingFarewell': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'attendingWedding': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'attendingWelcome': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'people'", 'to': u"orm['rsvp.Invitation']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'plusOneSwitch': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rsvp']