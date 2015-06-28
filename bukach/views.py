# Create your views here.

__author__ = 'likun'

from django.http import HttpResponse
import json
from django.shortcuts import render_to_response
from bukach.service import main_service as Service

CODE_ERR = -1
CODE_OK = 1


def auth(httpRequest):
    response_data = {}
    response_data['code'] = CODE_ERR
    if httpRequest.method == 'POST':
        username = httpRequest.POST.get('username', '')
        password = httpRequest.POST.get('password', '')
        result = Service.auth(username, password)
        if(result != -1):
            response_data['code'] = CODE_OK
            response_data['login_id'] = result
    return HttpResponse(json.dumps(response_data), content_type="application/json")



def index(httpRequest):
	return render_to_response("index.html")


def addUser(httpRequest):
    response_data = {}
    response_data['code'] = 'error'
    if httpRequest.method == 'POST':
        username = httpRequest.POST.get('username', '')
        password = httpRequest.POST.get('password', '')
        email = httpRequest.POST.get('email', '')
        result = Service.new_user(username, password, email)
        if(result == 1):
            response_data['code'] = CODE_OK
    return HttpResponse(json.dumps(response_data), content_type="application/json");
