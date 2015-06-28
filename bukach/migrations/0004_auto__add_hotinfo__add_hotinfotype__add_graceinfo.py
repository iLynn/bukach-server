# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HotInfo'
        db.create_table('bukach_hotinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hot_info_title', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('hot_info_title_img', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('hot_info_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bukach.HotInfoType'])),
            ('hot_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('hot_info_content_img', self.gf('django.db.models.fields.CharField')(default='', max_length=500)),
        ))
        db.send_create_signal('bukach', ['HotInfo'])

        # Adding model 'HotInfoType'
        db.create_table('bukach_hotinfotype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hot_info_desc', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
        ))
        db.send_create_signal('bukach', ['HotInfoType'])

        # Adding model 'GraceInfo'
        db.create_table('bukach_graceinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('grace_title', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('grace_title_img', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('grace_content_img', self.gf('django.db.models.fields.CharField')(default='', max_length=500)),
        ))
        db.send_create_signal('bukach', ['GraceInfo'])


    def backwards(self, orm):
        # Deleting model 'HotInfo'
        db.delete_table('bukach_hotinfo')

        # Deleting model 'HotInfoType'
        db.delete_table('bukach_hotinfotype')

        # Deleting model 'GraceInfo'
        db.delete_table('bukach_graceinfo')


    models = {
        'bukach.bukachuser': {
            'Meta': {'object_name': 'BukachUser'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'})
        },
        'bukach.coursecategory': {
            'Meta': {'object_name': 'CourseCategory'},
            'category_img': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'category_order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bukach.courseinfo': {
            'Meta': {'object_name': 'CourseInfo'},
            'course_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bukach.CourseCategory']"}),
            'course_detail': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'course_img': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'course_intro': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'course_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'course_teacher': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bukach.Teacher']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bukach.graceinfo': {
            'Meta': {'object_name': 'GraceInfo'},
            'grace_content_img': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'grace_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'grace_title_img': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bukach.hotinfo': {
            'Meta': {'object_name': 'HotInfo'},
            'hot_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hot_info_content_img': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'hot_info_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'hot_info_title_img': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'hot_info_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bukach.HotInfoType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bukach.hotinfotype': {
            'Meta': {'object_name': 'HotInfoType'},
            'hot_info_desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bukach.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teacher_award': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '200'}),
            'teacher_detail': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'teacher_education_bg': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '100'}),
            'teacher_experience': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'teacher_img': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'teacher_level': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'teacher_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'teacher_students': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'teacher_style': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'bukach.titleadsinfo': {
            'Meta': {'object_name': 'TitleAdsInfo'},
            'ad_img': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ad_order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'ad_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['bukach']