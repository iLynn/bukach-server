__author__ = 'likun'

from django.http import HttpResponse

import json
import logging
from django.shortcuts import render_to_response
from bukach.service import home_service as Service

CODE_ERR = -1
CODE_OK = 1

def getAdsInfo(httpRequest):
    logging.info("start to call getAdsInfo")
    response_data = {}
    result = Service.getAdsInfo()
    if result == CODE_ERR:
        response_data['code'] = CODE_ERR
    else:
        response_data['code'] = CODE_OK
        response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def getAdDetail(httpRequest):
    logging.info("start to call getAdDetail")
    response_data = {}

    if httpRequest.method == 'POST':
        ad_id = httpRequest.POST.get('ad_id', '')

        result = Service.get_ad_detail(ad_id)
        if result == CODE_ERR:
            response_data['code'] = CODE_ERR
        else:
            response_data['code'] = CODE_OK
            response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def getCourseCategory(httpRequest):
    logging.info("start to call getCourseCategory")
    response_data = {}
    result = Service.getCourseCategory()
    if result == CODE_ERR:
        response_data['code'] = CODE_ERR
    else:
        response_data['code'] = CODE_OK
        response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def getCourseByCategory(httpRequest):
    logging.info("start to call getCourseByCategory")
    response_data = {}

    if httpRequest.method == 'POST':
        categoryId = httpRequest.POST.get('category_id', '')

        result = Service.get_course_by_category(categoryId)
        if result == CODE_ERR:
            response_data['code'] = CODE_ERR
        else:
            response_data['code'] = CODE_OK
            response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def getCourseDetail(httpRequest):
    logging.info("start to call getCourseDetail")
    response_data = {}

    if httpRequest.method == 'POST':
        course_id = httpRequest.POST.get('course_id', '')

        result = Service.get_course_detail(course_id)
        if result == CODE_ERR:
            response_data['code'] = CODE_ERR
        else:
            response_data['code'] = CODE_OK
            response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def getTeacherInfo(httpRequest):
    logging.info("start to call getTeacherInfo")
    response_data = {}

    if httpRequest.method == 'POST':
        teacher_id = httpRequest.POST.get('teacher_id', '')

        result = Service.get_teacher_info(teacher_id)
        if result == CODE_ERR:
            response_data['code'] = CODE_ERR
        else:
            response_data['code'] = CODE_OK
            response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def getAllGrace(httpRequest):
    logging.info("start to call getAllGrace")
    response_data = {}

    if httpRequest.method == 'POST':
        start = httpRequest.POST.get('start', 0)
        end = httpRequest.POST.get('end', 19)
        result = Service.get_all_grace(start, end)
        if result == CODE_ERR:
            response_data['code'] = CODE_ERR
        else:
            response_data['code'] = CODE_OK
            response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def getGraceDetail(httpRequest):
    logging.info("start to call getGraceDetail")
    response_data = {}

    if httpRequest.method == 'POST':
        grace_id = httpRequest.POST.get('grace_id', '')

        result = Service.get_grace_detail(grace_id=grace_id)
        if result == CODE_ERR:
            response_data['code'] = CODE_ERR
        else:
            response_data['code'] = CODE_OK
            response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def getHostInfoSummary(httpRequest):
    logging.info("start to call getHostInfoSummary")
    response_data = {}

    result = Service.get_hot_info_summary()
    if result == CODE_ERR:
        response_data['code'] = CODE_ERR
    else:
        response_data['code'] = CODE_OK
        response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def addFeedback(httpRequest):
    logging.info("start to call addFeedback")
    response_data = {}

    if httpRequest.method == 'POST':
        content = httpRequest.POST.get('content', '')
        email = httpRequest.POST.get('email', 'a@126.com')
        phone = httpRequest.POST.get('phone', '131')

        result = Service.add_feedback(content=content, email = email, phone = phone)
        if result == CODE_ERR:
            response_data['code'] = CODE_ERR
        else:
            response_data['code'] = CODE_OK
            response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def aboutUs(httpRequest):
    logging.info("start to call aboutUs")
    response_data = {}

    result = Service.aboutUs()
    if result == CODE_ERR:
        response_data['code'] = CODE_ERR
    else:
        response_data['code'] = CODE_OK
        response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def jobInfos(httpRequest):
    logging.info("start to call jobInfos")
    response_data = {}

    result = Service.allJobInfo()
    if result == CODE_ERR:
        response_data['code'] = CODE_ERR
    else:
        response_data['code'] = CODE_OK
        response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_hot_summary(httpRequest):
    logging.info("start to call get_hot_summary")
    response_data = {}

    result = Service.get_hot_info_summary()
    if result == CODE_ERR:
        response_data['code'] = CODE_ERR
    else:
        response_data['code'] = CODE_OK
        response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_all_hot_by_type(httpRequest):
    logging.info("start to call get_all_hot_by_type")
    response_data = {}

    if httpRequest.method == 'POST':
        hot_type_id = httpRequest.POST.get('hot_type_id', '')

        result = Service.get_all_hot_by_type(hot_type_id)
        if result == CODE_ERR:
            response_data['code'] = CODE_ERR
        else:
            response_data['code'] = CODE_OK
            response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_hot_detail(httpRequest):
    logging.info("start to call get_hot_detail")
    response_data = {}

    if httpRequest.method == 'POST':
        hot_id = httpRequest.POST.get('hot_id', '')

        result = Service.get_hot_detail(hot_id)
        if result == CODE_ERR:
            response_data['code'] = CODE_ERR
        else:
            response_data['code'] = CODE_OK
            response_data['data'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json")