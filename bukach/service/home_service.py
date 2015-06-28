__author__ = 'likun'

from bukach.models import TitleAdsInfo
from bukach.models import CourseCategory
from bukach.models import CourseInfo
from bukach.models import Teacher
from bukach.models import GraceInfo
from bukach.models import HotInfoType
from bukach.models import HotInfo
from bukach.models import UserFeedback
from bukach.models import AboutUsInfo
from bukach.models import JobInfo
import logging

ERROR_CODE = -1

def getAdsInfo():
    try:
        adsInfo = TitleAdsInfo.objects.all()
        resultInfo = []
        for ads in adsInfo:
            ad = {
                'ads_id': ads.id,
                'ads_title': ads.ad_text,
                'ads_photo': ads.ad_img
            }
            resultInfo.append(ad)

        return resultInfo
    except Exception, e:
        logging(e)
        return ERROR_CODE


def get_ad_detail(ad_id):
    try:
        all_ads = TitleAdsInfo.objects.filter(id = ad_id)
        result_info = []
        for ad_info in all_ads:
            img_arr = [];
            if ad_info.ad_content_img is not None:
                img_arr = ad_info.ad_content_img.split("##")
            ad_item = {
                'ad_id': ad_info.id,
                'ad_text': ad_info.ad_text,
                'hot_photo_array': img_arr,
            }
            result_info.append(ad_item)

        return result_info
    except Exception, e:
        logging(e)
        return ERROR_CODE

def getCourseCategory():
    try:
        categoryInfoList = CourseCategory.objects.all()
        resultInfo = []
        for info in categoryInfoList:
            resultItem = {
                'category_id': info.id,
                'category_name': info.category_name,
                'category_photo': info.category_img
            }
            resultInfo.append(resultItem)

        return resultInfo
    except Exception, e:
        logging(e)
        return ERROR_CODE




def get_course_by_category(category_id):
    try:
        course_info_list = CourseInfo.objects.filter(course_category__id = category_id)
        result_info = []
        for info in course_info_list:
            result_item = {
                'course_id': info.id,
                'course_name': info.course_name,
                'course_intro': info.course_intro,
                'course_photo': info.course_img
            }
            result_info.append(result_item)

        return result_info
    except Exception, e:
        logging(e)
        return ERROR_CODE


def get_course_detail(category_id):
    try:
        course_info_list = CourseInfo.objects.filter(id = category_id)
        result_info = []
        for info in course_info_list:
            teacher_set = info.course_teacher.all()
            teacher_arr = []
            for teacher in teacher_set:
                teacher_info = {
                    'teacher_id': teacher.id,
                    'teacher_name': teacher.teacher_name,
                    'teacher_photo': teacher.teacher_img,
                    'teacher_level': teacher.teacher_level,
                }
                teacher_arr.append(teacher_info)

            result_item = {
                'course_id': info.id,
                'course_name': info.course_name,
                'course_intro': info.course_intro,
                'course_photo': info.course_img,
                'course_detail': info.course_detail,
                'teacher_arr': teacher_arr,
            }
            result_info.append(result_item)

        return result_info
    except Exception, e:
        logging(e)
        return ERROR_CODE


def get_teacher_info(teacher_id):
    try:
        teacher_info_set = Teacher.objects.filter(id = teacher_id)
        teacher_arr = []
        for teacher in teacher_info_set:
            teacher_info = {
                'teacher_id' : teacher.id,
                'teacher_name' : teacher.teacher_name,
                'teacher_photo': teacher.teacher_img,
                'teacher_style': teacher.teacher_style,
                'teacher_experience': teacher.teacher_experience,
                'teacher_detail': teacher.teacher_detail,
                'teacher_graduate_school': teacher.teacher_education_bg,
                'teacher_award': teacher.teacher_award,
                'teacher_students': teacher.teacher_students,
                'teacher_level': teacher.teacher_level,
            }
            teacher_arr.append(teacher_info)

        return teacher_arr
    except Exception, e:
        logging(e)
        return ERROR_CODE


def get_all_grace(start, end):
    try:
        all_grace_info = GraceInfo.objects.order_by('-grace_create_time')[start:end]
        result_info = []
        for info in all_grace_info:
            ctime = info.grace_create_time
            dateStr = str(ctime.year) + "-" + str(ctime.month) + "-" + str(ctime.day) + " " \
                      + str(ctime.hour) + ":" + str(ctime.minute) + ":" + str(ctime.second)
            resultItem = {
                'grace_id': info.id,
                'grace_title': info.grace_title,
                'grace_photo': info.grace_title_img,
                'grace_date': dateStr,
                'img_height': info.grace_title_img_height,
                'img_width': info.grace_title_img_width,
            }
            result_info.append(resultItem)

        return result_info
    except Exception, e:
        logging(e)
        return ERROR_CODE


