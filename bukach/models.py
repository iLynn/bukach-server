from django.db import models

import datetime
# Create your models here.

class BukachUser(models.Model):
    username = models.CharField(primary_key=True, max_length=25)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    create_time = models.DateTimeField()

    def __str__(self):
        if self.className :
            return "%s" % (self.className)

    def __unicode__(self):
        return self.username

#

class TitleAdsInfo(models.Model):
    ad_text = models.CharField(max_length=200, default='', blank=True)
    ad_img = models.CharField(max_length=50, default='', blank=True)
    ad_order = models.IntegerField(default=1, blank=True)
    ad_content_img = models.TextField(max_length=1000, default='', blank=True)

    def __unicode__(self):
        return self.ad_text

class CourseCategory(models.Model):
    category_name = models.CharField(max_length=100, default='', blank=True)
    category_img = models.CharField(max_length=50, default='', blank=True)
    category_order = models.IntegerField(default=1, blank=True)

    def __unicode__(self):
        return self.category_name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50, default='', blank=True)
    teacher_img = models.CharField(max_length=50, default='', blank=True)
    teacher_style = models.CharField(max_length=500, default='', blank=True)
    teacher_experience = models.CharField(max_length=100, default='', blank=True)
    teacher_detail = models.TextField(max_length=2000, default='', blank=True)
    teacher_education_bg = models.TextField(max_length=100, default='', blank=True)
    teacher_award = models.TextField(max_length=200, default='', blank=True)
    teacher_level = models.IntegerField(default=5, blank=True)
    teacher_students = models.CharField(max_length=500, default='', blank=True)

    def __unicode__(self):
        return  self.teacher_name


class CourseInfo(models.Model):
    course_name = models.CharField(max_length=100, default='', blank=True)
    course_category = models.ForeignKey(CourseCategory, blank=True)
    course_intro = models.TextField(max_length=500, default='', blank=True)
    course_detail = models.TextField(max_length=2000, default='', blank=True)
    course_img = models.CharField(max_length=50, default='', blank=True)
    course_teacher = models.ManyToManyField(Teacher, blank=True)

    def __unicode__(self):
        return self.course_name


class ImageInfo(models.Model):
    image_location = models.CharField(max_length=50, default='', blank=True)
    image_height = models.IntegerField(default=300, blank=True)
    image_width = models.IntegerField(default=200, blank=True)
    image_desc = models.CharField(max_length=200, default='', blank=True)

    def __unicode__(self):
        return self.image_location


class GraceInfo(models.Model):
    grace_title = models.CharField(max_length=100, default='', blank=True)
    grace_title_img = models.CharField(max_length=50, default='', blank=True)
    grace_title_img_height = models.IntegerField(default=300, blank=True)
    grace_title_img_width = models.IntegerField(default=200, blank=True)
    grace_create_time = models.DateTimeField(auto_now=True, default=datetime.date.today())
    grace_content_img = models.ManyToManyField(ImageInfo, blank=True)
    grace_img_str = models.TextField(max_length=1000, default='', blank=True)

    def __unicode__(self):
        return self.grace_title


class HotInfoType(models.Model):
    hot_info_desc = models.CharField(max_length=50, default='')

    def __unicode__(self):
        return self.hot_info_desc


class HotInfo(models.Model):
    hot_info_title = models.CharField(max_length=100, default='', blank=True)
    hot_info_title_img = models.CharField(max_length=50, default='', blank=True)
    hot_title_img_height = models.IntegerField(default=300, blank=True)
    hot_title_img_width = models.IntegerField(default=200, blank=True)
    hot_info_type = models.ForeignKey(HotInfoType, blank=True)
    hot_date = models.DateTimeField(auto_now_add=True, blank=True)
    hot_info_content_img = models.ManyToManyField(ImageInfo, blank=True)
    hot_info_img_str = models.TextField(max_length=1000, default='', blank=True)

    def __unicode__(self):
        return self.hot_info_title


class UserFeedback(models.Model):
    feedback_content = models.TextField(max_length=1000, default='')
    feedback_email = models.EmailField(default='example@126.com', blank=True)
    feedback_phone = models.CharField(max_length=15, default='', blank=True)
    feedback_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.feedback_content


class AboutUsInfo(models.Model):
    about_us_detail = models.TextField(max_length=1000, default='')

    def __unicode__(self):
        return self.about_us_detail


class JobInfo(models.Model):
    job_type = models.CharField(max_length=50, default='')
    job_name = models.CharField(max_length=50, default='')
    job_detail = models.TextField(max_length=500, default='', blank=True)
    job_quota = models.CharField(max_length=200, default='', blank=True)
    resume_to = models.CharField(max_length=100, default='', blank=True)
    job_deadline = models.CharField(max_length=50, default='long term', blank=True)

    def __unicode__(self):
        return self.job_name



