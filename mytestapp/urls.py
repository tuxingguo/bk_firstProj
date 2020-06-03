#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020-06-01 14:52
# @Author : tuxingguo
# @File : urls.py
# @Software : PyCharm

from django.conf.urls import url
from mytestapp import views


urlpatterns = (
    url(r'^mytestapp', views.myFunc),
)
