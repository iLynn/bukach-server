from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

import bukach.views as controller
import bukach.view_home as HomeView



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^add-user$', controller.addUser),
    url(r'^auth$', controller.auth),
    url(r'^$', controller.index),

    url(r'^get_ads_info$', HomeView.getAdsInfo),
    url(r'^get_ad_detail$', HomeView.getAdDetail),
    url(r'^get_course_category$', HomeView.getCourseCategory),
    url(r'^get_course_info$', HomeView.getCourseByCategory),
    url(r'^get_course_detail$', HomeView.getCourseDetail),
    url(r'^get_teacher_info$', HomeView.getTeacherInfo),

    url(r'^get_all_grace$', HomeView.getAllGrace),
    url(r'^get_grace_detail$', HomeView.getGraceDetail),
    url(r'^add_feedback$', HomeView.addFeedback),
    url(r'^about_us$', HomeView.aboutUs),
    url(r'^get_job_info$', HomeView.jobInfos),
    url(r'^get_hot_summary$', HomeView.get_hot_summary),
    url(r'^get_all_hot_by_type$', HomeView.get_all_hot_by_type),
    url(r'^get_hot_detail$', HomeView.get_hot_detail),
)
