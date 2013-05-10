#!/usr/bin/python

import sys
sys.path.insert(0,'../')
sys.path.insert(0,'.')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "livehouse.settings")

import hashlib,urllib,urllib2
'''
salt is from /var/lib/tomcat6/webapps/demo/bbb_api_conf.jsp
'''
salt = "0129f13790115541d6b2f16a1f684c05"
api_url_prefix = 'http://192.168.0.102/bigbluebutton/api/'
def create_meeting(name,meetingID,welcome='',pd=''):
    if pd:
        para= urllib.urlencode({'name':name,'meetingID':meetingID,'welcome':welcome,'record':'true','attendeePW':pd})
    else:
        para= urllib.urlencode({'name':name,'meetingID':meetingID,'welcome':welcome,'record':'true'})
    s = 'create' + para + salt
    print s
    checksum = ''.join([hex(ord(e))[2:] for e in hashlib.sha1(s).digest()])
    print checksum
    url = api_url_prefix+'create?'+para+'&checksum='+checksum
    print url
    print urllib2.urlopen(url).read()
        
create_meeting('sandy','liujia','welcome','fdasf123')

def join_meeting(fullName,meetingID,password):
    para = urllib.urlencode({'fullName':fullName,'meetingID':meetingID,'password':password})
    print para
    s = 'join'+para+salt
    checksum = ''.join([hex(ord(e))[2:] for e in hashlib.sha1(s).digest()])
    url = api_url_prefix+'join?'+para+'&checksum='+checksum
    print url

join_meeting('liujia','liujia','fdasf123')

def get_record(meetingID):
    para = urllib.urlencode({'meetingID':meetingID})
    s = 'getRecordings'+para+salt
    checksum = ''.join([hex(ord(e))[2:] for e in hashlib.sha1(s).digest()])
    url = api_url_prefix+'getRecordings?'+para+'&checksum='+checksum
    print url

#get_record('w')

from livehouse.models import *

import datetime

offset = datetime.timedelta(hours=1)

t = datetime.datetime.now()
for course in Course.objects.all():
    nextdates = [int(e) for e in course.nextdate.split(',')]
    starttime = course.starttime
    # nextdates.sort()
    if course.dateplan == 1: # by week
        n = t.weekday()+1
    elif course.dateplan == 2: # by month
        n = t.day

    for nextdate in nextdates:
        d = t + datetime.timedelta(nextdate-n)
        dt = datetime.datetime(d.year,d.month,d.day,starttime.hour,starttime.minute,starttime.second)
        if t < dt and (dt-t)<offset:
            print 1

