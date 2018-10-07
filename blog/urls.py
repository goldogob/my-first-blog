# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:35:35 2018

@author: abdinasir
"""
from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))