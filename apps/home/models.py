# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class College(models.Model):
    college_name = models.CharField(max_length=100, verbose_name="college name", help_text="name")
    college_address = models.CharField(max_length=100, verbose_name="address", help_text="address")
    college_estd = models.CharField(max_length=100, verbose_name="estd", help_text="estd")
    college_state =  models.CharField(max_length=100, verbose_name="state", help_text="state")
    college_affliated_to = models.CharField(max_length=100, verbose_name="affliation", help_text="affliation")
    college_type = models.CharField(max_length=100, verbose_name="type", help_text="type")
    college_zipcode = models.CharField(max_length=100, verbose_name="zipcode", help_text="zipcode")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class Course(models.Model):
    course_name = models.CharField(max_length=1000, verbose_name="course name", help_text="course name")
    course_code =  models.CharField(max_length=1000, verbose_name="course name", help_text="course name")
    course_intake = models.IntegerField(verbose_name="student intake", help_text="intake")
    college =  models.ForeignKey(College, on_delete=models.CASCADE)
    course_duration = models.FloatField(default = 0.0, blank=True)
    is_cgpa = models.BooleanField(default=False, verbose_name="is cgpa", help_text="is_cgpa")
    cgpa_scale = models.IntegerField(verbose_name="course cgpa scale", help_text="cgpa scale")
   



class Student(models.Model):
    due_amount = models.FloatField(default = 0.0, blank=True)
    cgpa = models.FloatField(default = 0.0, blank=True)
    percentage = models.FloatField(default = 0.0, blank=True)
    division = models.IntegerField(verbose_name="student class division", help_text="division")
    unique_id = models.CharField(max_length=1000, verbose_name="unique id", help_text="unique id")
    fathers_name = models.CharField(max_length=1000, verbose_name="name of father", help_text="fathers name")
    mothers_name = models.CharField(max_length=1000, verbose_name="mothers name", help_text="mothers name")
    admitted_year = models.IntegerField(verbose_name="year admitted", help_text="year admitted")
    total_tickets_opened = models.IntegerField(verbose_name="tickets raised total", help_text="total_tickets")
    total_tickets_closed = models.IntegerField(verbose_name="tickets closed total", help_text="total_tickets_closed")
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    college =  models.ForeignKey(College, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    

class Subject(models.Model):
    subject_name = models.CharField(max_length=1000, verbose_name="subject name", help_text="subject name")
    subject_code = models.CharField(max_length=1000, verbose_name="subject desc", help_text="subject desc")
    subject_semester = models.IntegerField(verbose_name="subject sem", help_text="sem taught in")
    subject_year = models.IntegerField(verbose_name="subject year", help_text="year taught in")
    credits = models.FloatField(default = 0.0, blank=True)
    max_marks = models.FloatField(default = 0.0, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #Describes break down of subjects like theory,practical,lab etc.
    # ex {'Practical':'25','Theory':'25','Quiz':'10'}
    # This will be created from the college panel mostly
    subject_marks_components = models.JSONField()

    # Decribe subject L-T-P-S breakdown
    # ex {'L':'4','T':'2','P':'2'} etc. Different college can create their own. that's why json.
    # This will be created from the college panel mostly
    subject_breakdown = models.JSONField()


class Marks(models.Model):
    marks_obtained = models.FloatField(default = 0.0, blank=True)
    max_marks = models.FloatField(default = 0.0, blank=True)
    grade = models.CharField(max_length=100, verbose_name="subject grade", help_text="subject grade")
    credits_awarded = models.FloatField(default = 0.0, blank=True)
    max_credits = models.FloatField(default = 0.0, blank=True)
    is_marks = models.BooleanField(default=False, verbose_name="is marks", help_text="ismarks")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    has_passed = models.BooleanField(default=False, verbose_name="pass or fail", help_text="pass/fail")
    # describes how much student has scored in subject components ex theory,lab,practicals etc
    #ex {'Practical':'50','Theory':'25','Quiz':'10'}
    scored_marks_components = models.JSONField()


class Document(models.Model):
    document_desc = models.CharField(max_length=100, verbose_name="document desc", help_text="document desc")
    base_cost = models.FloatField(default = 0.0, blank=True)
    gst_percentage = models.FloatField(default = 0.0, blank=True)
    delivery_charges = models.FloatField(default = 0.0, blank=True)
    download_charges = models.FloatField(default = 0.0, blank=True)
    download_gst_charges = models.FloatField(default = 0.0, blank=True)
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
    is_courier_available = models.BooleanField(default=False, verbose_name="is courier avail", help_text="is_delivery_avail?")
    extra_info = models.CharField(max_length=5000, verbose_name="document extra info", help_text="document info")

class StudentDocument(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    document_sl_no = models.CharField(max_length=1000, verbose_name="document serial no", help_text="serial no")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    document_url = models.CharField(max_length=2000, verbose_name="document url", help_text="url")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    