def get_grace_detail(grace_id):
    try:
        all_grace_info = GraceInfo.objects.filter(id = grace_id)
        result_info = []
        for info in all_grace_info:
            img_arr = [];
            if info.grace_img_str is not None:
                img_arr = info.grace_img_str.split("##")
            # img_set = info.grace_content_img.all()
            # for img in img_set:
            #     img_detail = {
            #         'img_location': img.image_location,
            #         'img_height': img.image_height,
            #         'img_width': img.image_width,
            #     }
            #     img_arr.append(img_detail)

            resultItem = {
                'grace_id': info.id,
                'grace_title': info.grace_title,
                'grace_photo': info.grace_title_img,
                'img_height': info.grace_title_img_height,
                'img_width': info.grace_title_img_width,
                'grace_photo_array': img_arr,
            }
            result_info.append(resultItem)

        return result_info
    except Exception, e:
        logging(e)
        return ERROR_CODE


def get_hot_info_summary():
    try:
        result_info = []
        all_hot_type = HotInfoType.objects.all()
        for type in all_hot_type:
            all_hot_info_per_type = HotInfo.objects.filter(hot_info_type__id = type.id)[0:5]
            hot_content = []
            for hot_info in all_hot_info_per_type:
                ctime = hot_info.hot_date
                dateStr = str(ctime.year) + "-" + str(ctime.month) + "-" + str(ctime.day) + " " \
                      + str(ctime.hour) + ":" + str(ctime.minute) + ":" + str(ctime.second)
                hot_item = {
                    "hot_id": hot_info.id,
                    "hot_date": dateStr,
                    "hot_title": hot_info.hot_info_title,
                    "hot_photo": hot_info.hot_info_title_img,
                }
                hot_content.append(hot_item)
            result_item = {
                "hot_type_id": type.id,
                "hot_type_name": type.hot_info_desc,
                "type_content": hot_content,
            }
            result_info.append(result_item)

        return result_info
    except Exception, e:
        logging(e)
        return ERROR_CODE


def add_feedback(content, email, phone):
    try:
        pub = UserFeedback(feedback_content = content, feedback_email = email, feedback_phone = phone)
        pub.save()
        return "1"
    except Exception, e:
        logging(e)
        return ERROR_CODE

def get_all_hot_by_type(hot_type_id):
    try:
        all_hot = HotInfo.objects.filter(hot_info_type__id = hot_type_id)
        result_info = []
        for hot_info in all_hot:
            ctime = hot_info.hot_date
            dateStr = str(ctime.year) + "-" + str(ctime.month) + "-" + str(ctime.day) + " " \
                  + str(ctime.hour) + ":" + str(ctime.minute) + ":" + str(ctime.second)
            hot_item = {
                    "hot_id": hot_info.id,
                    "hot_date": dateStr,
                    "hot_title": hot_info.hot_info_title,
                    "hot_photo": hot_info.hot_info_title_img,
                }
            result_info.append(hot_item)

        return result_info
    except Exception, e:
        logging(e)
        return ERROR_CODE

def get_hot_detail(hot_info_id):
    try:
        all_hot = HotInfo.objects.filter(id = hot_info_id)
        result_info = []
        for hot_info in all_hot:
            img_arr = [];
            if hot_info.hot_info_img_str is not None:
                img_arr = hot_info.hot_info_img_str.split("##")
            hot_item = {
                'hot_id': hot_info.id,
                'hot_name': hot_info.hot_info_title,
                'hot_photo_array': img_arr,
            }
            result_info.append(hot_item)

        return result_info
    except Exception, e:
        logging(e)
        return ERROR_CODE

def aboutUs():
    try:
        aboutUsInfo = AboutUsInfo.objects.all()
        result_info = []
        for about in aboutUsInfo:
            ad = {
                'about_us_detail': about.about_us_detail,
            }
            result_info.append(ad)

        return result_info
    except Exception, e:
        logging(e)
        return ERROR_CODE

def allJobInfo():
    try:
        job_info_list = JobInfo.objects.all()
        result_info = []
        for job_info in job_info_list:
            result = {
                'job_type': job_info.job_type,
                'job_name': job_info.job_name,
                'job_detail': job_info.job_detail,
                'job_quota': job_info.job_quota,
                'job_deadline': job_info.job_deadline,
                'job_resume': job_info.resume_to,
            }
            result_info.append(result)

        return result_info
    except Exception, e:
        logging(e)
        return ERROR_CODE