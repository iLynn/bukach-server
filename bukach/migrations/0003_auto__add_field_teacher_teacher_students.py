# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Teacher.teacher_students'
        db.add_column('bukach_teacher', 'teacher_students',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Teacher.teacher_students'
        db.delete_column('bukach_teacher', 'teacher_students')


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