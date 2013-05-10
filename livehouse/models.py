# -*- coding: utf-8 -*-
from django.db import models

class Teacher(models.Model):
    STATUS = (
                (0,"nothing"),
                (1,"recommreandr"),
                (2,"homepage"),
            )
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=512)
    hometown = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(max_length=400, blank=True, null=True)
    picture = models.URLField(blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    status = models.IntegerField(blank=True, null=True,choices=STATUS)
    praise = models.IntegerField(blank=True, null=True) 
    view = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.name

class Student(models.Model):
    course = models.ManyToManyField('Course',blank=True,null=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=512)
    description = models.TextField(max_length=400, blank=True, null=True)
    picture = models.URLField(blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)

    def __unicode__(self):
        return u'%s' % self.name

class Course(models.Model):
    DATE_PLAN = (
        (0,"by week"),
        (1,"by month"),
    )
    STATUS = (
                (0,"nothing"),
                (1,"recommreandr"),
                (2,"homepage"),
            )
    teacher = models.ForeignKey('Teacher')
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(blank=True,null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    starttime = models.TimeField(blank=True, null=True)
    endtime = models.TimeField(blank=True, null=True)
    dateplan = models.IntegerField(choices=DATE_PLAN,default=1,blank=True, null=True)
    nextdate = models.CharField(max_length=60,blank=True, null=True)
    level = models.CharField(max_length=256,blank=True, null=True)
    typ = models.CharField(max_length=256,blank=True, null=True)
    status = models.IntegerField(blank=True, null=True,choices=STATUS)
    praise = models.IntegerField(blank=True, null=True)
    max_count = models.IntegerField(blank=True, null=True)
    view = models.IntegerField(blank=True, null=True)
    urlt = models.URLField(blank=True,null=True)
    urls = models.URLField(blank=True,null=True)

    @property
    def openday(self):
        if self.dateplan == 0: # week
            return u'每周: ' + ','.join([u'周'+e for e in self.nextdate])
        elif self.dateplan == 1: # month
            return u'每月: ' + ','.join([e+u'号' for e in self.nextdate])

    def __unicode__(self):
        return u'%s' % self.name
