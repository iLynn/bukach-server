# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'AboutUsInfo.about_us_detail'
        db.alter_column('bukach_aboutusinfo', 'about_us_detail', self.gf('django.db.models.fields.TextField')(max_length=1000))

        # Changing field 'JobInfo.job_detail'
        db.alter_column('bukach_jobinfo', 'job_detail', self.gf('django.db.models.fields.TextField')(max_length=500))

    def backwards(self, orm):

        # Changing field 'AboutUsInfo.about_us_detail'
        db.alter_column('bukach_aboutusinfo', 'about_us_detail', self.gf('django.db.models.fields.CharField')(max_length=1000))

        # Changing field 'JobInfo.job_detail'
        db.alter_column('bukach_jobinfo', 'job_detail', self.gf('django.db.models.fields.CharField')(max_length=500))

    models = {
        'bukach.aboutusinfo': {
            'Meta': {'object_name': 'AboutUsInfo'},
            'about_us_detail': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bukach.bukachuser': {
            'Meta': {'object_name': 'BukachUser'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'})
        },
        'bukach.coursecategory': {
            'Meta': {'object_name': 'CourseCategory'},
            'category_img': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'category_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'category_order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bukach.courseinfo': {
            'Meta': {'object_name': 'CourseInfo'},
            'course_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bukach.CourseCategory']"}),
            'course_detail': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '2000'}),
            'course_img': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'course_intro': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '500'}),
            'course_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'course_teacher': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bukach.Teacher']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bukach.graceinfo': {
            'Meta': {'object_name': 'GraceInfo'},
            'grace_content_img': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bukach.ImageInfo']", 'symmetrical': 'False'}),
            'grace_create_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 6, 25, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'grace_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'grace_title_img': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'grace_title_img_height': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            'grace_title_img_width': ('django.db.models.fields.IntegerField', [], {'default': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bukach.hotinfo': {
            'Meta': {'object_name': 'HotInfo'},
            'hot_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hot_info_content_img': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bukach.ImageInfo']", 'symmetrical': 'False'}),
            'hot_info_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'hot_info_title_img': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'hot_info_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bukach.HotInfoType']"}),
            'hot_title_img_height': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            'hot_title_img_width': ('django.db.models.fields.IntegerField', [], {'default': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bukach.hotinfotype': {
            'Meta': {'object_name': 'HotInfoType'},
            'hot_info_desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bukach.imageinfo': {
            'Meta': {'object_name': 'ImageInfo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'image_height': ('django.db.models.fields.IntegerField', [], {'default': '300'}),
            'image_location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'image_width': ('django.db.models.fields.IntegerField', [], {'default': '200'})
        },
        'bukach.jobinfo': {
            'Meta': {'object_name': 'JobInfo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_deadline': ('django.db.models.fields.CharField', [], {'default': "'long term'", 'max_length': '50'}),
            'job_detail': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '500'}),
            'job_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'job_quota': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'job_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'resume_to': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        'bukach.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teacher_award': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '200'}),
            'teacher_detail': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '2000'}),
            'teacher_education_bg': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '100'}),
            'teacher_experience': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'teacher_img': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'teacher_level': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'teacher_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'teacher_students': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'teacher_style': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'})
        },
        'bukach.titleadsinfo': {
            'Meta': {'object_name': 'TitleAdsInfo'},
            'ad_img': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'ad_order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'ad_text': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'bukach.userfeedback': {
            'Meta': {'object_name': 'UserFeedback'},
            'feedback_content': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'feedback_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'feedback_email': ('django.db.models.fields.EmailField', [], {'default': "'example@126.com'", 'max_length': '75'}),
            'feedback_phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['bukach']