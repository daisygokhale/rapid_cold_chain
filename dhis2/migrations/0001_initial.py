# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrganisationUnit'
        db.create_table(u'dhis2_organisationunit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('dhis2_id', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('i18n_name', self.gf('jsonfield.fields.JSONField')()),
            ('dhis2_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['dhis2.OrganisationUnit'])),
        ))
        db.send_create_signal(u'dhis2', ['OrganisationUnit'])

        # Adding model 'Facility'
        db.create_table(u'dhis2_facility', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('dhis2_id', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('i18n_name', self.gf('jsonfield.fields.JSONField')()),
            ('dhis2_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dhis2.OrganisationUnit'], null=True, blank=True)),
        ))
        db.send_create_signal(u'dhis2', ['Facility'])

        # Adding model 'Equitment'
        db.create_table(u'dhis2_equitment', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('dhis2_id', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dhis2.Facility'], null=True, blank=True)),
            ('equitment_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('working', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'dhis2', ['Equitment'])

        # Adding model 'Contact'
        db.create_table(u'dhis2_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(default='ka', max_length=5)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dhis2.Facility'], null=True, blank=True)),
        ))
        db.send_create_signal(u'dhis2', ['Contact'])

        # Adding model 'ContactConnection'
        db.create_table(u'dhis2_contactconnection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='connection_set', to=orm['dhis2.Contact'])),
            ('connection', self.gf('django.db.models.fields.related.OneToOneField')(related_name='dhis2', unique=True, to=orm['rapidsms.Connection'])),
        ))
        db.send_create_signal(u'dhis2', ['ContactConnection'])


    def backwards(self, orm):
        # Deleting model 'OrganisationUnit'
        db.delete_table(u'dhis2_organisationunit')

        # Deleting model 'Facility'
        db.delete_table(u'dhis2_facility')

        # Deleting model 'Equitment'
        db.delete_table(u'dhis2_equitment')

        # Deleting model 'Contact'
        db.delete_table(u'dhis2_contact')

        # Deleting model 'ContactConnection'
        db.delete_table(u'dhis2_contactconnection')


    models = {
        u'dhis2.contact': {
            'Meta': {'object_name': 'Contact'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dhis2.Facility']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'ka'", 'max_length': '5'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'dhis2.contactconnection': {
            'Meta': {'object_name': 'ContactConnection'},
            'connection': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'dhis2'", 'unique': 'True', 'to': u"orm['rapidsms.Connection']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'connection_set'", 'to': u"orm['dhis2.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dhis2.equitment': {
            'Meta': {'object_name': 'Equitment'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dhis2_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'equitment_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dhis2.Facility']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'working': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'dhis2.facility': {
            'Meta': {'object_name': 'Facility'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dhis2_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'dhis2_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'i18n_name': ('jsonfield.fields.JSONField', [], {}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dhis2.OrganisationUnit']", 'null': 'True', 'blank': 'True'})
        },
        u'dhis2.organisationunit': {
            'Meta': {'object_name': 'OrganisationUnit'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dhis2_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'dhis2_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'i18n_name': ('jsonfield.fields.JSONField', [], {}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['dhis2.OrganisationUnit']"})
        },
        u'rapidsms.backend': {
            'Meta': {'object_name': 'Backend'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'rapidsms.connection': {
            'Meta': {'unique_together': "(('backend', 'identity'),)", 'object_name': 'Connection'},
            'backend': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rapidsms.Backend']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rapidsms.Contact']", 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'rapidsms.contact': {
            'Meta': {'object_name': 'Contact'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['dhis2']