# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Student,Document,StudentDocument


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    current_student = Student.objects.get(student=request.user.id)
    context['CurrentStudent'] = current_student

    if current_student.course.is_cgpa:
        context['cgpa_or_percentage'] = str(current_student.cgpa) + '/10'
    else:
        context['cgpa_or_percentage'] = str(current_student.percentage)+' %'

    if current_student.division==1:
        context['class_division'] = str(current_student.division) + 'st'
    elif current_student.division==2:
        context['class_division'] = str(current_student.division) + 'nd'
    elif current_student.division==3:
        context['class_division'] = str(current_student.division) + 'rd'


    print(context)

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def list_all_documents(request):
    context = {}
    current_student = Student.objects.get(student=request.user.id)
    context['Documents'] = Document.objects.filter(college_id=current_student.college)
    context['CurrentStudent'] = current_student

    html_template = loader.get_template('home/tables.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def list_all_documents(request):
    context = {}
    current_student = Student.objects.get(student=request.user.id)
    context['Documents'] = Document.objects.filter(college_id=current_student.college)
    context['CurrentStudent'] = current_student

    html_template = loader.get_template('home/list_all_documents.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def download_document(request,document_id):
    context = {}
    current_student = Student.objects.get(student=request.user.id)
    context['Document'] = Document.objects.get(pk=document_id)
    context['document_requested'] = StudentDocument.objects.filter(document=context['Document'],student=current_student)
    context['CurrentStudent'] = current_student
    
    html_template = loader.get_template('home/download_document.html')
    return HttpResponse(html_template.render(context, request))