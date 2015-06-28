__author__ = 'likun'

from bukach.models import BukachUser
import time
import hashlib
import random
import logging




def new_user(username, password, email):
    if (username == '' or password == ''):
        return -1

    try:
        curr_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        user = BukachUser(username = username, password = password, email = email, create_time = curr_time)
        user.save()

        return 1
    except Exception, e:
        logging(e)
        return -1

def auth(username, password):
    try:
        logging.info(username, password)
        result = BukachUser.objects.filter(username = username, password = password)
        if(len(result) == 1):
            logging.info("user " + username + "logon.")
            return md5(random.uniform(1, 10000))
        else:
            return -1
    except Exception, e:
        logging.info(e)
        return -1


def md5(input):
    m = hashlib.md5()
    m.update(str(input))
    return m.hexdigest()

