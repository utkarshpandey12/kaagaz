# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('documents/', views.list_all_documents, name='list_all_documents'),
    path('documents/download/<int:document_id>/', views.download_document, name='download_document'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
