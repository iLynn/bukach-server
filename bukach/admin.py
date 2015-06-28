__author__ = 'likun'


from django.contrib import admin

from bukach.models import *

admin.site.register(BukachUser)
admin.site.register(TitleAdsInfo)
admin.site.register(CourseCategory)
admin.site.register(Teacher)
admin.site.register(CourseInfo)
admin.site.register(GraceInfo)
admin.site.register(HotInfoType)
admin.site.register(HotInfo)
admin.site.register(ImageInfo)
admin.site.register(AboutUsInfo)
admin.site.register(JobInfo)
admin.site.register(UserFeedback)

