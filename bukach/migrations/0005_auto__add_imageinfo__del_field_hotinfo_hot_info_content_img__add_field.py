# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImageInfo'
        db.create_table('bukach_imageinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_location', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('image_height', self.gf('django.db.models.fields.IntegerField')(default=300)),
            ('image_width', self.gf('django.db.models.fields.IntegerField')(default=200)),
            ('image_desc', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal('bukach', ['ImageInfo'])

        # Deleting field 'HotInfo.hot_info_content_img'
        db.delete_column('bukach_hotinfo', 'hot_info_content_img')

        # Adding field 'HotInfo.hot_title_img_height'
        db.add_column('bukach_hotinfo', 'hot_title_img_height',
                      self.gf('django.db.models.fields.IntegerField')(default=300),
                      keep_default=False)

        # Adding field 'HotInfo.hot_title_img_width'
        db.add_column('bukach_hotinfo', 'hot_title_img_width',
                      self.gf('django.db.models.fields.IntegerField')(default=200),
                      keep_default=False)

        # Adding M2M table for field hot_info_content_img on 'HotInfo'
        m2m_table_name = db.shorten_name('bukach_hotinfo_hot_info_content_img')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hotinfo', models.ForeignKey(orm['bukach.hotinfo'], null=False)),
            ('imageinfo', models.ForeignKey(orm['bukach.imageinfo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['hotinfo_id', 'imageinfo_id'])

        # Deleting field 'GraceInfo.grace_content_img'
        db.delete_column('bukach_graceinfo', 'grace_content_img')

        # Adding field 'GraceInfo.grace_title_img_height'
        db.add_column('bukach_graceinfo', 'grace_title_img_height',
                      self.gf('django.db.models.fields.IntegerField')(default=300),
                      keep_default=False)

        # Adding field 'GraceInfo.grace_title_img_width'
        db.add_column('bukach_graceinfo', 'grace_title_img_width',
                      self.gf('django.db.models.fields.IntegerField')(default=200),
                      keep_default=False)

        # Adding M2M table for field grace_content_img on 'GraceInfo'
        m2m_table_name = db.shorten_name('bukach_graceinfo_grace_content_img')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('graceinfo', models.ForeignKey(orm['bukach.graceinfo'], null=False)),
            ('imageinfo', models.ForeignKey(orm['bukach.imageinfo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['graceinfo_id', 'imageinfo_id'])


    def backwards(self, orm):
        # Deleting model 'ImageInfo'
        db.delete_table('bukach_imageinfo')

        # Adding field 'HotInfo.hot_info_content_img'
        db.add_column('bukach_hotinfo', 'hot_info_content_img',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500),
                      keep_default=False)

        # Deleting field 'HotInfo.hot_title_img_height'
        db.delete_column('bukach_hotinfo', 'hot_title_img_height')

        # Deleting field 'HotInfo.hot_title_img_width'
        db.delete_column('bukach_hotinfo', 'hot_title_img_width')

        # Removing M2M table for field hot_info_content_img on 'HotInfo'
        db.delete_table(db.shorten_name('bukach_hotinfo_hot_info_content_img'))

        # Adding field 'GraceInfo.grace_content_img'
        db.add_column('bukach_graceinfo', 'grace_content_img',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500),
                      keep_default=False)

        # Deleting field 'GraceInfo.grace_title_img_height'
        db.delete_column('bukach_graceinfo', 'grace_title_img_height')

        # Deleting field 'GraceInfo.grace_title_img_width'
        db.delete_column('bukach_graceinfo', 'grace_title_img_width')

        # Removing M2M table for field grace_content_img on 'GraceInfo'
        db.delete_table(db.shorten_name('bukach_graceinfo_grace_content_img'))


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
            'grace_content_img': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bukach.ImageInfo']", 'symmetrical': 'False'}),
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