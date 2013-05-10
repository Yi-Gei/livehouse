# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect,render_to_response
from models import Course,Teacher,Student
import json,hashlib

def logout(request):
    error_msg = ''
    if 'user' in request.session:
        del request.session['user']
    return redirect('/')

def login(request):
    error_msg = ''
    if request.method == 'GET':
        error_msg = 'Post request is required'
        return HttpResponse(json.dumps({'error_msg':error_msg}))
    role = request.POST.get('role','')
    email = request.POST.get('email','')
    pw = request.POST.get('pw','')
    #pw = password=hash.md5(pw).digeset()
    user = None
    if role =='student':
        try:
            user = Student.objects.get(email=email,password=pw)
        except Student.DoesNotExist:
            error_msg = 'mismatch'
            return HttpResponse(json.dumps({'error_msg':error_msg}))
        else:
            request.session['role'] = 'student'
            request.session['user'] = user.name
            request.session['useremail'] = user.email
            request.session['user'] = user
    elif role == 'teacher':
        try:
            user = Teacher.objects.get(email=email,password=pw)
        except Teacher.DoesNotExist:
            error_msg = 'mismatch'
            return HttpResponse(json.dumps({'error_msg':error_msg}))
        else:
            request.session['role'] = 'teacher'
            request.session['user'] = user.name
            request.session['user'] = user
    else:
        error_msg =  'role needed'
        return HttpResponse(json.dumps({'error_msg':error_msg}))

    return HttpResponse(json.dumps({'error_msg':error_msg}))

def mainpage(request):
    render_obj = {}
    render_obj['recommend_course'] = Course.objects.filter(status=1)
    render_obj['homepage_course'] = Course.objects.filter(status=2)
    render_obj['top_course'] = Course.objects.order_by('-praise')[:5]
    render_obj['homepage_teacher'] = Teacher.objects.filter(status=2)
    render_obj['top_teacher'] = Teacher.objects.order_by('-praise')[:5]
    if 'user' in request.session:
        render_obj['teacher'] = True if request.session.get('role','')=='teacher' else False
        render_obj['student'] = True if request.session.get('role','')=='student' else False
        render_obj['user'] = request.session['user']
    else:
        render_obj['user'] = ''
    return render_to_response('index.html',{'render_obj':render_obj})

def teacher(request):
    render_obj = {}
    render_obj['all_teacher'] = Teacher.objects.all()
    render_obj['recommend_teacher'] = Teacher.objects.filter(status=1)
    render_obj['homepage_teacher'] = Teacher.objects.filter(status=2)
    render_obj['top_teacher'] = Teacher.objects.all()[:5]
    if 'user' in request.session:
        render_obj['teacher'] = True if request.session.get('role','')=='teacher' else False
        render_obj['student'] = True if request.session.get('role','')=='student' else False
        render_obj['user'] = request.session['user']
    else:
        render_obj['user'] = ''
    return render_to_response('teacher.html',{'render_obj':render_obj})

def course(request):
    render_obj = {}
    render_obj['all_course'] = Course.objects.all()
    render_obj['recommend_course'] = Course.objects.filter(status=1)
    render_obj['homepage_course'] = Course.objects.filter(status=2)
    render_obj['top_course'] = Course.objects.all()[:5]
    if 'user' in request.session:
        render_obj['teacher'] = True if request.session.get('role','')=='teacher' else False
        render_obj['student'] = True if request.session.get('role','')=='student' else False
        render_obj['user'] = request.session['user']
    else:
        render_obj['user'] = ''
    return render_to_response('course.html',{'render_obj':render_obj})

def one_course(request,cid):
    render_obj = {}
    try:
        course = Course.objects.get(id=cid)
        render_obj['course'] = course
        nextdate = course.nextdate.split(',')
        render_obj['openday'] = course.openday
    except Exception as e:
        print str(e)
        render_obj['course'] = None
    render_obj['top_course'] = Course.objects.all()[:5]
    if 'user' in request.session:
        render_obj['teacher'] = True if request.session.get('role','')=='teacher' else False
        render_obj['student'] = True if request.session.get('role','')=='student' else False
        render_obj['user'] = request.session['user']
    else:
        render_obj['user'] = ''
    render_obj['top_course'] = Course.objects.order_by('-praise')[:5]
    render_obj['top_teacher'] = Teacher.objects.order_by('-praise')[:5]
    return render_to_response('onecourse.html',{'render_obj':render_obj})

def one_teacher(request,tid):
    print tid
    render_obj = {}
    try:
        teacher = Teacher.objects.get(id=tid)
        render_obj['t'] = teacher
    except Exception as e:
        print str(e)
        render_obj['teacher'] = None
    render_obj['top_course'] = Course.objects.all()[:5]
    if 'user' in request.session:
        render_obj['teacher'] = True if request.session.get('role','')=='teacher' else False
        render_obj['student'] = True if request.session.get('role','')=='student' else False
        render_obj['user'] = request.session['user']
    else:
        render_obj['user'] = ''
    render_obj['top_course'] = Course.objects.order_by('-praise')[:5]
    render_obj['top_teacher'] = Teacher.objects.order_by('-praise')[:5]
    return render_to_response('oneteacher.html',{'render_obj':render_obj})
def mycourse(request):
    if 'user' not in request.session:
        return render_to_response('login.html')
    render_obj = {}
    if request.session['role'] == 'teacher':
        render_obj['mycourse'] = request.session['user'].course_set.all()
    else:
        render_obj['mycourse'] = request.session['user'].course.all()
    for c in render_obj['mycourse']:
        print c.name,c.urlt
    if 'user' in request.session:
        render_obj['teacher'] = True if request.session.get('role','')=='teacher' else False
        render_obj['student'] = True if request.session.get('role','')=='student' else False
        render_obj['user'] = request.session['user']
    else:
        render_obj['user'] = ''
    return render_to_response('mycourse.html',{'render_obj':render_obj})

def setupclass(request):
    render_obj = {}
    if request.session['role'] != 'teacher':
        return render_to_response('youarenotteacher.html')
    if 'user' in request.session:
        render_obj['teacher'] = True if request.session.get('role','')=='teacher' else False
        render_obj['student'] = True if request.session.get('role','')=='student' else False
        render_obj['user'] = request.session['user']
    else:
        render_obj['user'] = ''
    print render_obj
    return render_to_response('setupclass.html',{'render_obj':render_obj})

def reg(request):
    return render_to_response('reg.html')
