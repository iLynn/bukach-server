# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BukachUser'
        db.create_table('bukach_bukachuser', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=25, primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('bukach', ['BukachUser'])

        # Adding model 'TitleAdsInfo'
        db.create_table('bukach_titleadsinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ad_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ad_img', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ad_order', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('bukach', ['TitleAdsInfo'])

        # Adding model 'CourseCategory'
        db.create_table('bukach_coursecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('category_img', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bukach', ['CourseCategory'])

        # Adding model 'Teacher'
        db.create_table('bukach_teacher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teacher_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('teacher_img', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('teacher_style', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('teacher_experience', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('teacher_detail', self.gf('django.db.models.fields.TextField')(max_length=2000)),
        ))
        db.send_create_signal('bukach', ['Teacher'])

        # Adding model 'CourseInfo'
        db.create_table('bukach_courseinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('course_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bukach.CourseCategory'])),
            ('course_intro', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('course_detail', self.gf('django.db.models.fields.TextField')(max_length=2000)),
            ('course_img', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bukach', ['CourseInfo'])

        # Adding M2M table for field course_teacher on 'CourseInfo'
        m2m_table_name = db.shorten_name('bukach_courseinfo_course_teacher')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('courseinfo', models.ForeignKey(orm['bukach.courseinfo'], null=False)),
            ('teacher', models.ForeignKey(orm['bukach.teacher'], null=False))
        ))
        db.create_unique(m2m_table_name, ['courseinfo_id', 'teacher_id'])


    def backwards(self, orm):
        # Deleting model 'BukachUser'
        db.delete_table('bukach_bukachuser')

        # Deleting model 'TitleAdsInfo'
        db.delete_table('bukach_titleadsinfo')

        # Deleting model 'CourseCategory'
        db.delete_table('bukach_coursecategory')

        # Deleting model 'Teacher'
        db.delete_table('bukach_teacher')

        # Deleting model 'CourseInfo'
        db.delete_table('bukach_courseinfo')

        # Removing M2M table for field course_teacher on 'CourseInfo'
        db.delete_table(db.shorten_name('bukach_courseinfo_course_teacher'))


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
            'teacher_detail': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'teacher_experience': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'teacher_img': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'teacher_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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