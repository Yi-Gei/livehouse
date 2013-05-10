from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=512)
    hometown = models.CharField(max_length=256, blank=True, null=True)
    desciption = models.TextField(max_length=400, blank=True, null=True)
    picture = models.URLField(blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return name

class Course(models.Model):
    DATE_PLAN = (
        ("by week", 1),
        ("by month", 2),
    )
    teacher = models.ForeignKey = ('Teacher')
    name = models.CharField(max_length=256,unique=True)
    websit = models.CharField(max_length=256)
    desciption = models.TextField(blank=True,null=True)
    startdate = models.DateField()
    enddate = models.DateField()
    starttime = models.TimeField()
    endtime = models.TimeField()
    dateplan = models.IntegerField(choices=DATE_PLAN,default=1)
    nextdate = models.IntegerField()
    level = models.CharField(max_length=256)
    typ = models.CharField(max_length=256)
    status = models.IntegerField()
    odj = models.CharField(max_length=256)

    def __str__(self):
        return name

class Student(models.Model):
    course = models.ManyToManyField('Course')
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=512)
    desciption = models.TextField(max_length=400, blank=True, null=True)
    picture = models.URLField(blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return name
